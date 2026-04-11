from pathlib import Path
import json
from datetime import datetime, UTC

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DIGEST_PATH = PROJECT_ROOT / "data" / "knowledge" / "report_digests" / "latest_intervention_digest.json"
DEFAULTS_PATH = PROJECT_ROOT / "data" / "simulation" / "scenario_defaults.json"
OUTPUT_PATH = PROJECT_ROOT / "data" / "knowledge" / "tuning_packets" / "latest_scenario_tuning_packet.json"


def load_json(path: Path, default=None):
    if not path.exists():
        return {} if default is None else default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_starting_defaults() -> dict:
    defaults_doc = load_json(DEFAULTS_PATH, default={})
    experimental = defaults_doc.get("experimental_defaults", {})

    return {
        "feed_rate_percent_body_weight_per_day": experimental.get("feed_rate_percent_body_weight_per_day", 2.0),
        "plant_count": experimental.get("plant_count", 90),
        "biofilter_maturity": experimental.get("biofilter_maturity", 0.9),
        "water_volume_l": experimental.get("water_volume_l", 4000.0),
        "mode": experimental.get("mode", "robust_compromise_mode")
    }


def maybe_pick_numeric(change: str, candidates: list[float | int]) -> float | int | None:
    for candidate in candidates:
        if str(candidate) in change:
            return candidate
    return None


def pick_best_tuning_values(ideas: list[dict], base: dict) -> dict:
    """
    Start from best-known experimental defaults.
    Only override if the intervention digest clearly suggests a numeric value.
    Never silently downgrade known-good settings unless the digest explicitly says so.
    """
    result = dict(base)

    for idea in ideas:
        setting = str(idea.get("setting", "")).lower()
        change = str(idea.get("suggested_change", "")).lower()

        # feed
        if "feed" in setting:
            picked = maybe_pick_numeric(change, [1.0, 1.25, 1.5, 1.75, 2.0])
            if picked is not None:
                result["feed_rate_percent_body_weight_per_day"] = picked

        # plant count
        if "plant" in setting:
            picked = maybe_pick_numeric(change, [90, 120, 150])
            if picked is not None:
                result["plant_count"] = picked

        # biofilter
        if "biofilter" in setting:
            if "1.0" in change or "100%" in change:
                result["biofilter_maturity"] = 1.0
            elif "0.9" in change or "90%" in change:
                # only allow downgrade if explicitly requested
                result["biofilter_maturity"] = 0.9

        # water volume
        if "water volume" in setting or "volume" in setting:
            picked = maybe_pick_numeric(change, [4000.0, 5000.0, 6000.0])
            if picked is not None:
                result["water_volume_l"] = float(picked)

        # mode
        if "mode" in setting or "ph mode" in setting:
            if "plant_yield_optimization_mode" in change:
                result["mode"] = "plant_yield_optimization_mode"
            elif "robust_compromise_mode" in change:
                result["mode"] = "robust_compromise_mode"

    return result


def main():
    source = load_json(DIGEST_PATH)
    digest = source.get("digest", {})
    ideas = digest.get("recommended_tuning_ideas", [])

    starting_defaults = get_starting_defaults()
    chosen = pick_best_tuning_values(ideas, starting_defaults)

    packet = {
        "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_digest_file": str(DIGEST_PATH),
        "scenario_filename": "starter_tilapia_lettuce_system.json",
        "selection_notes": {
            "logic": "start_from_experimental_defaults_then_apply_explicit_digest_overrides",
            "idea_count_seen": len(ideas),
            "starting_defaults": starting_defaults
        },
        "set_fields": {
            "feeding": {
                "feed_rate_percent_body_weight_per_day": chosen["feed_rate_percent_body_weight_per_day"]
            },
            "plant_crop": {
                "plant_count": chosen["plant_count"]
            },
            "system": {
                "biofilter_maturity": chosen["biofilter_maturity"],
                "water_volume_l": chosen["water_volume_l"],
                "mode": chosen["mode"]
            },
            "operations_policy": {
                "target_pH_mode": chosen["mode"]
            }
        }
    }

    save_json(OUTPUT_PATH, packet)

    print(f"Built tuning packet from intervention digest: {DIGEST_PATH}")
    print(f"Saved tuning packet to: {OUTPUT_PATH}")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
