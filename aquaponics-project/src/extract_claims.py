from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import yaml
import sys
from pathlib import Path
from datetime import datetime, UTC

# ----------------------------
# Paths
# ----------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

INPUT_DIR = PROJECT_ROOT / "data" / "sources" / "input"
RUN_CONFIGS_DIR = PROJECT_ROOT / "data" / "sources" / "run_configs"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
RUNS_DIR = PROJECT_ROOT / "data" / "logs" / "extraction_runs"
CONFIG_DIR = PROJECT_ROOT / "configs"

MODEL_POLICY_PATH = CONFIG_DIR / "model_policy.yaml"
DEFAULT_RUN_CONFIG_PATH = INPUT_DIR / "run_config.yaml"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RUNS_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Environment
# ----------------------------
load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

# ----------------------------
# Load model policy
# ----------------------------
if not MODEL_POLICY_PATH.exists():
    raise FileNotFoundError(f"Missing model policy file: {MODEL_POLICY_PATH}")

with open(MODEL_POLICY_PATH, "r", encoding="utf-8") as f:
    model_policy = yaml.safe_load(f) or {}

extract_stage = (model_policy.get("stages") or {}).get("extract")
if not extract_stage:
    raise ValueError("Missing 'extract' stage in model_policy.yaml")

USE_LLM = extract_stage.get("use_llm", True)
MODEL_NAME = extract_stage.get("model")
REASONING_EFFORT = extract_stage.get("reasoning_effort", "low")

if not USE_LLM:
    raise ValueError("Extract stage is configured with use_llm: false, but extract_claims.py requires an LLM")

if not MODEL_NAME:
    raise ValueError("No model configured for extract stage in model_policy.yaml")

# ----------------------------
# Pick run config file
# Usage:
#   python src/extract_claims.py fao_ch02.yaml
# If no argument is given, fallback to data/sources/input/run_config.yaml
# ----------------------------
if len(sys.argv) > 1:
    run_config_name = sys.argv[1]
    RUN_CONFIG_PATH = RUN_CONFIGS_DIR / run_config_name
else:
    RUN_CONFIG_PATH = DEFAULT_RUN_CONFIG_PATH

if not RUN_CONFIG_PATH.exists():
    raise FileNotFoundError(f"Run config file not found: {RUN_CONFIG_PATH}")

# ----------------------------
# Load run config
# ----------------------------
with open(RUN_CONFIG_PATH, "r", encoding="utf-8") as f:
    run_config = yaml.safe_load(f) or {}

INPUT_FILENAME = run_config.get("input_filename")
SOURCE_ID = run_config.get("source_id")
SECTION_ID = run_config.get("section_id")
SOURCE_TYPE = run_config.get("source_type")

missing_fields = []
for field_name, field_value in [
    ("input_filename", INPUT_FILENAME),
    ("source_id", SOURCE_ID),
    ("section_id", SECTION_ID),
    ("source_type", SOURCE_TYPE),
]:
    if not field_value:
        missing_fields.append(field_name)

if missing_fields:
    raise ValueError(f"Missing required fields in run config: {', '.join(missing_fields)}")

INPUT_PATH = INPUT_DIR / INPUT_FILENAME
if not INPUT_PATH.exists():
    raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

source_text = INPUT_PATH.read_text(encoding="utf-8").strip()
if not source_text:
    raise ValueError(f"Input file is empty: {INPUT_PATH}")

# ----------------------------
# Prompt
# ----------------------------
prompt = f"""
You extract structured aquaponics knowledge from technical text.

Rules:
- Return valid JSON only.
- Do not invent facts.
- Stay close to the source text.
- If something is unclear, put it in unresolved_items.
- Keep statements atomic and precise.
- Use only these top-level keys:
  entities, claims, parameters, processes, risks, unresolved_items

Return this exact JSON structure:
{{
  "entities": [
    {{
      "entity_id": "string",
      "name": "string",
      "entity_type": "organism | chemical | process | infrastructure | operational_factor | environmental_factor"
    }}
  ],
  "claims": [
    {{
      "claim_id": "string",
      "statement": "string",
      "domain": "biology | water_chemistry | system_design | operations | risk",
      "claim_type": "definition | process | dependency | risk | parameter",
      "confidence": "high | medium | low"
    }}
  ],
  "parameters": [
    {{
      "parameter_id": "string",
      "name": "string",
      "description": "string",
      "unit": "string | null"
    }}
  ],
  "processes": [
    {{
      "process_id": "string",
      "name": "string",
      "inputs": ["string"],
      "outputs": ["string"],
      "drivers": ["string"]
    }}
  ],
  "risks": [
    {{
      "risk_id": "string",
      "name": "string",
      "description": "string",
      "severity": "high | medium | low"
    }}
  ],
  "unresolved_items": [
    {{
      "item_id": "string",
      "issue": "string"
    }}
  ]
}}

Source metadata:
- source_id: {SOURCE_ID}
- section_id: {SECTION_ID}
- source_type: {SOURCE_TYPE}

Text:
\"\"\"
{source_text}
\"\"\"
"""

# ----------------------------
# Model call
# ----------------------------
response = client.responses.create(
    model=MODEL_NAME,
    reasoning={"effort": REASONING_EFFORT},
    input=prompt
)

raw_output = response.output_text.strip()

# ----------------------------
# Parse JSON
# ----------------------------
try:
    extracted = json.loads(raw_output)
except json.JSONDecodeError:
    bad_output_path = OUTPUT_DIR / "bad_model_output.txt"
    bad_output_path.write_text(raw_output, encoding="utf-8")
    raise ValueError(
        f"Model did not return valid JSON. Raw output saved to {bad_output_path}"
    )

# ----------------------------
# Package result
# ----------------------------
run_timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
run_id = f"extract_{SOURCE_ID}_{run_timestamp}"

package = {
    "run_id": run_id,
    "model_policy": {
        "stage": "extract",
        "model": MODEL_NAME,
        "reasoning_effort": REASONING_EFFORT
    },
    "run_config_file": str(RUN_CONFIG_PATH.relative_to(PROJECT_ROOT)),
    "run_config": {
        "input_filename": INPUT_FILENAME,
        "source_id": SOURCE_ID,
        "section_id": SECTION_ID,
        "source_type": SOURCE_TYPE
    },
    "source_metadata": {
        "source_id": SOURCE_ID,
        "section_id": SECTION_ID,
        "source_type": SOURCE_TYPE,
        "input_filename": INPUT_FILENAME,
        "extracted_at_utc": run_timestamp
    },
    "extraction": extracted
}

# ----------------------------
# Save outputs
# ----------------------------
output_filename = f"{SOURCE_ID}_{SECTION_ID}_{run_timestamp}.json"

data_output_path = OUTPUT_DIR / output_filename
repo_output_path = RUNS_DIR / output_filename

with open(data_output_path, "w", encoding="utf-8") as f:
    json.dump(package, f, indent=2)

with open(repo_output_path, "w", encoding="utf-8") as f:
    json.dump(package, f, indent=2)

print(f"Using model: {MODEL_NAME}")
print(f"Reasoning effort: {REASONING_EFFORT}")
print(f"Using run config: {RUN_CONFIG_PATH}")
print(f"Saved extraction to:")
print(f" - {data_output_path}")
print(f" - {repo_output_path}")
print(json.dumps(package['source_metadata'], indent=2))
