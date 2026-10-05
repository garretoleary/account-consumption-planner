import csv
from collections import Counter, defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RECOVERY_ACCOUNTS = {"Norevix Capital Group"}


def format_table(headers, rows):
    widths = [len(header) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(str(value)))

    def render(row):
        return "  ".join(str(value).ljust(widths[index]) for index, value in enumerate(row))

    return "\n".join(
        [render(headers), render(["-" * width for width in widths]), *[render(row) for row in rows]]
    )


def load_usage(path):
    divisions = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            row["tokens"] = int(row["tokens"])
            row["seats"] = int(row["seats"])
            row["active users"] = int(row["active users"])
            divisions[(row["account"], row["division"])].append(row)

    for records in divisions.values():
        records.sort(key=lambda record: record["month"])
    return divisions


def load_price(path):
    with path.open(newline="", encoding="utf-8") as source:
        row = next(csv.DictReader(source))
    return float(row["price_per_million_tokens"])


def load_targets(path):
    with path.open(newline="", encoding="utf-8") as source:
        return {
            row["account"]: float(row["next_quarter_revenue_target"])
            for row in csv.DictReader(source)
        }


def load_cases(path):
    cases = []
    with path.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            row["volume"] = int(row["volume"])
            row["impact per case"] = float(row["impact per case"])
            row["improvement factor"] = float(row["improvement factor"])
            row["expected added monthly tokens"] = int(row["expected added monthly tokens"])
            row["next quarter ramp percentage"] = float(row["next quarter ramp percentage"])
            cases.append(row)
    return cases


def load_prospects(path):
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def score_prospect(prospect, case_by_name):
    lookalike = case_by_name[prospect["lookalike case"]]
    fit_score = 3 if lookalike["status"] == "proven" else 2
    article = "an" if lookalike["status"] == "agreed" else "a"
    fit_reason = f"'{prospect['lookalike case']}' is {article} {lookalike['status']} case"

    trigger = prospect["trigger"].lower()
    if any(term in trigger for term in ("published", "regulatory", "board-mandated", "deadline")):
        trigger_score = 3
        trigger_reason = f"'{prospect['trigger']}' is a public target or hard deadline"
    elif any(term in trigger for term in ("new chief", "new head", "acquisition")):
        trigger_score = 2
        trigger_reason = f"'{prospect['trigger']}' is a leadership or integration change"
    else:
        trigger_score = 1
        trigger_reason = f"'{prospect['trigger']}' is an internal review without a hard deadline"

    route = prospect["route in"].lower()
    if "executive moved" in route or "former colleague" in route:
        route_score = 3
        route_reason = f"'{prospect['route in']}' is a direct executive or former-colleague path"
    elif "shared" in route or "board adviser" in route:
        route_score = 2
        route_reason = f"'{prospect['route in']}' is a credible shared relationship"
    else:
        route_score = 1
        route_reason = f"'{prospect['route in']}' is an introduction without a close relationship"

    total = fit_score + trigger_score + route_score
    reason = (
        f"Fit {fit_score}: {fit_reason}; Trigger {trigger_score}: {trigger_reason}; "
        f"Route {route_score}: {route_reason}."
    )
    return fit_score, trigger_score, route_score, total, reason


def analyze(records, current_window_start):
    token_values = [record["tokens"] for record in records]
    seat_values = [record["seats"] for record in records]

    recent_tokens = token_values[-3:]
    recent_seats = seat_values[-3:]
    new = records[0]["month"] >= current_window_start
    decline = len(recent_tokens) == 3 and recent_tokens[2] < recent_tokens[1] < recent_tokens[0]
    growth = any(
        recent_tokens[index] > recent_tokens[index - 1] * 1.30
        or recent_seats[index] > recent_seats[index - 1]
        for index in range(1, len(recent_tokens))
    )

    if new:
        signal = "new"
    elif decline:
        signal = "decline"
    elif growth:
        signal = "growth"
    else:
        signal = "stable"

    if new:
        trend = "new"
    else:
        change = token_values[-1] / token_values[0] - 1
        trend = "growing" if change > 0.05 else "declining" if change < -0.05 else "flat"

    return trend, signal


