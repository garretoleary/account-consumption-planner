import csv
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

from dotenv import load_dotenv
from openai import APIConnectionError, OpenAI

from planner import (
    analyze,
    case_forecast_role,
    case_volume_label,
    customer_value_label,
    evaluate_division_pipeline,
    evidence_low_forecast,
)


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

if not os.environ.get("OPENAI_API_KEY"):
    print("ERROR: OPENAI_API_KEY was not found in .env.", file=sys.stderr)
    raise SystemExit(2)


def read_csv(filename):
    with (BASE_DIR / filename).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def money(value):
    return f"${value:,.0f}"


def main():
    usage = read_csv("usage.csv")
    cases = read_csv("cases.csv")
    targets = {row["account"]: float(row["next_quarter_revenue_target"]) for row in read_csv("targets.csv")}
    price = float(read_csv("prices.csv")[0]["price_per_million_tokens"])

    by_division = defaultdict(list)
    by_account_month = defaultdict(Counter)
    for row in usage:
        row["tokens"] = int(row["tokens"])
        row["seats"] = int(row["seats"])
        row["active users"] = int(row["active users"])
        by_division[(row["account"], row["division"])].append(row)
        by_account_month[row["account"]][row["month"]] += row["tokens"]
    for records in by_division.values():
        records.sort(key=lambda row: row["month"])

    months = sorted({row["month"] for row in usage})
    current_window_start = months[-3]
    cases_by_account = defaultdict(list)
    for case in cases:
        case["volume"] = int(case["volume"])
        case["impact per case"] = float(case["impact per case"])
        case["improvement factor"] = float(case["improvement factor"])
        case["expected added monthly tokens"] = int(case["expected added monthly tokens"])
        case["next quarter ramp percentage"] = float(case["next quarter ramp percentage"])
        cases_by_account[case["account"]].append(case)

    division_pipeline = {
        "Azrulon Energy Networks": ("Customer Systems", 0.20),
        "Norevix Capital Group": ("Markets Operations", 0.15),
        "Quorvane Therapeutics": ("Procurement", 0.20),
        "Talvexon Industrial Systems": ("Field Engineering", 0.20),
        "Veyrith Biologics": ("Supplier Quality", 0.20),
    }

    client = OpenAI()
    plans = []
    for account in sorted(by_account_month):
        footprints = []
        for (row_account, division), records in sorted(by_division.items()):
            if row_account != account:
                continue
            trend, signal = analyze(records, current_window_start)
            latest = records[-1]
            footprints.append(
                f"- {division}: {latest['stage']} at {latest['month']}; {trend} over 12 months; "
                f"{signal} in last 3 months; {latest['tokens']:,} tokens in latest month; "
                f"{latest['seats']:,} seats in latest month; {latest['active users']:,} active users in latest month"
            )

        case_lines = []
        middle_tokens = 0
        high_tokens = 0
        case_by_name = {}
        for case in cases_by_account[account]:
            case_by_name[case["use case"]] = case
            value = case["volume"] * case["impact per case"] * case["improvement factor"]
            annual_usage_cost = case["expected added monthly tokens"] * 12 / 1_000_000 * price
            customer_return = value / annual_usage_cost
            role = case_forecast_role(case)
            effective = case["expected added monthly tokens"] * 3 * case["next quarter ramp percentage"]
            if role == "middle":
                middle_tokens += effective
            elif role == "high only":
                high_tokens += effective
            risk = []
            if not case["sponsor"]:
                risk.append("no sponsor yet identified")
            if not case["owner"]:
                risk.append("no owner yet identified")
            case_lines.append(
                f"- {case['use case']} in {case['division']}: objective '{case['customer objective']}'; "
                f"{case['status']}; {case['volume']:,} {case_volume_label(case)}/year × "
                f"{money(case['impact per case'])}/"
                f"{'shift handover' if case_volume_label(case) == 'shift handovers' else 'case'} × "
                f"{case['improvement factor']:.0%}/year = {money(value)}/year of {customer_value_label(case)}; "
                f"yearly usage cost = {case['expected added monthly tokens']:,} tokens/month × 12 months/year ÷ "
                f"1,000,000 tokens × {money(price)}/million tokens = {money(annual_usage_cost)}/year; "
                f"customer return = {money(value)}/year of {customer_value_label(case)} ÷ "
                f"{money(annual_usage_cost)}/year = {customer_return:.2f}×; "
                f"separate plain measure, not the source of the money value: {case['plain measure']}; "
                f"forecast role: {role}; "
                f"ownership: sponsor={case['sponsor'] or 'missing'}, owner={case['owner'] or 'missing'}"
                f"{'; risk=' + ', '.join(risk) if risk else ''}"
            )

        monthly = [by_account_month[account][month] for month in months]
        low_tokens = evidence_low_forecast(monthly)
        pipeline_division, pipeline_ramp = division_pipeline[account]
        pipeline_evaluation = evaluate_division_pipeline(
            account,
            pipeline_division,
            pipeline_ramp,
            cases_by_account[account],
            by_division[(account, pipeline_division)][-1],
        )
        pipeline_tokens = pipeline_evaluation["tokens"]
        forecasts = [
            low_tokens / 1_000_000 * price,
            (low_tokens + middle_tokens) / 1_000_000 * price,
            (low_tokens + middle_tokens + high_tokens + pipeline_tokens) / 1_000_000 * price,
        ]

        prompt = f"""Write a concise enterprise account plan using only the invented data below. Do not research or add unsupported customer facts.

Account: {account}
Current footprint at {months[-1]}:
{chr(10).join(footprints)}

Next-quarter forecast covering 3 months:
- target: {money(targets[account])} for the next quarter
- low: {money(forecasts[0])} for the next quarter
- middle: {money(forecasts[1])} for the next quarter
- high: {money(forecasts[2])} for the next quarter

Value cases:
{chr(10).join(case_lines)}

Known next-division pipeline candidate: {pipeline_division}, at {pipeline_ramp:.0%} ramp during the next quarter. Eligibility: {pipeline_evaluation['reason']}. Eligible pipeline tokens: {pipeline_tokens:,.0f} for the next quarter.
Recovery rule: an account in recovery counts no proposed case and no pipeline.
Division pipeline counts in high only when active users are above half of seats, a case fits the division's own work, and that case is not already counted.

Return Markdown only, with these sections in this exact order:
# {account} account plan
**DRAFT — invented data.**
## The customer's objectives
State objectives only from the available value cases. Every use case used later must tie explicitly to one of these objectives.
## Stakeholders by function
Use invented role titles organized by function. Do not claim named people exist.
## Current footprint by division and stage
Include every division, its latest stage, 12-month trend, last-three-month signal, and latest-month usage. Label every number with what it counts and its period.
## Next divisions to open
Rank the best two or three non-production divisions, highest value and lowest effort first. For each, state an effort rating of low, medium or high and label it as an estimate; give a one-line reason. Tie one available use case to a stated objective. Show its annual business-case working, annual usage-cost working and customer return. Do not invent a new value case or new numeric input.
## Risks
Include every division with a decline signal and every available case missing a sponsor or owner. Include other material risks supported by the data.
## Twelve-month plan by quarter
Give four sequential quarters, each covering three months. Use Q1 through Q4 rather than calendar quarters. Label every numeric target as an estimate and state its period. Keep actions grounded in the data.

State that the plan is a draft on invented data exactly once at the top. Do not repeat invented labels on every line."""

        try:
            response = client.responses.create(
                model="gpt-6-astra",
                reasoning={"effort": "low"},
                input=prompt,
            )
        except APIConnectionError:
            print("ERROR: The OpenAI API network connection is blocked or unavailable.", file=sys.stderr)
            raise SystemExit(3)
        plans.append(response.output_text.strip())

    print("\n\n---ACCOUNT-PLAN-SEPARATOR---\n\n".join(plans))


if __name__ == "__main__":
    main()
