from pathlib import Path
import subprocess
import sys
import json
import os
import yaml
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_POLICY_PATH = PROJECT_ROOT / "configs" / "model_policy.yaml"

SAFE_READ_ROOTS = [
    PROJECT_ROOT / "data",
    PROJECT_ROOT / "data" / "knowledge",
]

SCRIPT_MAP = {
    "build_update_packet_from_report": PROJECT_ROOT / "src" / "build_update_packet_from_report.py",
    "apply_update_packet": PROJECT_ROOT / "src" / "apply_update_packet.py",
    "run_tradeoff_matrix": PROJECT_ROOT / "src" / "run_tradeoff_matrix.py",
    "simulate_n_days": PROJECT_ROOT / "src" / "simulate_n_days.py",
    "build_learning_packet_from_simulation": PROJECT_ROOT / "src" / "build_learning_packet_from_simulation.py",
    "apply_learning_packet": PROJECT_ROOT / "src" / "apply_learning_packet.py",
}

SYSTEM_PROMPT = """
You are the aquaponics update orchestrator.

Your job:
- convert approved local digests into local update packets
- apply updates using approved tools
- rerun simulations
- build and apply learning packets
- summarize what changed

Rules:
- never modify atomic facts directly
- never rewrite simulation code
- use only the provided tools
- prefer local deterministic tools over freeform reasoning
- if a tool fails, explain the failure clearly
"""

TOOLS = [
    {
        "type": "function",
        "name": "build_update_packet_from_report",
        "description": "Build latest_update_packet.json from the latest structured species report digest.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "apply_update_packet",
        "description": "Apply the current latest_update_packet.json to local species and evidence JSON files.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "run_tradeoff_matrix",
        "description": "Run the local tradeoff matrix simulation and save tradeoff_matrix_results.json.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "simulate_n_days",
        "description": "Run the local multi-day simulator for a scenario file.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "scenario_path": {
                    "type": "string",
                    "description": "Relative path to the scenario JSON file from the project root.",
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days to simulate.",
                },
            },
            "required": ["scenario_path", "days"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "build_learning_packet_from_simulation",
        "description": "Build latest_learning_packet.json from the latest simulation outputs and tuning reports.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "apply_learning_packet",
        "description": "Apply latest_learning_packet.json into evidence maps, model tickets, and scenario defaults.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "read_json",
        "description": "Read a local JSON file from an approved folder and return its contents.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path to a JSON file under data/.",
                }
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
]


def load_model_policy() -> dict:
    if MODEL_POLICY_PATH.exists():
        with open(MODEL_POLICY_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


policy = load_model_policy()

MODEL = (
    policy.get("api_bot", {}).get("model")
    or policy.get("orchestrator", {}).get("model")
    or os.getenv("OPENAI_MODEL")
    or "gpt-5"
)

REASONING_EFFORT = (
    policy.get("api_bot", {}).get("reasoning_effort")
    or policy.get("orchestrator", {}).get("reasoning_effort")
    or "medium"
)

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=API_KEY)


def assert_safe_read_path(relative_path: str) -> Path:
    path = (PROJECT_ROOT / relative_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".json":
        raise PermissionError(f"Only JSON files may be read with read_json: {path}")

    if not any(str(path).startswith(str(root.resolve())) for root in SAFE_READ_ROOTS):
        raise PermissionError(f"Read path not allowed: {path}")

    return path


def run_python_script(script_path: Path, args: list[str] | None = None) -> str:
    if not script_path.exists():
        raise FileNotFoundError(f"Missing script: {script_path}")

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Script failed: {script_path.name}\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    return result.stdout.strip()


def dispatch_tool(name: str, args: dict) -> str:
    if name == "build_update_packet_from_report":
        return run_python_script(SCRIPT_MAP[name])

    if name == "apply_update_packet":
        return run_python_script(SCRIPT_MAP[name])

    if name == "run_tradeoff_matrix":
        return run_python_script(SCRIPT_MAP[name])

    if name == "simulate_n_days":
        scenario_path = args["scenario_path"]
        days = str(args["days"])
        return run_python_script(SCRIPT_MAP[name], [scenario_path, days])

    if name == "build_learning_packet_from_simulation":
        return run_python_script(SCRIPT_MAP[name])

    if name == "apply_learning_packet":
        return run_python_script(SCRIPT_MAP[name])

    if name == "read_json":
        path = assert_safe_read_path(args["path"])
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    raise ValueError(f"Unknown tool: {name}")


def create_response(input_payload, previous_response_id: str | None = None):
    kwargs = {
        "model": MODEL,
        "input": input_payload,
        "tools": TOOLS,
        "parallel_tool_calls": False,
        "reasoning": {"effort": REASONING_EFFORT},
    }

    if previous_response_id is not None:
        kwargs["previous_response_id"] = previous_response_id

    return client.responses.create(**kwargs)


def run_bot(user_task: str) -> str:
    response = create_response(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_task},
        ]
    )

    while True:
        tool_calls = [item for item in response.output if item.type == "function_call"]

        if not tool_calls:
            return response.output_text

        tool_outputs = []
        for call in tool_calls:
            try:
                args = json.loads(call.arguments) if call.arguments else {}
                result = dispatch_tool(call.name, args)
            except Exception as e:
                result = json.dumps({"error": str(e)})

            tool_outputs.append(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": result,
                }
            )

        response = create_response(
            tool_outputs,
            previous_response_id=response.id,
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError(
            "Usage:\n"
            "python src\\api_bot.py \"<task instruction>\"\n\n"
            "Example:\n"
            "python src\\api_bot.py \"Build the latest update packet, apply it, run the tradeoff matrix, simulate 7 days on data\\simulation\\scenarios\\starter_tilapia_lettuce_system.json, then build and apply the learning packet and summarize the result.\""
        )

    task = " ".join(sys.argv[1:])
    final_text = run_bot(task)

    print("\n=== Bot summary ===")
    print(final_text)