def explain_difference(trend, signal):
    matching_signal = {
        "growing": "growth",
        "declining": "decline",
        "flat": "stable",
        "new": "new",
    }[trend]
    if signal == matching_signal:
        return ""

    explanations = {
        ("growing", "stable"): "Growth has levelled off in the last three months.",
        ("growing", "decline"): "Long-term growth reversed in the last three months.",
        ("declining", "stable"): "Decline has levelled off in the last three months.",
        ("declining", "growth"): "Recent growth follows a 12-month decline.",
        ("flat", "growth"): "Recent growth follows a flat 12-month trend.",
        ("flat", "decline"): "Recent decline follows a flat 12-month trend.",
    }
    return explanations.get((trend, signal), "The recent signal differs from the 12-month trend.")


def forecast_next_quarter(monthly_tokens):
    values = monthly_tokens[-6:]
    count = len(values)
    x_mean = (count - 1) / 2
    y_mean = sum(values) / count
    denominator = sum((index - x_mean) ** 2 for index in range(count))
    slope = sum(
        (index - x_mean) * (value - y_mean)
        for index, value in enumerate(values)
    ) / denominator
    middle = sum(
        max(0, y_mean + slope * ((count + offset) - x_mean))
        for offset in range(3)
    )
    return middle * 0.90, middle, middle * 1.10


def evidence_low_forecast(monthly_tokens):
    latest = monthly_tokens[-1]
    twelve_month_change = latest / monthly_tokens[0] - 1
    if twelve_month_change >= -0.05:
        return latest * 3

    recent = monthly_tokens[-3:]
    recent_rates = [recent[index] / recent[index - 1] - 1 for index in range(1, 3)]
    decline_rate = min(0, sum(recent_rates) / len(recent_rates))
    return sum(latest * (1 + decline_rate) ** step for step in range(1, 4))


def money(value):
    sign = "-" if value < 0 else ""
    return f"{sign}${abs(value):,.0f}"


def customer_value_label(case):
    if case.get("money counts"):
        return case["money counts"]
    labels = {
        "Dispatch exception triage": "outage-coordination effort avoided",
        "Predictive work-order briefs": "unplanned-maintenance impact avoided",
        "Permit evidence assistant": "permit-review delay avoided",
        "Credit memo assembly": "analyst preparation effort avoided",
        "Scenario pack automation": "portfolio-risk review effort avoided",
        "Batch record review": "release-review effort avoided",
        "Deviation investigation drafts": "deviation-closure delay avoided",
        "Shift handover synthesis": "production downtime avoided",
        "Supplier disruption planning": "emergency expedite cost avoided",
        "Demand plan scenario briefs": "demand-planning delay avoided",
        "Shipment exception resolution": "shipment-delay impact avoided",
        "Supplier audit evidence review": "supplier-audit rework avoided",
    }
    return labels[case["use case"]]


def case_volume_label(case):
    return "shift handovers" if case["use case"] == "Shift handover synthesis" else "cases"


def case_forecast_role(case):
    complete_ownership = bool(case["sponsor"] and case["owner"])
    if case["status"] == "proven":
        return "protects low"
    if case["account"] in RECOVERY_ACCOUNTS:
        return "excluded during recovery"
    if case["status"] == "agreed" and complete_ownership:
        return "middle"
    return "high only"


def evaluate_division_pipeline(account, division, ramp, account_cases, latest_record):
    reasons = []
    if account in RECOVERY_ACCOUNTS:
        reasons.append("account is in recovery")
    if latest_record["active users"] <= latest_record["seats"] / 2:
        reasons.append(
            f"active users are not above half of seats "
            f"({latest_record['active users']:,} active users and {latest_record['seats']:,} seats)"
        )

    fitting_cases = [case for case in account_cases if case["division"] == division]
    case = fitting_cases[0] if fitting_cases else None
    if case is None:
        reasons.append("no case fits the division's own work")
    else:
        role = case_forecast_role(case)
        if role in {"protects low", "middle", "high only"}:
            reasons.append(f"{case['use case']} is already counted as {role}")

    eligible = not reasons
    tokens = (
        case["expected added monthly tokens"] * 3 * ramp
        if eligible
        else 0
    )
    return {
        "eligible": eligible,
        "case": case,
        "tokens": tokens,
        "reason": "; ".join(reasons) if reasons else "eligible",
    }


