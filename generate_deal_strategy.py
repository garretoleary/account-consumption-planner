import csv
import os
import sys
from datetime import date
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


def main():
    prospects = {row["prospect"]: row for row in load_rows("prospects.csv")}
    cases = {row["use case"]: row for row in load_rows("cases.csv")}
    prospect = prospects["Qelvoryn Forgeworks"]
    case = cases[prospect["lookalike case"]]
    value = int(case["volume"]) * float(case["impact per case"]) * float(case["improvement factor"])

    prompt = f"""Write a concise one-page enterprise deal strategy in Markdown using only the invented data below. Do not research or imply that any detail is verified.

Today: {date.today().isoformat()}
Prospect: {prospect['prospect']} (highest prospect score: 9 points out of 9)
Industry: {prospect['industry']}
Size: {prospect['size']}
Trigger: {prospect['trigger']}
Warm route: {prospect['route in']}
Likely sponsor role: {prospect['likely sponsor role']}
Similar case: {case['use case']} ({case['status']})
Similar-case objective: {case['customer objective']}
Similar-case value inputs: {int(case['volume']):,} shift handovers per year; ${float(case['impact per case']):,.0f} {case['money counts']} per shift handover; {float(case['improvement factor']):.0%} potential improvement; ${value:,.0f} potential {case['money counts']} per year.
Similar-case usage: {int(case['expected added monthly tokens']):,} tokens per month.
Invented price: $10 per million tokens; this is not any vendor's real price.

Return Markdown only. Use these sections in this exact order:
# Qelvoryn Forgeworks deal strategy
**DRAFT — all figures, roles and dates are invented.**
## The decision
State who decides, who influences and who can block, using clearly invented role titles, and explain how the decision will be made.
## The commercial shape
Describe a small committed start in one division with usage on top and how it grows. Give concise reasoning. Every value figure must state its period and every number must say what it counts and its period. Do not repeat invented labels; the statement at the top covers all figures. Do not present the price as any vendor's real price or term.
## What must be true for them to say yes
## Risks to the deal and how each is reduced
Include the security and data review that every large enterprise runs before signing, who on our side answers it, and a mitigation for every risk.
## Joint plan to agree with the customer
Exactly five dated steps, chronologically from discovery to signature to first value. Use dates after today. The security and data review must take four to six weeks. Signature must be about three months after discovery. First value review must occur only after the full pilot period has elapsed. Every step must name an owner on their side and an owner on our side. Do not repeat invented labels beside dates or roles.
## What I would walk away from

Keep it to roughly one printed page. State that all figures, roles and dates are invented exactly once at the top and nowhere else."""

    try:
        response = OpenAI().responses.create(
            model="gpt-6-astra",
            reasoning={"effort": "low"},
            input=prompt,
        )
    except APIConnectionError:
        print("ERROR: The OpenAI API network connection is blocked or unavailable.", file=sys.stderr)
        raise SystemExit(3)

    print(response.output_text.strip())


if __name__ == "__main__":
    main()
