import csv
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import APIConnectionError, OpenAI


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

if not os.environ.get("OPENAI_API_KEY"):
    print("ERROR: OPENAI_API_KEY was not found in .env.", file=sys.stderr)
    raise SystemExit(2)


def load_rows(filename):
    with (BASE_DIR / filename).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def build_prompt(prospect, case):
    value = int(case["volume"]) * float(case["impact per case"]) * float(case["improvement factor"])
    case_unit = "shift handovers" if case["use case"] == "Shift handover synthesis" else "cases"
    case_unit_singular = "shift handover" if case["use case"] == "Shift handover synthesis" else "case"
    pilot_length = "six-week" if prospect["prospect"] == "Qelvoryn Forgeworks" else "fixed-length"
    working = (
        f"{int(case['volume']):,} {case_unit} per year × "
        f"${float(case['impact per case']):,.0f} {case['money counts']} per {case_unit_singular} × "
        f"{float(case['improvement factor']):.0%} potential improvement per year = "
        f"${value:,.0f} potential {case['money counts']} per year"
    )
    regulated = prospect["industry"] in {"life sciences", "financial services", "energy"}
    compliance_instruction = (
        "Include a section headed exactly '## Compliance, privacy and security questions'. "
        "Write exactly six questions the customer will ask us: validation, data location, access, retention, "
        "security, and whether their data will be used to train our models. For each, name a role "
        "on our side who answers and a role on their side who must approve. Do not repeat invented labels beside roles."
        if regulated
        else "Do not include a compliance section because this prospect is not marked as a regulated industry."
    )
    return f"""Write one concise discovery call brief using only the invented data below. Do not research or imply that any fact was verified.

Prospect: {prospect['prospect']}
Industry: {prospect['industry']}
Size: {prospect['size']}
Trigger: {prospect['trigger']}
Route in: {prospect['route in']}
Likely sponsor role: {prospect['likely sponsor role']}
Lookalike case: {case['use case']}
Lookalike customer objective: {case['customer objective']}
Lookalike value working: {working}
Lookalike plain measure: {case['plain measure']}. This is a separate result and is not the source of the money value.

Return Markdown only, with these sections in this exact order:
# {prospect['prospect']} discovery call brief
**DRAFT — all figures, roles and dates are invented.**
## Why you, why now
Exactly two sentences explaining why this prospect should take the call now, grounded in the trigger. Do not explain how we reached them.
## Value hypothesis
One hypothesis drawn from the similar case. Include the complete value working and say what the money counts. Label every number with what it counts and its period. If you include the plain measure beside the money value, say explicitly that it is a separate result and is not the source of the money value. Explicitly label it 'Hypothesis to test — not a promise.'
## Five discovery questions
Exactly five numbered questions, in this order: what is most at risk, what the problem costs them, what they have already tried, who feels it most, and what else competes for attention. Questions only; no selling. Do not name our solution, ask for a sponsor, or mention a pilot.
## Likely objection
One likely objection.
## Honest answer
One candid answer that does not overclaim. In customer-facing words, do not say 'invented' or 'lookalike'; say that a similar case elsewhere does not prove it would work for them.
## Small first step to propose
A {pilot_length} pilot in one division with one agreed measure and a fixed baseline.
{compliance_instruction}
## My opening

Leave 'My opening' completely empty. End immediately after that heading. State that all figures, roles and dates are invented exactly once at the top and nowhere else."""


def main():
    prospects = {row["prospect"]: row for row in load_rows("prospects.csv")}
    cases = {row["use case"]: row for row in load_rows("cases.csv")}
    chosen = sys.argv[1:] or ["Qelvoryn Forgeworks", "Zynthara Biosystems", "Virelqua Process Labs"]
    unknown = [name for name in chosen if name not in prospects]
    if unknown:
        print(f"ERROR: Unknown prospect: {', '.join(unknown)}", file=sys.stderr)
        raise SystemExit(4)
    client = OpenAI()
    briefs = []

    try:
        for name in chosen:
            prospect = prospects[name]
            case = cases[prospect["lookalike case"]]
            response = client.responses.create(
                model="gpt-6-astra",
                reasoning={"effort": "low"},
                input=build_prompt(prospect, case),
            )
            brief = response.output_text.strip()
            opening_heading = "## My opening"
            if opening_heading not in brief:
                raise ValueError(f"Missing My opening section for {name}")
            brief = brief.split(opening_heading, 1)[0].rstrip() + f"\n\n{opening_heading}\n"
            briefs.append(brief)
    except APIConnectionError:
        print("ERROR: The OpenAI API network connection is blocked or unavailable.", file=sys.stderr)
        raise SystemExit(3)

    print("\n\n---BRIEF-SEPARATOR---\n\n".join(briefs))


if __name__ == "__main__":
    main()