def main():
    divisions = load_usage(BASE_DIR / "usage.csv")
    price_per_million = load_price(BASE_DIR / "prices.csv")
    targets = load_targets(BASE_DIR / "targets.csv")
    cases = load_cases(BASE_DIR / "cases.csv")
    prospects = load_prospects(BASE_DIR / "prospects.csv")
    months = sorted({record["month"] for records in divisions.values() for record in records})
    book_start = months[0]
    book_end = months[-1]
    current_window_start = months[-3]

    summary_rows = []
    tokens_by_account = Counter()
    latest_active_users = Counter()
    latest_stage_counts = Counter()
    monthly_tokens_by_account = defaultdict(Counter)

    for (account, division), records in sorted(divisions.items()):
        trend, signal = analyze(records, current_window_start)
        latest = records[-1]
        note = explain_difference(trend, signal)
        summary_rows.append((account, division, latest["stage"], trend, signal, note))
        tokens_by_account[account] += sum(record["tokens"] for record in records)
        latest_active_users[account] += latest["active users"]
        latest_stage_counts[latest["stage"]] += 1
        for record in records:
            monthly_tokens_by_account[account][record["month"]] += record["tokens"]

    print("DIVISION SUMMARY")
    print(
        format_table(
            ("Account", "Division", "Stage", "Trend over 12 months", "Signal in last 3 months", "Note"),
            summary_rows,
        )
    )
    print(
        "Trend over 12 months compares the first and latest token levels; "
        "Signal in last 3 months describes the most recent token and seat movement."
    )

    print(f"\nBOOK NUMBERS ({book_start} to {book_end})")
    print(f"Total tokens: {sum(tokens_by_account.values()):,}")

    print("\nTokens by account")
    print(format_table(("Account", "Tokens"), [(account, f"{tokens:,}") for account, tokens in sorted(tokens_by_account.items())]))

    print(f"\nActive users by account ({book_end})")
    print(format_table(("Account", "Active users"), [(account, f"{users:,}") for account, users in sorted(latest_active_users.items())]))

    print(f"\nDivisions by stage ({book_end})")
    stage_order = ("consideration", "pilot", "rollout", "production")
    print(format_table(("Stage", "Divisions"), [(stage, latest_stage_counts[stage]) for stage in stage_order]))

    cases_by_account = defaultdict(list)
    case_by_name = {case["use case"]: case for case in cases}
    value_case_rows = []
    for case in cases:
        forecast_role = case_forecast_role(case)
        missing = []
        if not case["sponsor"]:
            missing.append("sponsor")
        if not case["owner"]:
            missing.append("owner")
        risk = f"forecast risk: no {' or '.join(missing)} yet identified" if missing else ""
        value = case["volume"] * case["impact per case"] * case["improvement factor"]
        yearly_usage_cost = (
            case["expected added monthly tokens"] * 12 / 1_000_000 * price_per_million
        )
        customer_return = value / yearly_usage_cost
        value_label = customer_value_label(case)
        volume_label = case_volume_label(case)
        working = (
            f"{case['volume']:,} {volume_label}/year × {money(case['impact per case'])}/"
            f"{'shift handover' if volume_label == 'shift handovers' else 'case'} × "
            f"{case['improvement factor']:.0%}/year = {money(value)}/year of {value_label}"
        )
        return_working = (
            f"{money(value)}/year of {value_label} ÷ "
            f"({case['expected added monthly tokens']:,} tokens/month × 12 months/year ÷ "
            f"1,000,000 tokens × {money(price_per_million)}/million tokens) = "
            f"{customer_return:.2f}× return"
        )
        case["forecast role"] = forecast_role
        case["risk"] = risk
        case["effective added quarterly tokens"] = (
            case["expected added monthly tokens"] * 3 * case["next quarter ramp percentage"]
        )
        cases_by_account[case["account"]].append(case)
        value_case_rows.append(
            (
                case["account"],
                case["division"],
                case["use case"],
                case["status"],
                working,
                return_working,
                case["plain measure"],
                f"{case['expected added monthly tokens']:,}",
                f"{case['next quarter ramp percentage']:.0%} estimate",
                forecast_role,
                risk,
            )
        )

    print("\nVALUE CASES")
    print("Statuses: proposed means suggested; agreed means customer-accepted; proven means measured.")
    print(
        format_table(
            (
                "Account",
                "Division",
                "Use case",
                "Status",
                "Money value working (what money counts)",
                "Customer return",
                "Separate plain measure (not source of money)",
                "Added monthly tokens",
                "Next-quarter ramp",
                "Forecast role",
                "Risk",
            ),
            value_case_rows,
        )
    )

    for prospect in prospects:
        fit, trigger, route, total, reason = score_prospect(prospect, case_by_name)
        prospect["fit score"] = fit
        prospect["trigger score"] = trigger
        prospect["route score"] = route
        prospect["total score"] = total
        prospect["score reason"] = reason
    ranked_prospects = sorted(
        prospects,
        key=lambda prospect: (
            -prospect["total score"],
            -prospect["trigger score"],
            -prospect["route score"],
            -prospect["fit score"],
            prospect["prospect"],
        ),
    )
    top_prospects = ranked_prospects[:3]
    prospect_rows = [
        (
            prospect["prospect"],
            prospect["industry"],
            prospect["size"],
            prospect["lookalike case"],
            prospect["fit score"],
            prospect["trigger score"],
            prospect["route score"],
            f"{prospect['total score']}/9",
            prospect["score reason"],
        )
        for prospect in ranked_prospects
    ]

    print("\nPROSPECT SCORES")
    print("Every prospect, trigger, and route below is invented; nothing was researched.")
    print("Tie-break rule: trigger score first, then route score, then fit score, then prospect name.")
    print(
        format_table(
            ("Prospect", "Industry", "Size", "Lookalike case", "Fit", "Trigger", "Route", "Score", "Reason"),
            prospect_rows,
        )
    )
    print("\nTOP THREE")
    for index, prospect in enumerate(top_prospects, start=1):
        print(f"{index}. {prospect['prospect']} — {prospect['total score']}/9")
    print("\nWhy these three")
    why_selected = {
        "Qelvoryn Forgeworks": "Qelvoryn ranks first because a published downtime target matches a proven shift-handover case and an executive moved across from Talvexon.",
        "Zynthara Biosystems": "Zynthara ranks second because its nine-month distribution compliance deadline is urgent and a shared logistics partner can open the Chief Supply Chain Officer route.",
        "Virelqua Process Labs": "Virelqua wins the seven-point tie on trigger first, then route.",
    }
    for prospect in top_prospects:
        print(why_selected[prospect["prospect"]])
    best_left_out = ranked_prospects[3]
    print(
        f"Best prospect left out: {best_left_out['prospect']} scored {best_left_out['total score']}/9 but its "
        f"{best_left_out['route score']}-point route lost the tie-break to Virelqua's stronger shared-partner route."
    )

    division_pipeline = {
        "Azrulon Energy Networks": ("Customer Systems", 0.20),
        "Norevix Capital Group": ("Markets Operations", 0.15),
        "Quorvane Therapeutics": ("Procurement", 0.20),
        "Talvexon Industrial Systems": ("Field Engineering", 0.20),
        "Veyrith Biologics": ("Supplier Quality", 0.20),
    }
    pipeline_evaluations = {}
    for account, (division, ramp) in division_pipeline.items():
        latest_record = divisions[(account, division)][-1]
        pipeline_evaluations[account] = evaluate_division_pipeline(
            account,
            division,
            ramp,
            cases_by_account[account],
            latest_record,
        )

    forecast_rows = []
    for account in sorted(monthly_tokens_by_account):
        monthly_tokens = [monthly_tokens_by_account[account][month] for month in months]
        low_tokens = evidence_low_forecast(monthly_tokens)
        middle_case_tokens = sum(
            case["effective added quarterly tokens"]
            for case in cases_by_account[account]
            if case["forecast role"] == "middle"
        )
        high_only_tokens = sum(
            case["effective added quarterly tokens"]
            for case in cases_by_account[account]
            if case["forecast role"] == "high only"
        )
        token_forecasts = (
            low_tokens,
            low_tokens + middle_case_tokens,
            low_tokens + middle_case_tokens + high_only_tokens + pipeline_evaluations[account]["tokens"],
        )
        revenue_forecasts = [tokens / 1_000_000 * price_per_million for tokens in token_forecasts]
        straight_line_revenue = forecast_next_quarter(monthly_tokens)[1] / 1_000_000 * price_per_million
        target = targets[account]
        gaps = [forecast - target for forecast in revenue_forecasts]
        middle_gap_ratio = gaps[1] / target
        position = "close" if abs(middle_gap_ratio) <= 0.02 else "ahead" if middle_gap_ratio > 0 else "behind"
        forecast_rows.append(
            (
                account,
                money(target),
                f"{money(revenue_forecasts[0])} estimate",
                money(gaps[0]),
                f"{money(revenue_forecasts[1])} estimate",
                money(gaps[1]),
                f"{money(revenue_forecasts[2])} estimate",
                money(gaps[2]),
                f"{money(straight_line_revenue)} estimate",
                position,
            )
        )

    print("\nNEXT-QUARTER CONSUMPTION REVENUE FORECAST")
    print(
        f"Invented price: {money(price_per_million)} per million tokens. "
        "This is not any vendor's real price. Revenue targets are also invented."
    )
    print(
        format_table(
            (
                "Account",
                "Target",
                "Low forecast",
                "Low gap",
                "Middle forecast",
                "Middle gap",
                "High forecast",
                "High gap",
                "Straight-line comparison",
                "Position",
            ),
            forecast_rows,
        )
    )
    print(
        "Method: low continues the current run rate and carries forward a recent decline; middle adds quarterly "
        "ramped tokens only from agreed cases with a sponsor and owner; proven cases protect low without adding "
        "tokens; high adds ramped proposed and ownership-incomplete cases plus eligible existing-account division "
        "pipeline. Division pipeline is eligible only when active users are above half of seats, a case fits the "
        "division's own work, and that case is not already counted. Prospecting-stage prospects remain outside the "
        "next-quarter forecast."
    )
    print("An account in recovery counts no proposed case and no pipeline.")
    print(
        "Division pipeline counts in high only when active users are above half of seats, a case fits the "
        "division's own work, and that case is not already counted."
    )

    print("\nFORECAST EVIDENCE BY ACCOUNT")
    for account in sorted(cases_by_account):
        low_cases = [case["use case"] for case in cases_by_account[account] if case["forecast role"] == "protects low"]
        middle_cases = [
            f"{case['use case']} ({case['next quarter ramp percentage']:.0%} ramp estimate; "
            f"+{case['effective added quarterly tokens']:,.0f} tokens estimate)"
            for case in cases_by_account[account]
            if case["forecast role"] == "middle"
        ]
        high_cases = [
            f"{case['use case']} ({case['next quarter ramp percentage']:.0%} ramp estimate; "
            f"+{case['effective added quarterly tokens']:,.0f} tokens estimate"
            f"{'; ' + case['risk'] if case['risk'] else ''})"
            for case in cases_by_account[account]
            if case["forecast role"] == "high only"
        ]
        recovery_exclusions = [
            case["use case"]
            for case in cases_by_account[account]
            if case["forecast role"] == "excluded during recovery"
        ]
        print(
            f"{account}: Protects low — {', '.join(low_cases) if low_cases else 'none'}; "
            f"Middle additions — {', '.join(middle_cases) if middle_cases else 'none'}; "
            f"High only — {', '.join(high_cases) if high_cases else 'none'}; "
            f"Excluded during recovery — {', '.join(recovery_exclusions) if recovery_exclusions else 'none'}"
        )

    pipeline_rows = []
    prospect_pipeline_total = 0
    for prospect in top_prospects:
        lookalike = case_by_name[prospect["lookalike case"]]
        first_quarter_tokens = lookalike["expected added monthly tokens"] * 3 * 0.20
        first_quarter_revenue = first_quarter_tokens / 1_000_000 * price_per_million
        prospect_pipeline_total += first_quarter_revenue
        working = (
            f"{lookalike['expected added monthly tokens']:,.0f} tokens/month × 3 months × "
            f"20% ramp estimate × {money(price_per_million)}/M = {money(first_quarter_revenue)} estimate"
        )
        pipeline_rows.append(
            (
                prospect["prospect"],
                "prospect",
                "prospecting",
                "First quarter after signature; timing unknown",
                working,
                f"Top-three prospect linked to {prospect['lookalike case']}.",
                "not in next-quarter forecast",
            )
        )
    next_quarter_pipeline_total = 0
    for account, (division, ramp) in division_pipeline.items():
        stage = next(
            records[-1]["stage"]
            for (division_account, division_name), records in divisions.items()
            if division_account == account and division_name == division
        )
        evaluation = pipeline_evaluations[account]
        revenue = evaluation["tokens"] / 1_000_000 * price_per_million
        next_quarter_pipeline_total += revenue
        if evaluation["eligible"]:
            monthly_tokens = evaluation["case"]["expected added monthly tokens"]
            working = (
                f"{monthly_tokens:,.0f} tokens/month × 3 months × {ramp:.0%} ramp estimate × "
                f"{money(price_per_million)}/M = {money(revenue)} estimate"
            )
            forecast_use = "high only"
        else:
            working = "$0 estimate for the forecast quarter"
            forecast_use = "ineligible"
        pipeline_rows.append(
            (
                account,
                division,
                stage,
                "Nov 2026–Jan 2027 forecast quarter",
                working,
                evaluation["reason"],
                forecast_use,
            )
        )

    print("\nPIPELINE VIEW")
    print("Pipeline counts only in the high forecast and never in the middle forecast.")
    print(
        format_table(
            ("Company or account", "Prospect or division", "Stage", "Quarter", "Revenue estimate and working", "Eligibility reason", "Forecast use"),
            pipeline_rows,
        )
    )
    print(
        f"Next-quarter high-only pipeline total: {money(next_quarter_pipeline_total)} estimate; prospecting-stage "
        "prospects contribute $0 to next quarter."
    )
    print(
        f"First-quarter-after-signature prospect potential: {money(prospect_pipeline_total)} estimate; timing is unknown."
    )
    print("Every prospect, trigger, and route is invented; nothing was researched.")

    backtest_rows = []
    absolute_errors = []
    for account in sorted(monthly_tokens_by_account):
        monthly_tokens = [monthly_tokens_by_account[account][month] for month in months]
        _, forecast_tokens, _ = forecast_next_quarter(monthly_tokens[:9])
        actual_tokens = sum(monthly_tokens[9:12])
        error_percent = (forecast_tokens - actual_tokens) / actual_tokens * 100
        absolute_errors.append(abs(error_percent))
        backtest_rows.append(
            (
                account,
                f"{forecast_tokens:,.0f} estimate",
                f"{actual_tokens:,}",
                f"{error_percent:+.1f}%",
            )
        )

    print("\nBACK-TEST: FORECAST MONTHS 10 TO 12 FROM MONTHS 1 TO 9")
    print(format_table(("Account", "Middle forecast tokens", "Actual tokens", "Error"), backtest_rows))
    print(
        f"The back-test missed an account's quarter by as much as {max(absolute_errors):.1f}%, "
        "so use this method as a planning range rather than a precise commitment."
    )
    print(
        "All five errors are under-forecasts; the largest is Azrulon Energy Networks, where a new division appeared "
        "that a trend line could not foresee."
    )


if __name__ == "__main__":
    main()
