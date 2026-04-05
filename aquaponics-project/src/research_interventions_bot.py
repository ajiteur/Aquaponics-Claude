from pathlib import Path
import json
import os
import re
import sys
import yaml
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_POLICY_PATH = PROJECT_ROOT / "configs" / "model_policy.yaml"

MULTI_DAY_SUMMARY_PATH = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
LEARNING_PACKET_PATH = PROJECT_ROOT / "data" / "learning_packets" / "latest_learning_packet.json"
OUTPUT_PATH = PROJECT_ROOT / "data" / "report_digests" / "latest_intervention_digest.json"

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=API_KEY)


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_model_policy() -> dict:
    if MODEL_POLICY_PATH.exists():
        with open(MODEL_POLICY_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def get_model_settings(policy: dict) -> tuple[str, str]:
    model = (
        policy.get("research_bot", {}).get("model")
        or policy.get("stages", {}).get("discovery", {}).get("model")
        or os.getenv("OPENAI_MODEL")
        or "gpt-5"
    )

    reasoning_effort = (
        policy.get("research_bot", {}).get("reasoning_effort")
        or policy.get("stages", {}).get("discovery", {}).get("reasoning_effort")
        or "medium"
    )

    return model, reasoning_effort


def extract_json_from_text(text: str) -> dict:
    text = text.strip()

    fenced = re.search(r"```json\s*(\{.*\})\s*```", text, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    bare = re.search(r"(\{.*\})", text, re.DOTALL)
    if bare:
        return json.loads(bare.group(1))

    raise ValueError("Could not find JSON object in model output.")


def extract_sources(response_dict: dict) -> list[dict]:
    sources = []

    for item in response_dict.get("output", []):
        if item.get("type") == "web_search_call":
            action = item.get("action") or {}
            raw_sources = action.get("sources") or []

            for src in raw_sources:
                if not isinstance(src, dict):
                    continue
                sources.append({
                    "type": src.get("type"),
                    "title": src.get("title"),
                    "url": src.get("url")
                })

        if item.get("type") == "message":
            for content in item.get("content", []) or []:
                for ann in content.get("annotations", []) or []:
                    if ann.get("type") == "url_citation":
                        sources.append({
                            "type": "url_citation",
                            "title": ann.get("title"),
                            "url": ann.get("url")
                        })

    # de-duplicate
    seen = set()
    deduped = []
    for src in sources:
        key = (src.get("title"), src.get("url"))
        if key not in seen:
            deduped.append(src)
            seen.add(key)

    return deduped


def build_context() -> dict:
    summary = load_json(MULTI_DAY_SUMMARY_PATH, default=[])
    final_day = summary[-1] if summary else None
    learning_packet = load_json(LEARNING_PACKET_PATH, default={})

    return {
        "final_day": final_day,
        "learning_packet_summary": {
            "simulation_observations": len(learning_packet.get("simulation_observations", [])),
            "model_update_proposals": len(learning_packet.get("model_update_proposals", [])),
            "parameter_library_proposals": len(learning_packet.get("parameter_library_proposals", []))
        }
    }


def build_prompt(context: dict, issue: str) -> str:
    final_day = context.get("final_day") or {}

    return f"""
You are building a structured intervention digest for an aquaponics simulation project.

Problem focus:
{issue}

Current simulation context:
- day: {final_day.get("day")}
- pH: {final_day.get("pH")}
- TAN mg/L: {final_day.get("tan_mg_L")}
- unionized NH3 mg/L: {final_day.get("unionized_nh3_mg_L")}
- nitrate mg/L: {final_day.get("nitrate_mg_L")}
- fish biomass kg: {final_day.get("fish_biomass_kg")}
- plant avg biomass g: {final_day.get("plant_avg_biomass_g")}
- daily operating cost: {final_day.get("daily_operating_cost")}
- system stability score: {final_day.get("system_stability_score")}

Research goal:
Find high-trust methods or interventions that can reduce high TAN, high unionized NH3, or unstable pH in aquaponics or closely related recirculating aquaculture / aquaculture systems.

Source policy:
- Prioritize Tier 1 and Tier 2 sources only:
  - FAO
  - university extension / experiment stations
  - peer-reviewed journals
  - official manuals or standards
  - UVI / SRAC / Texas A&M / similar institutional sources
- Exclude commercial blogs and vendor content unless explicitly used only as a low-trust comparison
- Prefer PDFs, official pages, university-hosted files, and open-access sources

Return JSON only with this exact structure:
{{
  "problem_focus": "...",
  "executive_summary": "...",
  "interventions": [
    {{
      "intervention_name": "...",
      "problem_target": ["high_tan", "high_nh3", "high_ph", "low_ph", "nitrification_instability"],
      "mechanism": "...",
      "expected_effects": ["..."],
      "when_to_use": "...",
      "tradeoffs_or_costs": ["..."],
      "source_type": "...",
      "trust_tier": "tier_1 or tier_2",
      "source_name": "...",
      "source_quote_or_close_paraphrase": "...",
      "recommendation_status": "experimental_scenario_tuning or provisional_operational_guidance or contradiction_ticket"
    }}
  ],
  "recommended_tuning_ideas": [
    {{
      "setting": "...",
      "suggested_change": "...",
      "reason": "..."
    }}
  ],
  "notes_for_atomic_facts": [
    "..."
  ]
}}

Important:
- Prefer interventions relevant to coupled aquaponics systems
- Separate emergency actions from longer-term design changes
- Do not promote anything directly to accepted atomic facts
- If evidence is context-dependent, say so
"""


def main():
    issue = (
        "high unionized NH3 and TAN over a 7-day aquaponics run"
        if len(sys.argv) < 2
        else " ".join(sys.argv[1:])
    )

    policy = load_model_policy()
    model, reasoning_effort = get_model_settings(policy)
    context = build_context()
    prompt = build_prompt(context, issue)

    response = client.responses.create(
        model=model,
        reasoning={"effort": reasoning_effort},
        tools=[
            {
                "type": "web_search",
                "filters": {
                    "allowed_domains": [
                        "openknowledge.fao.org",
                        "fao.org",
                        "extension.okstate.edu",
                        "pubs.nmsu.edu",
                        "ctahr.hawaii.edu",
                        "www.uvi.edu",
                        "agrilifeextension.tamu.edu",
                        "srac.tamu.edu",
                        "aquaculture.ca.uky.edu",
                        "ccd.uky.edu",
                        "extension.uga.edu",
                        "edis.ifas.ufl.edu",
                        "pubmed.ncbi.nlm.nih.gov",
                        "frontiersin.org",
                        "mdpi.com",
                        "link.springer.com"
                    ]
                }
            }
        ],
        include=["web_search_call.action.sources"],
        input=prompt
    )

    response_dict = response.model_dump()
    output_text = response.output_text
    parsed = extract_json_from_text(output_text)
    sources = extract_sources(response_dict)

    digest = {
        "generated_from": "research_interventions_bot",
        "issue": issue,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "context": context,
        "digest": parsed,
        "sources": sources
    }

    save_json(OUTPUT_PATH, digest)

    print(f"Saved intervention digest to: {OUTPUT_PATH}")
    print(json.dumps({
        "issue": issue,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "intervention_count": len(parsed.get("interventions", [])),
        "recommended_tuning_ideas_count": len(parsed.get("recommended_tuning_ideas", [])),
        "source_count": len(sources)
    }, indent=2))


if __name__ == "__main__":
    main()