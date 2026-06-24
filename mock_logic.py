import json
from typing import Any


# --- LOADER ---
def load_test_cases() -> dict[str, Any]:
    """Loads the Golden Artifacts from JSON."""
    try:
        with open("test_cases.json") as f:
            return json.load(f)  # type: ignore[no-any-return]
    except Exception as e:
        print(f"CRITICAL ERROR: Could not load test_cases.json - {e}")
        return {}


# --- INTELLIGENCE ROUTER ---
def get_smart_response(
    user_prompt: str, uploaded_file_name: str | None
) -> tuple[str, str]:
    """
    Metadata Trigger Logic.
    Returns: (Response Text, Scenario Key)
    """
    cases = load_test_cases()
    prompt_lower = user_prompt.lower()
    file_lower = uploaded_file_name.lower() if uploaded_file_name else ""

    # Check Filenames for failure trigger
    if "fail" in file_lower or "error" in file_lower:
        return "SYSTEM_CRITICAL_FAILURE_500", "failure_test"

    # 1. ROUTING LOGIC
    # Default State
    scenario = "general"
    response_text = None

    # 1A. PRIMARY ROUTING: BY FILENAME
    # Expanded for PEP 8 Compliance (E701 Fix)
    if "geometry" in file_lower:
        scenario = "geometry"
    elif "algebra" in file_lower:
        scenario = "algebra"
    elif "graph" in file_lower:
        scenario = "graph"
    elif "handwritten" in file_lower:
        scenario = "handwritten"
    elif "trick" in file_lower:
        scenario = "trick"
    elif "trial" in file_lower or "pdf" in file_lower:
        scenario = "pdf_test"

    # 1B. FALLBACK ROUTING: BY KEYWORDS
    # Only if filename didn't catch it
    if scenario == "general":
        for key, data in cases.items():
            if any(k in prompt_lower for k in data.get("trigger_keywords", [])):
                scenario = key
                break

    # 2. RETRIEVE TEXT
    if scenario in cases:
        response_text = cases[scenario]["response"]

    # 3. FOLLOW-UP LOGIC (Conversational)
    # If no specific image match, check if user is asking for clarification
    if not response_text:
        if any(
            kw in prompt_lower for kw in ["explain", "why", "how", "detail", "step"]
        ):
            # Hardcoded follow-up example for the demo
            response_text = """
### Step Clarification
Certainly. Let's look closer at the **Substitution Method**.

We replaced variable $y$ with $(3 - x)$ because the first equation gave us a direct relationship.
$$ 2x + 3(3 - x) = 12 $$

This reduces the problem to a single variable ($x$), allowing us to solve it linearly.
            """
            scenario = "general"  # Use generic thinking steps for follow-ups

    # 4. FINAL FALLBACK
    if not response_text:
        response_text = cases.get("general", {}).get("response", "No mock data found.")

    return response_text, scenario
