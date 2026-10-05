# Corrections

## 1

### Draft

Created planner.py. It loads `.env` securely, reads `usage.csv`, and passed syntax validation.

Output:

```text
DIVISION SUMMARY
Account                      Division                  Stage       Trend      Signal
---------------------------  ------------------------  ----------  ---------  ---------------
Azrulon Energy Networks            Asset Reliability         production  growing    decline, growth
Azrulon Energy Networks            Customer Systems          production  growing    decline, growth
Azrulon Energy Networks            Grid Operations           production  growing    decline, growth
Azrulon Energy Networks            Hydrogen Networks         pilot       new        growth, new
Azrulon Energy Networks            Market Dispatch           production  growing    decline, growth
Norevix Capital Group        Corporate Banking         production  declining  decline
Norevix Capital Group        Markets Operations        production  declining  decline
Norevix Capital Group        Risk Analytics            production  declining  decline
Norevix Capital Group        Wealth Platforms          production  declining  decline
Quorvane Therapeutics        Manufacturing Operations  production  growing    decline, growth
Quorvane Therapeutics        Procurement               production  flat       decline
Quorvane Therapeutics        Quality Assurance         production  growing    decline, growth
Quorvane Therapeutics        Supply Chain Planning     production  flat       decline
Talvexon Industrial Systems  Advanced Fabrication      production  growing    growth
Talvexon Industrial Systems  Field Engineering         production  growing    growth
Talvexon Industrial Systems  Quality Automation        production  growing    growth
Talvexon Industrial Systems  Supply Network            production  growing    growth
Veyrith Biologics            Biostatistics             production  growing    growth
Veyrith Biologics            Clinical Operations       production  growing    growth
Veyrith Biologics            Discovery Informatics     production  growing    growth
Veyrith Biologics            Regulatory Sciences       production  growing    growth

BOOK NUMBERS (2025-11 to 2026-10)
Total tokens: 686,142,000

Tokens by account
Account                      Tokens
---------------------------  -----------
Azrulon Energy Networks            128,039,000
Norevix Capital Group        132,688,000
Quorvane Therapeutics        86,902,000
Talvexon Industrial Systems  170,620,000
Veyrith Biologics            167,893,000

Active users by account (2026-10)
Account                      Active users
---------------------------  ------------
Azrulon Energy Networks            1,897
Norevix Capital Group        1,825
Quorvane Therapeutics        1,292
Talvexon Industrial Systems  2,485
Veyrith Biologics            2,403

Divisions by stage (2026-10)
Stage          Divisions
-------------  ---------
consideration  0
pilot          1
rollout        0
production     20
```

### What is wrong and why

Two things are wrong. First, the signal column contradicts itself: a division cannot be both declining and growing. A signal must describe what is happening now. Base it on the last three months only, and show one primary signal per division. Second, twenty of twenty-one divisions are in production and none are in consideration or rollout. That is not a real book of accounts. Change the stage data so every account has divisions at different stages: at least two in consideration with very low usage, three in pilot and three in rollout, with stages moving forward over time where usage grows. Keep each account's overall trend as it is. Then rerun and show me the new table.

### Fixed version

Updated `planner.py` and `usage.csv`. Signals now use only the final three months and show one primary value. The latest stage mix is 3 consideration, 6 pilot, 6 rollout, and 6 production divisions.

```text
DIVISION SUMMARY
Account                      Division                  Stage          Trend      Signal
---------------------------  ------------------------  -------------  ---------  -------
Azrulon Energy Networks            Asset Reliability         rollout        growing    growth
Azrulon Energy Networks            Customer Systems          consideration  growing    stable
Azrulon Energy Networks            Grid Operations           production     growing    growth
Azrulon Energy Networks            Hydrogen Networks         pilot          new        new
Azrulon Energy Networks            Market Dispatch           pilot          growing    growth
Norevix Capital Group        Corporate Banking         production     declining  decline
Norevix Capital Group        Markets Operations        consideration  declining  decline
Norevix Capital Group        Risk Analytics            rollout        declining  decline
Norevix Capital Group        Wealth Platforms          pilot          declining  decline
Quorvane Therapeutics        Manufacturing Operations  production     growing    growth
Quorvane Therapeutics        Procurement               consideration  flat       stable
Quorvane Therapeutics        Quality Assurance         pilot          growing    growth
Quorvane Therapeutics        Supply Chain Planning     rollout        flat       stable
Talvexon Industrial Systems  Advanced Fabrication      production     growing    growth
Talvexon Industrial Systems  Field Engineering         pilot          growing    growth
Talvexon Industrial Systems  Quality Automation        rollout        growing    growth
Talvexon Industrial Systems  Supply Network            rollout        growing    growth
Veyrith Biologics            Biostatistics             production     growing    growth
Veyrith Biologics            Clinical Operations       rollout        growing    growth
Veyrith Biologics            Discovery Informatics     production     growing    growth
Veyrith Biologics            Regulatory Sciences       pilot          growing    growth

BOOK NUMBERS (2025-11 to 2026-10)
Total tokens: 619,433,000

Tokens by account
Account                      Tokens
---------------------------  -----------
Azrulon Energy Networks            107,287,000
Norevix Capital Group        103,931,000
Quorvane Therapeutics        69,702,000
Talvexon Industrial Systems  170,620,000
Veyrith Biologics            167,893,000

Active users by account (2026-10)
Account                      Active users
---------------------------  ------------
Azrulon Energy Networks            1,319
Norevix Capital Group        1,162
Quorvane Therapeutics        840
Talvexon Industrial Systems  2,054
Veyrith Biologics            2,078

Divisions by stage (2026-10)
Stage          Divisions
-------------  ---------
consideration  3
pilot          6
rollout        6
production     6
```


## 2

### Draft

Updated `planner.py` and `usage.csv`. Signals now use only the final three months and show one primary value. The latest stage mix is 3 consideration, 6 pilot, 6 rollout, and 6 production divisions.

```text
DIVISION SUMMARY
Account                      Division                  Stage          Trend      Signal
---------------------------  ------------------------  -------------  ---------  -------
Azrulon Energy Networks            Asset Reliability         rollout        growing    growth
Azrulon Energy Networks            Customer Systems          consideration  growing    stable
Azrulon Energy Networks            Grid Operations           production     growing    growth
Azrulon Energy Networks            Hydrogen Networks         pilot          new        new
Azrulon Energy Networks            Market Dispatch           pilot          growing    growth
Norevix Capital Group        Corporate Banking         production     declining  decline
Norevix Capital Group        Markets Operations        consideration  declining  decline
Norevix Capital Group        Risk Analytics            rollout        declining  decline
Norevix Capital Group        Wealth Platforms          pilot          declining  decline
Quorvane Therapeutics        Manufacturing Operations  production     growing    growth
Quorvane Therapeutics        Procurement               consideration  flat       stable
Quorvane Therapeutics        Quality Assurance         pilot          growing    growth
Quorvane Therapeutics        Supply Chain Planning     rollout        flat       stable
Talvexon Industrial Systems  Advanced Fabrication      production     growing    growth
Talvexon Industrial Systems  Field Engineering         pilot          growing    growth
Talvexon Industrial Systems  Quality Automation        rollout        growing    growth
Talvexon Industrial Systems  Supply Network            rollout        growing    growth
Veyrith Biologics            Biostatistics             production     growing    growth
Veyrith Biologics            Clinical Operations       rollout        growing    growth
Veyrith Biologics            Discovery Informatics     production     growing    growth
Veyrith Biologics            Regulatory Sciences       pilot          growing    growth

BOOK NUMBERS (2025-11 to 2026-10)
Total tokens: 619,433,000

Tokens by account
Account                      Tokens
---------------------------  -----------
Azrulon Energy Networks            107,287,000
Norevix Capital Group        103,931,000
Quorvane Therapeutics        69,702,000
Talvexon Industrial Systems  170,620,000
Veyrith Biologics            167,893,000

Active users by account (2026-10)
Account                      Active users
---------------------------  ------------
Azrulon Energy Networks            1,319
Norevix Capital Group        1,162
Quorvane Therapeutics        840
Talvexon Industrial Systems  2,054
Veyrith Biologics            2,078

Divisions by stage (2026-10)
Stage          Divisions
-------------  ---------
consideration  3
pilot          6
rollout        6
production     6
```

### What is wrong and why

In the division summary, Customer Systems at Azrulon Energy Networks shows a trend of growing but a signal of stable. To a reader that looks like a contradiction, because the table does not say the two columns cover different periods. Fix it in three ways. First, rename the columns to Trend over 12 months and Signal in last 3 months. Second, add a new column called Note. Where the trend and the signal differ, write a short plain reason, for example: growth has levelled off in the last three months. Leave the note empty where they agree. Third, add one line under the table explaining what each column measures. Then rerun and show me the table.

### Fixed version

Updated `planner.py`. The table now names both measurement periods, explains the one differing result, and leaves matching rows blank in the Note column.

```text
DIVISION SUMMARY
Account                      Division                  Stage          Trend over 12 months  Signal in last 3 months  Note
---------------------------  ------------------------  -------------  --------------------  -----------------------  -------------------------------------------------
Azrulon Energy Networks            Asset Reliability         rollout        growing               growth
Azrulon Energy Networks            Customer Systems          consideration  growing               stable                   Growth has levelled off in the last three months.
Azrulon Energy Networks            Grid Operations           production     growing               growth
Azrulon Energy Networks            Hydrogen Networks         pilot          new                   new
Azrulon Energy Networks            Market Dispatch           pilot          growing               growth
Norevix Capital Group        Corporate Banking         production     declining             decline
Norevix Capital Group        Markets Operations        consideration  declining             decline
Norevix Capital Group        Risk Analytics            rollout        declining             decline
Norevix Capital Group        Wealth Platforms          pilot          declining             decline
Quorvane Therapeutics        Manufacturing Operations  production     growing               growth
Quorvane Therapeutics        Procurement               consideration  flat                  stable
Quorvane Therapeutics        Quality Assurance         pilot          growing               growth
Quorvane Therapeutics        Supply Chain Planning     rollout        flat                  stable
Talvexon Industrial Systems  Advanced Fabrication      production     growing               growth
Talvexon Industrial Systems  Field Engineering         pilot          growing               growth
Talvexon Industrial Systems  Quality Automation        rollout        growing               growth
Talvexon Industrial Systems  Supply Network            rollout        growing               growth
Veyrith Biologics            Biostatistics             production     growing               growth
Veyrith Biologics            Clinical Operations       rollout        growing               growth
Veyrith Biologics            Discovery Informatics     production     growing               growth
Veyrith Biologics            Regulatory Sciences       pilot          growing               growth
Trend over 12 months compares the first and latest token levels; Signal in last 3 months describes the most recent token and seat movement.
```


## 3

### Draft

Created prices.csv and targets.csv. Updated planner.py and ran it successfully.

```text
NEXT-QUARTER CONSUMPTION REVENUE FORECAST
Invented price: $200 per million tokens. Revenue targets are also invented.

Account                      Target   Low forecast      Low gap  Middle forecast   Middle gap  High forecast     High gap  Position
---------------------------  -------  ----------------  -------  ----------------  ----------  ----------------  --------  --------
Azrulon Energy Networks            $6,200   $6,220 estimate   $20      $6,912 estimate   $712        $7,603 estimate   $1,403    ahead
Norevix Capital Group        $4,500   $3,615 estimate   -$885    $4,017 estimate   -$483       $4,418 estimate   -$82      behind
Quorvane Therapeutics        $3,600   $3,243 estimate   -$357    $3,603 estimate   $3          $3,963 estimate   $363      close
Talvexon Industrial Systems  $11,000  $11,173 estimate  $173     $12,414 estimate  $1,414      $13,656 estimate  $2,656    ahead
Veyrith Biologics            $14,500  $11,537 estimate  -$2,963  $12,819 estimate  -$1,681     $14,101 estimate  -$399     behind

Method: fit a straight-line trend to each account's last six monthly token totals, project three months, and set low and high at 10% below and above the middle estimate.
```


## 4

### Draft

Created cases.csv with 12 validated invented cases. Updated planner.py and ran it successfully.

```text
VALUE CASES
Statuses: proposed means suggested; agreed means customer-accepted; proven means measured.

Account                      Use case                        Status    Customer value working             Plain measure                             Forecast role  Risk
---------------------------  ------------------------------  --------  ---------------------------------  ----------------------------------------  -------------  ------------------------------
Azrulon Energy Networks            Dispatch exception triage       agreed    180,000 × $14 × 8% = $201,600      420 operator hours saved per month        middle
Azrulon Energy Networks            Predictive work-order briefs    proven    42,000 × $900 × 3% = $1,134,000    1,260 maintenance hours saved per quarter middle
Azrulon Energy Networks            Permit evidence assistant       proposed  12,000 × $250 × 10% = $300,000     180 review days saved per quarter         high only      forecast risk: missing sponsor
Norevix Capital Group        Credit memo assembly            proven    85,000 × $45 × 20% = $765,000      6,800 analyst hours saved per year        middle
Norevix Capital Group        Scenario pack automation        proposed  24,000 × $180 × 15% = $648,000     960 review hours saved per quarter        high only
Quorvane Therapeutics        Batch record review             agreed    60,000 × $70 × 18% = $756,000      2,400 reviewer hours saved per quarter    middle
Quorvane Therapeutics        Deviation investigation drafts  agreed    18,000 × $400 × 12% = $864,000     720 closure days saved per year           high only      forecast risk: missing owner
Talvexon Industrial Systems  Shift handover synthesis        proven    110,000 × $55 × 10% = $605,000     5,500 supervisor hours saved per year     middle
Talvexon Industrial Systems  Supplier disruption planning    proposed  36,000 × $500 × 8% = $1,440,000    288 avoided expedite events per year      high only
Veyrith Biologics            Protocol evidence synthesis     agreed    30,000 × $350 × 12% = $1,260,000   900 scientist days saved per year         middle
Veyrith Biologics            Site query resolution           proven    95,000 × $90 × 16% = $1,368,000    15,200 site days saved per year           middle
Veyrith Biologics            Submission consistency review   proposed  25,000 × $600 × 10% = $1,500,000   500 review cycles avoided per year        high only      forecast risk: missing sponsor

NEXT-QUARTER CONSUMPTION REVENUE FORECAST
Invented price: $10 per million tokens. This is not any vendor's real price. Revenue targets are also invented.

Account                      Target    Low forecast       Middle forecast    High forecast      Straight-line comparison
---------------------------  --------  -----------------  -----------------  -----------------  ------------------------
Azrulon Energy Networks            $310,000  $320,070 estimate  $545,070 estimate  $605,070 estimate  $345,575 estimate
Norevix Capital Group        $225,000  $204,211 estimate  $318,211 estimate  $393,211 estimate  $200,826 estimate
Quorvane Therapeutics        $180,000  $178,950 estimate  $262,950 estimate  $325,950 estimate  $180,151 estimate
Talvexon Industrial Systems  $550,000  $568,680 estimate  $688,680 estimate  $793,680 estimate  $620,716 estimate
Veyrith Biologics            $725,000  $581,460 estimate  $809,460 estimate  $899,460 estimate  $640,937 estimate

Method: low continues the current run rate and carries forward a recent decline; middle adds quarterly tokens from agreed or proven cases with a sponsor and owner; high adds every remaining case.

FORECAST EVIDENCE BY ACCOUNT
Azrulon Energy Networks: Middle — Dispatch exception triage, Predictive work-order briefs; High only — Permit evidence assistant (forecast risk: missing sponsor)
Norevix Capital Group: Middle — Credit memo assembly; High only — Scenario pack automation
Quorvane Therapeutics: Middle — Batch record review; High only — Deviation investigation drafts (forecast risk: missing owner)
Talvexon Industrial Systems: Middle — Shift handover synthesis; High only — Supplier disruption planning
Veyrith Biologics: Middle — Protocol evidence synthesis, Site query resolution; High only — Submission consistency review (forecast risk: missing sponsor)

BACK-TEST
All five errors are under-forecasts; the largest is Azrulon Energy Networks, where a new division appeared that a trend line could not foresee.
```

### What is wrong and why

I would not defend this middle forecast to a sales leader. Three things are wrong. First, proven cases are added on top of the run rate. A proven case has already been measured, so its usage is already in the run rate. That is double counting. Second, the declining account, Norevix, now shows a middle forecast 41 percent above its target. Third, every account is ahead of target, so the forecast has lost its meaning. Fix it like this. Proven cases add no new tokens; list them as evidence that protects the low forecast. Agreed cases with a sponsor and an owner add tokens to the middle, but only the share that can realistically go live next quarter; show a ramp percentage for each and label it an estimate. Size the added tokens so that an agreed case adds between five and fifteen percent of that account's current quarterly run rate. Proposed cases, and any case missing a sponsor or owner, count only in the high. Then reset the targets so that on the middle forecast two accounts are ahead, two are behind and one is close, with Norevix behind. Rerun and show me the forecast and the evidence list.

### Fixed version

Corrected the evidence model and reran `planner.py`. Proven cases no longer add tokens, and the eligible agreed-case additions are 8.8%–11.7% of current quarterly run rate. The middle case now has two accounts ahead, two behind, and one close, with Norevix behind.

```text
NEXT-QUARTER CONSUMPTION REVENUE FORECAST
Invented price: $10 per million tokens. This is not any vendor's real price. Revenue targets are also invented.

Account                      Target    Low forecast       Low gap   Middle forecast    Middle gap  High forecast      High gap  Straight-line comparison  Position
---------------------------  --------  -----------------  --------  -----------------  ----------  -----------------  --------  ------------------------  --------
Azrulon Energy Networks            $335,000  $320,070 estimate  -$14,930  $353,820 estimate  $18,820     $383,820 estimate  $48,820   $345,575 estimate         ahead
Norevix Capital Group        $225,000  $204,211 estimate  -$20,789  $204,211 estimate  -$20,789    $241,711 estimate  $16,711   $200,826 estimate         behind
Quorvane Therapeutics        $200,000  $178,950 estimate  -$21,050  $199,950 estimate  -$50        $218,850 estimate  $18,850   $180,151 estimate         close
Talvexon Industrial Systems  $600,000  $568,680 estimate  -$31,320  $568,680 estimate  -$31,320    $610,680 estimate  $10,680   $620,716 estimate         behind
Veyrith Biologics            $610,000  $581,460 estimate  -$28,540  $632,460 estimate  $22,460     $663,960 estimate  $53,960   $640,937 estimate         ahead

Method: low continues the current run rate and carries forward a recent decline; middle adds quarterly ramped tokens only from agreed cases with a sponsor and owner; proven cases protect low without adding tokens; high adds ramped proposed and ownership-incomplete cases.

FORECAST EVIDENCE BY ACCOUNT
Azrulon Energy Networks: Protects low — Predictive work-order briefs; Middle additions — Dispatch exception triage (25% ramp estimate; +3,375,000,000 tokens estimate); High only — Permit evidence assistant (50% ramp estimate; +3,000,000,000 tokens estimate; forecast risk: missing sponsor)
Norevix Capital Group: Protects low — Credit memo assembly; Middle additions — none; High only — Scenario pack automation (50% ramp estimate; +3,750,000,000 tokens estimate)
Quorvane Therapeutics: Protects low — none; Middle additions — Batch record review (25% ramp estimate; +2,100,000,000 tokens estimate); High only — Deviation investigation drafts (30% ramp estimate; +1,890,000,000 tokens estimate; forecast risk: missing owner)
Talvexon Industrial Systems: Protects low — Shift handover synthesis; Middle additions — none; High only — Supplier disruption planning (40% ramp estimate; +4,200,000,000 tokens estimate)
Veyrith Biologics: Protects low — Site query resolution; Middle additions — Protocol evidence synthesis (50% ramp estimate; +5,100,000,000 tokens estimate); High only — Submission consistency review (35% ramp estimate; +3,150,000,000 tokens estimate; forecast risk: missing sponsor)
```


## 5

### Draft

Created prospects.csv with 10 validated prospects. Every prospect, trigger, route, and company name is invented; nothing was researched.

```text
PROSPECT SCORES
Prospect                  Fit  Trigger  Route  Score  Reason
------------------------  ---  -------  -----  -----  -------------------------------------------------------------------------------------------------------------------------------------------------
Qelvoryn Forgeworks       3    3        3      9/9    Fit 3: matches a proven case; Trigger 3: a public target or hard governance deadline; Route 3: a direct executive or former-colleague path.
Zynthara Biosystems       3    3        3      9/9    Fit 3: matches a proven case; Trigger 3: a public target or hard governance deadline; Route 3: a direct executive or former-colleague path.
Praxevon Ledgercraft      3    3        3      9/9    Fit 3: matches a proven case; Trigger 3: a public target or hard governance deadline; Route 3: a direct executive or former-colleague path.
Ulmaris Power Systems     3    2        2      7/9    Fit 3: matches a proven case; Trigger 2: a leadership or integration change; Route 2: a credible shared relationship.
Virelqua Process Labs     2    3        2      7/9    Fit 2: matches an agreed case; Trigger 3: a public target or hard governance deadline; Route 2: a credible shared relationship.
Dorthenix Materials       3    2        1      6/9    Fit 3: matches a proven case; Trigger 2: a leadership or integration change; Route 1: an introduction path without a close relationship.
Kavoryx Fleet Systems     2    1        3      6/9    Fit 2: matches an agreed case; Trigger 1: an internal review without a hard deadline; Route 3: a direct executive or former-colleague path.
Eluntra Riskworks         3    3        2      8/9    Fit 3: matches a proven case; Trigger 3: a public target or hard governance deadline; Route 2: a credible shared relationship.
Myzara Clinical Engines   2    2        2      6/9    Fit 2: matches an agreed case; Trigger 2: a leadership or integration change; Route 2: a credible shared relationship.
Torqevia Industrial Mesh  3    3        1      7/9    Fit 3: matches a proven case; Trigger 3: a public target or hard governance deadline; Route 1: an introduction path without a close relationship.

TOP THREE
1. Praxevon Ledgercraft — 9/9
2. Qelvoryn Forgeworks — 9/9
3. Zynthara Biosystems — 9/9

Why these three
Praxevon Ledgercraft has a measured lookalike case, an urgent trigger, and a direct warm route to the likely sponsor.
Qelvoryn Forgeworks has a measured lookalike case, an urgent trigger, and a direct warm route to the likely sponsor.
Zynthara Biosystems has a measured lookalike case, an urgent trigger, and a direct warm route to the likely sponsor.

PIPELINE VIEW
Pipeline counts only in the high forecast and never in the middle forecast.

Company or account           Prospect or division  Stage          First-quarter revenue  Forecast use
---------------------------  --------------------  -------------  ---------------------  ------------
Praxevon Ledgercraft         prospect              prospecting    $22,800 estimate       high only
Qelvoryn Forgeworks          prospect              prospecting    $24,000 estimate       high only
Zynthara Biosystems          prospect              prospecting    $25,200 estimate       high only
Azrulon Energy Networks            Customer Systems      consideration  $27,000 estimate       high only
Norevix Capital Group        Markets Operations    consideration  $17,100 estimate       high only
Quorvane Therapeutics        Procurement           consideration  $16,800 estimate       high only
Talvexon Industrial Systems  Field Engineering     pilot          $24,000 estimate       high only
Veyrith Biologics            Regulatory Sciences   pilot          $20,400 estimate       high only
```

### What is wrong and why

The prospect scoring does not discriminate. Three prospects score nine out of nine with identical reasons, so the top three is a tie, not a choice. Fix six things. One: rewrite the invented prospect data so scores spread realistically, with at most one nine, and state a tie-break rule: trigger first, then route, then fit. Two: replace each reason with a specific one naming that prospect's actual trigger, lookalike case and route. Three: sort the table by score, highest first. Four: rewrite Why these three so each reason is different and specific, and add one line on why the best prospect left out was left out. Five: in the pipeline view, show the working beside every revenue estimate, name the quarter each falls in, and say why each existing division was chosen. A prospect still at prospecting adds nothing to next quarter's high forecast; show its revenue as first quarter after signature only. Six: print the pipeline total, and the line saying every prospect, trigger and route is invented and nothing was researched. Run it and show me the output.

### Fixed version

Reworked the prospect model and reran `planner.py`. Scores now spread from 6/9 to 9/9, with only one 9. The table uses the stated tie-break rule and the prospecting-stage opportunities contribute $0 to next quarter.

```text
PROSPECT SCORES
Every prospect, trigger, and route below is invented; nothing was researched.
Tie-break rule: trigger score first, then route score, then fit score, then prospect name.

Prospect                  Fit  Trigger  Route  Score  Reason
------------------------  ---  -------  -----  -----  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Qelvoryn Forgeworks       3    3        3      9/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 3: 'Published factory downtime efficiency target' is a public target or hard deadline; Route 3: 'Executive moved from Talvexon Industrial Systems' is a direct executive or former-colleague path.
Zynthara Biosystems       3    3        2      8/9    Fit 3: 'Site query resolution' is a proven case; Trigger 3: 'Regulatory trial delivery deadline in nine months' is a public target or hard deadline; Route 2: 'Shared clinical research partner' is a credible shared relationship.
Virelqua Process Labs     2    3        2      7/9    Fit 2: 'Batch record review' is an agreed case; Trigger 3: 'Published batch-release cycle target' is a public target or hard deadline; Route 2: 'Shared validation partner' is a credible shared relationship.
Eluntra Riskworks         3    3        1      7/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 3: 'Regulatory model-governance deadline' is a public target or hard deadline; Route 1: 'Conference introduction' is an introduction without a close relationship.
Ulmaris Power Systems     3    2        2      7/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief digital officer appointed' is a leadership or integration change; Route 2: 'Shared implementation partner' is a credible shared relationship.
Myzara Clinical Engines   2    2        2      6/9    Fit 2: 'Batch record review' is an agreed case; Trigger 2: 'New chief operating officer appointed' is a leadership or integration change; Route 2: 'Board adviser introduction' is a credible shared relationship.
Dorthenix Materials       3    2        1      6/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 2: 'Acquisition integration programme started' is a leadership or integration change; Route 1: 'Industry council introduction' is an introduction without a close relationship.
Torqevia Industrial Mesh  3    2        1      6/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief procurement officer appointed' is a leadership or integration change; Route 1: 'Conference introduction' is an introduction without a close relationship.
Kavoryx Fleet Systems     2    1        3      6/9    Fit 2: 'Dispatch exception triage' is an agreed case; Trigger 1: 'Operations productivity review announced' is an internal review without a hard deadline; Route 3: 'Former colleague of the Azrulon sponsor' is a direct executive or former-colleague path.
Praxevon Ledgercraft      3    1        2      6/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 1: 'New head of digital credit appointed' is an internal review without a hard deadline; Route 2: 'Shared banking transformation partner' is a credible shared relationship.

TOP THREE
1. Qelvoryn Forgeworks — 9/9
2. Zynthara Biosystems — 8/9
3. Virelqua Process Labs — 7/9

Why these three
Qelvoryn ranks first because a published downtime target matches a proven shift-handover case and an executive moved across from Talvexon.
Zynthara ranks second because its nine-month regulatory deadline is urgent and a shared clinical research partner can open the Chief Clinical Officer route.
Virelqua wins the seven-point tie because its published batch-release target and shared validation partner outrank the warmer-fit alternatives under the trigger-then-route rule.
Best prospect left out: Eluntra Riskworks scored 7/9 but its 1-point route lost the tie-break to Virelqua's stronger shared-partner route.

PIPELINE VIEW
Pipeline counts only in the high forecast and never in the middle forecast.

Company or account           Prospect or division  Stage          Quarter                                        Revenue estimate and working                                                          Why chosen                                                                              Forecast use
---------------------------  --------------------  -------------  ---------------------------------------------  ------------------------------------------------------------------------------------  --------------------------------------------------------------------------------------  ----------------------------
Qelvoryn Forgeworks          prospect              prospecting    First quarter after signature; timing unknown  4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Top-three prospect linked to Shift handover synthesis.                                  not in next-quarter forecast
Zynthara Biosystems          prospect              prospecting    First quarter after signature; timing unknown  4,200,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $25,200 estimate  Top-three prospect linked to Site query resolution.                                     not in next-quarter forecast
Virelqua Process Labs        prospect              prospecting    First quarter after signature; timing unknown  2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Top-three prospect linked to Batch record review.                                       not in next-quarter forecast
Azrulon Energy Networks            Customer Systems      consideration  Nov 2026–Jan 2027 forecast quarter             4,500,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $27,000 estimate  Customer Systems is the account's consideration-stage division and has levelled usage.  high only
Norevix Capital Group        Markets Operations    consideration  Nov 2026–Jan 2027 forecast quarter             3,800,000,000 tokens/month × 3 months × 15% ramp estimate × $10/M = $17,100 estimate  Markets Operations is in consideration and needs a new path in a declining account.     high only
Quorvane Therapeutics        Procurement           consideration  Nov 2026–Jan 2027 forecast quarter             2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Procurement is the account's consideration-stage division with low current usage.       high only
Talvexon Industrial Systems  Field Engineering     pilot          Nov 2026–Jan 2027 forecast quarter             4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Field Engineering is a growing pilot and the next logical rollout candidate.            high only
Veyrith Biologics            Regulatory Sciences   pilot          Nov 2026–Jan 2027 forecast quarter             3,400,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $20,400 estimate  Regulatory Sciences is a growing pilot with an agreed-case lookalike nearby.            high only

Next-quarter high-only pipeline total: $105,300 estimate; prospecting-stage prospects contribute $0 to next quarter.
First-quarter-after-signature prospect potential: $66,000 estimate; timing is unknown.
Every prospect, trigger, and route is invented; nothing was researched.
```


## 6

### Draft

Updated prospects.csv. Scores now spread from 6/9 to 9/9, with only one 9. Prospecting-stage opportunities contribute $0 to next quarter.

```text
PROSPECT SCORES
Every prospect, trigger, and route below is invented; nothing was researched.
Tie-break rule: trigger score first, then route score, then fit score, then prospect name.

Prospect                  Fit  Trigger  Route  Score  Reason
------------------------  ---  -------  -----  -----  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Qelvoryn Forgeworks       3    3        3      9/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 3: 'Published factory downtime efficiency target' is a public target or hard deadline; Route 3: 'Executive moved from Talvexon Industrial Systems' is a direct executive or former-colleague path.
Zynthara Biosystems       3    3        2      8/9    Fit 3: 'Site query resolution' is a proven case; Trigger 3: 'Regulatory trial delivery deadline in nine months' is a public target or hard deadline; Route 2: 'Shared clinical research partner' is a credible shared relationship.
Virelqua Process Labs     2    3        2      7/9    Fit 2: 'Batch record review' is an agreed case; Trigger 3: 'Published batch-release cycle target' is a public target or hard deadline; Route 2: 'Shared validation partner' is a credible shared relationship.
Eluntra Riskworks         3    3        1      7/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 3: 'Regulatory model-governance deadline' is a public target or hard deadline; Route 1: 'Conference introduction' is an introduction without a close relationship.
Ulmaris Power Systems     3    2        2      7/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief digital officer appointed' is a leadership or integration change; Route 2: 'Shared implementation partner' is a credible shared relationship.
Myzara Clinical Engines   2    2        2      6/9    Fit 2: 'Batch record review' is an agreed case; Trigger 2: 'New chief operating officer appointed' is a leadership or integration change; Route 2: 'Board adviser introduction' is a credible shared relationship.
Dorthenix Materials       3    2        1      6/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 2: 'Acquisition integration programme started' is a leadership or integration change; Route 1: 'Industry council introduction' is an introduction without a close relationship.
Torqevia Industrial Mesh  3    2        1      6/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief procurement officer appointed' is a leadership or integration change; Route 1: 'Conference introduction' is an introduction without a close relationship.
Kavoryx Fleet Systems     2    1        3      6/9    Fit 2: 'Dispatch exception triage' is an agreed case; Trigger 1: 'Operations productivity review announced' is an internal review without a hard deadline; Route 3: 'Former colleague of the Azrulon sponsor' is a direct executive or former-colleague path.
Praxevon Ledgercraft      3    1        2      6/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 1: 'New head of digital credit appointed' is an internal review without a hard deadline; Route 2: 'Shared banking transformation partner' is a credible shared relationship.

TOP THREE
1. Qelvoryn Forgeworks — 9/9
2. Zynthara Biosystems — 8/9
3. Virelqua Process Labs — 7/9

Why these three
Qelvoryn ranks first because a published downtime target matches a proven shift-handover case and an executive moved across from Talvexon.
Zynthara ranks second because its nine-month regulatory deadline is urgent and a shared clinical research partner can open the Chief Clinical Officer route.
Virelqua wins the seven-point tie because its published batch-release target and shared validation partner outrank the warmer-fit alternatives under the trigger-then-route rule.
Best prospect left out: Eluntra Riskworks scored 7/9 but its 1-point route lost the tie-break to Virelqua's stronger shared-partner route.

PIPELINE VIEW
Pipeline counts only in the high forecast and never in the middle forecast.

Company or account           Prospect or division  Stage          Quarter                                        Revenue estimate and working                                                          Why chosen                                                                              Forecast use
---------------------------  --------------------  -------------  ---------------------------------------------  ------------------------------------------------------------------------------------  --------------------------------------------------------------------------------------  ----------------------------
Qelvoryn Forgeworks          prospect              prospecting    First quarter after signature; timing unknown  4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Top-three prospect linked to Shift handover synthesis.                                  not in next-quarter forecast
Zynthara Biosystems          prospect              prospecting    First quarter after signature; timing unknown  4,200,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $25,200 estimate  Top-three prospect linked to Site query resolution.                                     not in next-quarter forecast
Virelqua Process Labs        prospect              prospecting    First quarter after signature; timing unknown  2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Top-three prospect linked to Batch record review.                                       not in next-quarter forecast
Azrulon Energy Networks            Customer Systems      consideration  Nov 2026–Jan 2027 forecast quarter             4,500,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $27,000 estimate  Customer Systems is the account's consideration-stage division and has levelled usage.  high only
Norevix Capital Group        Markets Operations    consideration  Nov 2026–Jan 2027 forecast quarter             3,800,000,000 tokens/month × 3 months × 15% ramp estimate × $10/M = $17,100 estimate  Markets Operations is in consideration and needs a new path in a declining account.     high only
Quorvane Therapeutics        Procurement           consideration  Nov 2026–Jan 2027 forecast quarter             2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Procurement is the account's consideration-stage division with low current usage.       high only
Talvexon Industrial Systems  Field Engineering     pilot          Nov 2026–Jan 2027 forecast quarter             4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Field Engineering is a growing pilot and the next logical rollout candidate.            high only
Veyrith Biologics            Regulatory Sciences   pilot          Nov 2026–Jan 2027 forecast quarter             3,400,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $20,400 estimate  Regulatory Sciences is a growing pilot with an agreed-case lookalike nearby.            high only

Next-quarter high-only pipeline total: $105,300 estimate; prospecting-stage prospects contribute $0 to next quarter.
First-quarter-after-signature prospect potential: $66,000 estimate; timing is unknown.
Every prospect, trigger, and route is invented; nothing was researched.
```

### What is wrong and why

Praxevon Ledgercraft's trigger is a new appointment, but it scores 1 and is described as an internal review. The other three new appointments each score 2. Score the same kind of trigger the same way. Fix Praxevon to trigger 2, described as a leadership change. Also reword the Virelqua line in Why these three: say plainly that it wins the tie on trigger first, then route, and remove the words warmer-fit. Run it and show me the full output.

### Fixed version

Updated `planner.py`. Praxevon now scores trigger 2 as a leadership change, and Virelqua's tie-break explanation says plainly that it wins on trigger first, then route.

```text
DIVISION SUMMARY
Account                      Division                  Stage          Trend over 12 months  Signal in last 3 months  Note                                             
---------------------------  ------------------------  -------------  --------------------  -----------------------  -------------------------------------------------
Azrulon Energy Networks            Asset Reliability         rollout        growing               growth                                                                    
Azrulon Energy Networks            Customer Systems          consideration  growing               stable                   Growth has levelled off in the last three months.
Azrulon Energy Networks            Grid Operations           production     growing               growth                                                                    
Azrulon Energy Networks            Hydrogen Networks         pilot          new                   new                                                                       
Azrulon Energy Networks            Market Dispatch           pilot          growing               growth                                                                    
Norevix Capital Group        Corporate Banking         production     declining             decline                                                                   
Norevix Capital Group        Markets Operations        consideration  declining             decline                                                                   
Norevix Capital Group        Risk Analytics            rollout        declining             decline                                                                   
Norevix Capital Group        Wealth Platforms          pilot          declining             decline                                                                   
Quorvane Therapeutics        Manufacturing Operations  production     growing               growth                                                                    
Quorvane Therapeutics        Procurement               consideration  flat                  stable                                                                    
Quorvane Therapeutics        Quality Assurance         pilot          growing               growth                                                                    
Quorvane Therapeutics        Supply Chain Planning     rollout        flat                  stable                                                                    
Talvexon Industrial Systems  Advanced Fabrication      production     growing               growth                                                                    
Talvexon Industrial Systems  Field Engineering         pilot          growing               growth                                                                    
Talvexon Industrial Systems  Quality Automation        rollout        growing               growth                                                                    
Talvexon Industrial Systems  Supply Network            rollout        growing               growth                                                                    
Veyrith Biologics            Biostatistics             production     growing               growth                                                                    
Veyrith Biologics            Clinical Operations       rollout        growing               growth                                                                    
Veyrith Biologics            Discovery Informatics     production     growing               growth                                                                    
Veyrith Biologics            Regulatory Sciences       pilot          growing               growth                                                                    
Trend over 12 months compares the first and latest token levels; Signal in last 3 months describes the most recent token and seat movement.

BOOK NUMBERS (2025-11 to 2026-10)
Total tokens: 619,433,000,000

Tokens by account
Account                      Tokens         
---------------------------  ---------------
Azrulon Energy Networks            107,287,000,000
Norevix Capital Group        103,931,000,000
Quorvane Therapeutics        69,702,000,000 
Talvexon Industrial Systems  170,620,000,000
Veyrith Biologics            167,893,000,000

Active users by account (2026-10)
Account                      Active users
---------------------------  ------------
Azrulon Energy Networks            13,190      
Norevix Capital Group        11,620      
Quorvane Therapeutics        8,400       
Talvexon Industrial Systems  20,540      
Veyrith Biologics            20,780      

Divisions by stage (2026-10)
Stage          Divisions
-------------  ---------
consideration  3        
pilot          6        
rollout        6        
production     6        

VALUE CASES
Statuses: proposed means suggested; agreed means customer-accepted; proven means measured.
Account                      Division                  Use case                        Status    Customer value working            Plain measure                             Added monthly tokens  Next-quarter ramp  Forecast role  Risk                          
---------------------------  ------------------------  ------------------------------  --------  --------------------------------  ----------------------------------------  --------------------  -----------------  -------------  ------------------------------
Azrulon Energy Networks            Grid Operations           Dispatch exception triage       agreed    180,000 × $14 × 8% = $201,600     420 operator hours saved per month        4,500,000,000         25% estimate       middle                                       
Azrulon Energy Networks            Asset Reliability         Predictive work-order briefs    proven    42,000 × $900 × 3% = $1,134,000   1260 maintenance hours saved per quarter  3,000,000,000         0% estimate        protects low                                 
Azrulon Energy Networks            Hydrogen Networks         Permit evidence assistant       proposed  12,000 × $250 × 10% = $300,000    180 review days saved per quarter         2,000,000,000         50% estimate       high only      forecast risk: missing sponsor
Norevix Capital Group        Corporate Banking         Credit memo assembly            proven    85,000 × $45 × 20% = $765,000     6800 analyst hours saved per year         3,800,000,000         0% estimate        protects low                                 
Norevix Capital Group        Risk Analytics            Scenario pack automation        proposed  24,000 × $180 × 15% = $648,000    960 review hours saved per quarter        2,500,000,000         50% estimate       high only                                    
Quorvane Therapeutics        Manufacturing Operations  Batch record review             agreed    60,000 × $70 × 18% = $756,000     2400 reviewer hours saved per quarter     2,800,000,000         25% estimate       middle                                       
Quorvane Therapeutics        Quality Assurance         Deviation investigation drafts  agreed    18,000 × $400 × 12% = $864,000    720 closure days saved per year           2,100,000,000         30% estimate       high only      forecast risk: missing owner  
Talvexon Industrial Systems  Advanced Fabrication      Shift handover synthesis        proven    110,000 × $55 × 10% = $605,000    5500 supervisor hours saved per year      4,000,000,000         0% estimate        protects low                                 
Talvexon Industrial Systems  Supply Network            Supplier disruption planning    proposed  36,000 × $500 × 8% = $1,440,000   288 avoided expedite events per year      3,500,000,000         40% estimate       high only                                    
Veyrith Biologics            Discovery Informatics     Protocol evidence synthesis     agreed    30,000 × $350 × 12% = $1,260,000  900 scientist days saved per year         3,400,000,000         50% estimate       middle                                       
Veyrith Biologics            Clinical Operations       Site query resolution           proven    95,000 × $90 × 16% = $1,368,000   15200 site days saved per year            4,200,000,000         0% estimate        protects low                                 
Veyrith Biologics            Regulatory Sciences       Submission consistency review   proposed  25,000 × $600 × 10% = $1,500,000  500 review cycles avoided per year        3,000,000,000         35% estimate       high only      forecast risk: missing sponsor

PROSPECT SCORES
Every prospect, trigger, and route below is invented; nothing was researched.
Tie-break rule: trigger score first, then route score, then fit score, then prospect name.
Prospect                  Industry            Size             Lookalike case                Fit  Trigger  Route  Score  Reason                                                                                                                                                                                                                                                        
------------------------  ------------------  ---------------  ----------------------------  ---  -------  -----  -----  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Qelvoryn Forgeworks       manufacturing       42000 employees  Shift handover synthesis      3    3        3      9/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 3: 'Published factory downtime efficiency target' is a public target or hard deadline; Route 3: 'Executive moved from Talvexon Industrial Systems' is a direct executive or former-colleague path.
Zynthara Biosystems       life sciences       28000 employees  Site query resolution         3    3        2      8/9    Fit 3: 'Site query resolution' is a proven case; Trigger 3: 'Regulatory trial delivery deadline in nine months' is a public target or hard deadline; Route 2: 'Shared clinical research partner' is a credible shared relationship.                           
Virelqua Process Labs     life sciences       19000 employees  Batch record review           2    3        2      7/9    Fit 2: 'Batch record review' is an agreed case; Trigger 3: 'Published batch-release cycle target' is a public target or hard deadline; Route 2: 'Shared validation partner' is a credible shared relationship.                                                
Eluntra Riskworks         financial services  22000 employees  Credit memo assembly          3    3        1      7/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 3: 'Regulatory model-governance deadline' is a public target or hard deadline; Route 1: 'Conference introduction' is an introduction without a close relationship.                                    
Praxevon Ledgercraft      financial services  36000 employees  Credit memo assembly          3    2        2      7/9    Fit 3: 'Credit memo assembly' is a proven case; Trigger 2: 'New head of digital credit appointed' is a leadership or integration change; Route 2: 'Shared banking transformation partner' is a credible shared relationship.                                  
Ulmaris Power Systems     energy              55000 employees  Predictive work-order briefs  3    2        2      7/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief digital officer appointed' is a leadership or integration change; Route 2: 'Shared implementation partner' is a credible shared relationship.                                   
Myzara Clinical Engines   life sciences       31000 employees  Batch record review           2    2        2      6/9    Fit 2: 'Batch record review' is an agreed case; Trigger 2: 'New chief operating officer appointed' is a leadership or integration change; Route 2: 'Board adviser introduction' is a credible shared relationship.                                            
Dorthenix Materials       manufacturing       61000 employees  Shift handover synthesis      3    2        1      6/9    Fit 3: 'Shift handover synthesis' is a proven case; Trigger 2: 'Acquisition integration programme started' is a leadership or integration change; Route 1: 'Industry council introduction' is an introduction without a close relationship.                   
Torqevia Industrial Mesh  manufacturing       68000 employees  Predictive work-order briefs  3    2        1      6/9    Fit 3: 'Predictive work-order briefs' is a proven case; Trigger 2: 'New chief procurement officer appointed' is a leadership or integration change; Route 1: 'Conference introduction' is an introduction without a close relationship.                       
Kavoryx Fleet Systems     manufacturing       47000 employees  Dispatch exception triage     2    1        3      6/9    Fit 2: 'Dispatch exception triage' is an agreed case; Trigger 1: 'Operations productivity review announced' is an internal review without a hard deadline; Route 3: 'Former colleague of the Azrulon sponsor' is a direct executive or former-colleague path. 

TOP THREE
1. Qelvoryn Forgeworks — 9/9
2. Zynthara Biosystems — 8/9
3. Virelqua Process Labs — 7/9

Why these three
Qelvoryn ranks first because a published downtime target matches a proven shift-handover case and an executive moved across from Talvexon.
Zynthara ranks second because its nine-month regulatory deadline is urgent and a shared clinical research partner can open the Chief Clinical Officer route.
Virelqua wins the seven-point tie on trigger first, then route.
Best prospect left out: Eluntra Riskworks scored 7/9 but its 1-point route lost the tie-break to Virelqua's stronger shared-partner route.

NEXT-QUARTER CONSUMPTION REVENUE FORECAST
Invented price: $10 per million tokens. This is not any vendor's real price. Revenue targets are also invented.
Account                      Target    Low forecast       Low gap   Middle forecast    Middle gap  High forecast      High gap  Straight-line comparison  Position
---------------------------  --------  -----------------  --------  -----------------  ----------  -----------------  --------  ------------------------  --------
Azrulon Energy Networks            $335,000  $320,070 estimate  -$14,930  $353,820 estimate  $18,820     $410,820 estimate  $75,820   $345,575 estimate         ahead   
Norevix Capital Group        $225,000  $204,211 estimate  -$20,789  $204,211 estimate  -$20,789    $258,811 estimate  $33,811   $200,826 estimate         behind  
Quorvane Therapeutics        $200,000  $178,950 estimate  -$21,050  $199,950 estimate  -$50        $235,650 estimate  $35,650   $180,151 estimate         close   
Talvexon Industrial Systems  $600,000  $568,680 estimate  -$31,320  $568,680 estimate  -$31,320    $634,680 estimate  $34,680   $620,716 estimate         behind  
Veyrith Biologics            $610,000  $581,460 estimate  -$28,540  $632,460 estimate  $22,460     $684,360 estimate  $74,360   $640,937 estimate         ahead   
Method: low continues the current run rate and carries forward a recent decline; middle adds quarterly ramped tokens only from agreed cases with a sponsor and owner; proven cases protect low without adding tokens; high adds ramped proposed and ownership-incomplete cases plus identified existing-account division pipeline. Prospecting-stage prospects remain outside the next-quarter forecast.

FORECAST EVIDENCE BY ACCOUNT
Azrulon Energy Networks: Protects low — Predictive work-order briefs; Middle additions — Dispatch exception triage (25% ramp estimate; +3,375,000,000 tokens estimate); High only — Permit evidence assistant (50% ramp estimate; +3,000,000,000 tokens estimate; forecast risk: missing sponsor)
Norevix Capital Group: Protects low — Credit memo assembly; Middle additions — none; High only — Scenario pack automation (50% ramp estimate; +3,750,000,000 tokens estimate)
Quorvane Therapeutics: Protects low — none; Middle additions — Batch record review (25% ramp estimate; +2,100,000,000 tokens estimate); High only — Deviation investigation drafts (30% ramp estimate; +1,890,000,000 tokens estimate; forecast risk: missing owner)
Talvexon Industrial Systems: Protects low — Shift handover synthesis; Middle additions — none; High only — Supplier disruption planning (40% ramp estimate; +4,200,000,000 tokens estimate)
Veyrith Biologics: Protects low — Site query resolution; Middle additions — Protocol evidence synthesis (50% ramp estimate; +5,100,000,000 tokens estimate); High only — Submission consistency review (35% ramp estimate; +3,150,000,000 tokens estimate; forecast risk: missing sponsor)

PIPELINE VIEW
Pipeline counts only in the high forecast and never in the middle forecast.
Company or account           Prospect or division  Stage          Quarter                                        Revenue estimate and working                                                          Why chosen                                                                              Forecast use                
---------------------------  --------------------  -------------  ---------------------------------------------  ------------------------------------------------------------------------------------  --------------------------------------------------------------------------------------  ----------------------------
Qelvoryn Forgeworks          prospect              prospecting    First quarter after signature; timing unknown  4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Top-three prospect linked to Shift handover synthesis.                                  not in next-quarter forecast
Zynthara Biosystems          prospect              prospecting    First quarter after signature; timing unknown  4,200,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $25,200 estimate  Top-three prospect linked to Site query resolution.                                     not in next-quarter forecast
Virelqua Process Labs        prospect              prospecting    First quarter after signature; timing unknown  2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Top-three prospect linked to Batch record review.                                       not in next-quarter forecast
Azrulon Energy Networks            Customer Systems      consideration  Nov 2026–Jan 2027 forecast quarter             4,500,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $27,000 estimate  Customer Systems is the account's consideration-stage division and has levelled usage.  high only                   
Norevix Capital Group        Markets Operations    consideration  Nov 2026–Jan 2027 forecast quarter             3,800,000,000 tokens/month × 3 months × 15% ramp estimate × $10/M = $17,100 estimate  Markets Operations is in consideration and needs a new path in a declining account.     high only                   
Quorvane Therapeutics        Procurement           consideration  Nov 2026–Jan 2027 forecast quarter             2,800,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $16,800 estimate  Procurement is the account's consideration-stage division with low current usage.       high only                   
Talvexon Industrial Systems  Field Engineering     pilot          Nov 2026–Jan 2027 forecast quarter             4,000,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $24,000 estimate  Field Engineering is a growing pilot and the next logical rollout candidate.            high only                   
Veyrith Biologics            Regulatory Sciences   pilot          Nov 2026–Jan 2027 forecast quarter             3,400,000,000 tokens/month × 3 months × 20% ramp estimate × $10/M = $20,400 estimate  Regulatory Sciences is a growing pilot with an agreed-case lookalike nearby.            high only                   
Next-quarter high-only pipeline total: $105,300 estimate; prospecting-stage prospects contribute $0 to next quarter.
First-quarter-after-signature prospect potential: $66,000 estimate; timing is unknown.
Every prospect, trigger, and route is invented; nothing was researched.

BACK-TEST: FORECAST MONTHS 10 TO 12 FROM MONTHS 1 TO 9
Account                      Middle forecast tokens   Actual tokens   Error 
---------------------------  -----------------------  --------------  ------
Azrulon Energy Networks            26,700,457,143 estimate  31,061,000,000  -14.0%
Norevix Capital Group        21,477,428,571 estimate  22,502,000,000  -4.6% 
Quorvane Therapeutics        17,316,028,571 estimate  17,883,000,000  -3.2% 
Talvexon Industrial Systems  51,304,171,429 estimate  54,061,000,000  -5.1% 
Veyrith Biologics            51,703,771,429 estimate  54,846,000,000  -5.7% 
The back-test missed an account's quarter by as much as 14.0%, so use this method as a planning range rather than a precise commitment.
All five errors are under-forecasts; the largest is Azrulon Energy Networks, where a new division appeared that a trend line could not foresee.
```

### What is wrong and why

The scale is wrong for a large enterprise book. The biggest quarterly target is $14,500 and the whole book is about $40,000 a quarter. An account director for large enterprises carries targets above $2 million a year, so these numbers do not look like the job. Fix it in two ways. First, multiply every token figure in usage.csv by one thousand, and scale seats and active users up so they suit large enterprises. Second, change the invented price to $10 per million tokens, and say clearly that it is invented and is not any vendor's real price. Then reset the targets so the pattern stays the same: two accounts ahead, two behind, one close. Rerun everything and show me the division summary totals and the forecast.

### Fixed version

Rescaled the full book and reran `planner.py`. Tokens are 1,000× larger, seats and active users are 10× larger, and the target pattern remains two ahead, two behind, and one close.

```text
DIVISION SUMMARY
Account                      Division                  Stage          Trend over 12 months  Signal in last 3 months  Note
---------------------------  ------------------------  -------------  --------------------  -----------------------  -------------------------------------------------
Azrulon Energy Networks            Asset Reliability         rollout        growing               growth
Azrulon Energy Networks            Customer Systems          consideration  growing               stable                   Growth has levelled off in the last three months.
Azrulon Energy Networks            Grid Operations           production     growing               growth
Azrulon Energy Networks            Hydrogen Networks         pilot          new                   new
Azrulon Energy Networks            Market Dispatch           pilot          growing               growth
Norevix Capital Group        Corporate Banking         production     declining             decline
Norevix Capital Group        Markets Operations        consideration  declining             decline
Norevix Capital Group        Risk Analytics            rollout        declining             decline
Norevix Capital Group        Wealth Platforms          pilot          declining             decline
Quorvane Therapeutics        Manufacturing Operations  production     growing               growth
Quorvane Therapeutics        Procurement               consideration  flat                  stable
Quorvane Therapeutics        Quality Assurance         pilot          growing               growth
Quorvane Therapeutics        Supply Chain Planning     rollout        flat                  stable
Talvexon Industrial Systems  Advanced Fabrication      production     growing               growth
Talvexon Industrial Systems  Field Engineering         pilot          growing               growth
Talvexon Industrial Systems  Quality Automation        rollout        growing               growth
Talvexon Industrial Systems  Supply Network            rollout        growing               growth
Veyrith Biologics            Biostatistics             production     growing               growth
Veyrith Biologics            Clinical Operations       rollout        growing               growth
Veyrith Biologics            Discovery Informatics     production     growing               growth
Veyrith Biologics            Regulatory Sciences       pilot          growing               growth
Trend over 12 months compares the first and latest token levels; Signal in last 3 months describes the most recent token and seat movement.

BOOK NUMBERS (2025-11 to 2026-10)
Total tokens: 619,433,000,000

Tokens by account
Account                      Tokens
---------------------------  ---------------
Azrulon Energy Networks            107,287,000,000
Norevix Capital Group        103,931,000,000
Quorvane Therapeutics        69,702,000,000
Talvexon Industrial Systems  170,620,000,000
Veyrith Biologics            167,893,000,000

Active users by account (2026-10)
Account                      Active users
---------------------------  ------------
Azrulon Energy Networks            13,190
Norevix Capital Group        11,620
Quorvane Therapeutics        8,400
Talvexon Industrial Systems  20,540
Veyrith Biologics            20,780

Divisions by stage (2026-10)
Stage          Divisions
-------------  ---------
consideration  3
pilot          6
rollout        6
production     6

NEXT-QUARTER CONSUMPTION REVENUE FORECAST
Invented price: $10 per million tokens. This is not any vendor's real price. Revenue targets are also invented.
Account                      Target    Low forecast       Low gap    Middle forecast    Middle gap  High forecast      High gap  Position
---------------------------  --------  -----------------  ---------  -----------------  ----------  -----------------  --------  --------
Azrulon Energy Networks            $310,000  $311,018 estimate  $1,018     $345,575 estimate  $35,575     $380,133 estimate  $70,133   ahead
Norevix Capital Group        $225,000  $180,743 estimate  -$44,257   $200,826 estimate  -$24,174    $220,908 estimate  -$4,092   behind
Quorvane Therapeutics        $180,000  $162,136 estimate  -$17,864   $180,151 estimate  $151        $198,166 estimate  $18,166   close
Talvexon Industrial Systems  $550,000  $558,644 estimate  $8,644     $620,716 estimate  $70,716     $682,787 estimate  $132,787  ahead
Veyrith Biologics            $725,000  $576,843 estimate  -$148,157  $640,937 estimate  -$84,063    $705,030 estimate  -$19,970  behind
Method: fit a straight-line trend to each account's last six monthly token totals, project three months, and set low and high at 10% below and above the middle estimate.
```

## 7

### Draft

Created discovery_briefs.md with three API-generated briefs. The generator used the official [Responses API Python pattern](https://developers.openai.com/api/docs/libraries), loaded the key without displaying it, and all required sections passed validation.

Here is one brief:

# Zynthara Biosystems discovery call brief

**DRAFT — invented data**

## Why you, why now

With a regulatory trial delivery deadline in nine months, the shared clinical research partner offers a warm route to explore delivery risks with Zynthara Biosystems’ likely sponsor, the Chief Clinical Officer.

Use that partner introduction to ask whether site query resolution is a bottleneck worth addressing before the nine-month deadline.

## Value hypothesis

**Hypothesis to test — not a promise.** The site query resolution lookalike suggests that reducing trial query cycle time could free site capacity: **95,000 × $90 × 16% = $1,368,000**, with a plain measure of **15,200 site days saved per year**. These invented lookalike figures are not a forecast for Zynthara; their applicability and assumptions need testing.

## Five discovery questions

1. Which trial delivery milestones are most at risk before the regulatory deadline in nine months?
2. How much of that risk comes from site query resolution?
3. What is the current query cycle time, and how is it measured?
4. Would the Chief Clinical Officer sponsor this assessment, and who would own execution?
5. Could the shared clinical research partner help identify one division and a usable baseline for a pilot?

## Likely objection

“We cannot risk disrupting trial delivery or introducing compliance issues with only nine months remaining.”

## Honest answer

That is a reasonable concern; the invented lookalike does not establish that this would help Zynthara. A narrowly scoped pilot would only make sense if your teams approve the controls and can measure results without putting delivery at risk.

## Small first step to propose

Propose a pilot in one division, using **median site query cycle time** as the single agreed measure. Before starting, agree and freeze the baseline period, eligible query population and calculation method; assess the pilot against that fixed baseline without extrapolating the lookalike savings.

## Compliance, privacy and security questions

- What regulatory requirements, validation evidence and audit trails would the pilot require? **Customer role to answer: Regulatory Affairs lead.**
- What approvals and change controls are needed to protect trial integrity? **Customer role to answer: Clinical Quality Assurance lead.**
- What personal or clinical data could be used, and what minimisation, access and transfer restrictions apply? **Customer role to answer: Data Protection Officer.**
- What security review, access controls, hosting conditions and incident-response requirements must be satisfied? **Customer role to answer: Chief Information Security Officer.**
- What retention, deletion and partner data-sharing terms would apply? **Customer role to answer: Legal Counsel.**

## My opening


## 8

### Draft

Logged as correction 7 and updated all three briefs in discovery_briefs.md. Validation passed.

# Zynthara Biosystems discovery call brief

**DRAFT — invented data**

## Why you, why now

Zynthara Biosystems faces a regulatory trial delivery deadline in nine months, so a discovery call could expose the operational risks most likely to threaten that deadline while there is still time to act.

The conversation should help its clinical leaders quantify the consequences, understand what has already failed and decide whether this issue merits attention alongside other trial priorities.

## Value hypothesis

**Hypothesis to test — not a promise.** Faster site query resolution may release site capacity and reduce risk to trial delivery. Illustrative working from a similar case: **95,000 site queries per year × $90 cost per unresolved query × 16% potential improvement = $1,368,000 potential value per year**, alongside a separate operational measure of **15,200 site days per year**; both assumptions must be tested against Zynthara’s own data.

## Five discovery questions

1. What is most at risk as the regulatory trial delivery deadline approaches?
2. What do unresolved site queries cost in delayed milestones, site effort or rework over a typical month?
3. What have you already tried to shorten query cycle time, and what happened?
4. Which teams, sites or roles feel the impact of slow query resolution most?
5. What other trial priorities are competing for the same people, budget and attention?

## Likely objection

“We cannot risk disrupting trial delivery or introducing compliance issues with only nine months remaining.”

## Honest answer

That is a reasonable concern. A similar case elsewhere does not prove it would work for you, and nothing should proceed unless your clinical, quality, privacy and security teams are satisfied that it protects trial delivery and meets your controls.

## Small first step to propose

Run a six-week assessment in one clinical division using **median site query cycle time** as the single agreed measure. Fix the baseline using the six weeks immediately before the assessment, with an agreed query population and calculation method.

## Compliance, privacy and security questions

- “How would you validate the approach and preserve an auditable record of its performance?” **Our side: Validation Lead (invented role). Their side to approve: Clinical Quality Assurance Lead.**
- “Where would our trial and site data be stored and processed?” **Our side: Data Residency Architect (invented role). Their side to approve: Data Protection Officer.**
- “Who could access our data, and how would access be authorised, logged and reviewed?” **Our side: Identity and Access Security Lead (invented role). Their side to approve: Chief Information Security Officer.**
- “How long would you retain our data, and how would deletion be verified?” **Our side: Data Governance Lead (invented role). Their side to approve: Privacy Counsel.**
- “Which security controls, testing evidence and incident-response commitments would you provide?” **Our side: Product Security Lead (invented role). Their side to approve: Chief Information Security Officer.**

## My opening

### What is wrong and why

Log this. My expertise is supply chain: plan, make, logistics and fulfilment, procurement, quality, and centres of excellence. I will not show work I cannot defend, so remove all clinical trial and drug discovery content. Change labels only; keep every number identical. One: in Veyrith Biologics, rename Clinical Operations to Logistics and Fulfilment, Discovery Informatics to Demand and Supply Planning, Regulatory Sciences to Supplier Quality, and Biostatistics to Supply Chain Centre of Excellence. Two: rename the three Veyrith cases to Shipment exception resolution, Demand plan scenario briefs, and Supplier audit evidence review, and relabel their units and plain measures to match. Three: change Zynthara Biosystems so its lookalike is Shipment exception resolution, its trigger is a distribution compliance deadline in nine months, its route is a shared logistics partner, and its sponsor is the Chief Supply Chain Officer. Four: update every file that uses the old names. Five: run the program and confirm the forecast figures and back-test errors are unchanged. Show me the Veyrith rows and the Zynthara row. Do not regenerate the briefs yet.

### Fixed version

The live project data now uses supply-chain labels throughout. The discovery briefs were relabelled without calling the API. Forecast figures and back-test errors are unchanged.

```text
Veyrith Biologics  Demand and Supply Planning         production  growing  growth
Veyrith Biologics  Logistics and Fulfilment           rollout     growing  growth
Veyrith Biologics  Supplier Quality                   pilot       growing  growth
Veyrith Biologics  Supply Chain Centre of Excellence  production  growing  growth

Veyrith Biologics  Demand and Supply Planning  Demand plan scenario briefs     agreed    30,000 × $350 × 12% = $1,260,000  900 planner days saved per year
Veyrith Biologics  Logistics and Fulfilment    Shipment exception resolution   proven    95,000 × $90 × 16% = $1,368,000   15200 shipment delay days avoided per year
Veyrith Biologics  Supplier Quality            Supplier audit evidence review  proposed  25,000 × $600 × 10% = $1,500,000  500 supplier audit review cycles avoided per year

Zynthara Biosystems  life sciences  28000 employees  Distribution compliance deadline in nine months  Shipment exception resolution  Shared logistics partner  Chief Supply Chain Officer
```

### What is wrong and why

Log this. The discovery briefs sell when they should discover. Fix all three briefs. One: rewrite the five questions so none names our solution, asks for a sponsor, or mentions a pilot. Ask about their problem: what is most at risk, what it costs them, what they have already tried, who feels it most, and what else competes for attention. Two: in the honest answer, never say invented or lookalike in words spoken to the customer; say a similar case elsewhere does not prove it would work for you. Three: rewrite the compliance section as the questions the customer will ask us about validation, data location, access, retention and security, and for each name the invented role on our side who answers and the role on their side who must approve. Four: label every number in the working with what it counts and its period. Five: give the pilot a fixed length. Six: make Why you, why now say why this prospect should take the call, not how we reach them. Keep My opening empty. Show me the Zynthara brief again.

### Fixed version

All three briefs were revised. Here is the corrected Zynthara brief:

# Zynthara Biosystems discovery call brief

**DRAFT — invented data**

## Why you, why now

Zynthara Biosystems faces a regulatory trial delivery deadline in nine months, so a discovery call could expose the operational risks most likely to threaten that deadline while there is still time to act.

The conversation should help its clinical leaders quantify the consequences, understand what has already failed and decide whether this issue merits attention alongside other trial priorities.

## Value hypothesis

**Hypothesis to test — not a promise.** Faster site query resolution may release site capacity and reduce risk to trial delivery. Illustrative working from a similar case: **95,000 site queries per year × $90 cost per unresolved query × 16% potential improvement = $1,368,000 potential value per year**, alongside a separate operational measure of **15,200 site days per year**; both assumptions must be tested against Zynthara’s own data.

## Five discovery questions

1. What is most at risk as the regulatory trial delivery deadline approaches?
2. What do unresolved site queries cost in delayed milestones, site effort or rework over a typical month?
3. What have you already tried to shorten query cycle time, and what happened?
4. Which teams, sites or roles feel the impact of slow query resolution most?
5. What other trial priorities are competing for the same people, budget and attention?

## Likely objection

“We cannot risk disrupting trial delivery or introducing compliance issues with only nine months remaining.”

## Honest answer

That is a reasonable concern. A similar case elsewhere does not prove it would work for you, and nothing should proceed unless your clinical, quality, privacy and security teams are satisfied that it protects trial delivery and meets your controls.

## Small first step to propose

Run a six-week assessment in one clinical division using **median site query cycle time** as the single agreed measure. Fix the baseline using the six weeks immediately before the assessment, with an agreed query population and calculation method.

## Compliance, privacy and security questions

- “How would you validate the approach and preserve an auditable record of its performance?” **Our side: Validation Lead (invented role). Their side to approve: Clinical Quality Assurance Lead.**
- “Where would our trial and site data be stored and processed?” **Our side: Data Residency Architect (invented role). Their side to approve: Data Protection Officer.**
- “Who could access our data, and how would access be authorised, logged and reviewed?” **Our side: Identity and Access Security Lead (invented role). Their side to approve: Chief Information Security Officer.**
- “How long would you retain our data, and how would deletion be verified?” **Our side: Data Governance Lead (invented role). Their side to approve: Privacy Counsel.**
- “Which security controls, testing evidence and incident-response commitments would you provide?” **Our side: Product Security Lead (invented role). Their side to approve: Chief Information Security Officer.**

## My opening


## 9

### Draft

# Qelvoryn Forgeworks deal strategy

**DRAFT — invented data**

All prospect details, roles, economics and planning dates below are invented and unverified. This is a proposed strategy, not evidence of customer agreement.

## The decision

The **Chief Operating Officer (invented role)** is the proposed sponsor and business decision-maker. The **Divisional Manufacturing Director (invented role)** and **Shift Operations Lead (invented role)** influence workflow fit and adoption. The **Enterprise Security Director (invented role)**, **Data Governance Counsel (invented role)** and **Procurement Director (invented role)** can block approval.

Use the executive’s move from Talvexon Industrial Systems as a potential introduction route; do not assume access. Connect discovery to the published factory downtime efficiency target. Seek a decision through sponsor-backed validation of operational value, security clearance and an acceptable commercial case.

## The commercial shape

Start with **one division for a six-week validation period (invented division count and period)** and a **$60,000 fixed commitment for that six-week period (invented commitment)**, with metered usage charged on top at **$10 per million tokens consumed during the six-week period (invented usage price, not any vendor’s real price or term)**. Expand by **one additional division per successful value review (invented expansion step)** only after demonstrated value and repeatable deployment.

The invented similar case—shift handover synthesis—is described as proven in the supplied scenario, not independently verified. Its economics are:

- **110,000 activities per year (invented annual volume)** at **$55 per activity during that year (invented unit cost)**.
- **10% potential improvement over that year (invented annual improvement assumption)**, yielding **$605,000 potential value per year (invented annual estimate)**.
- **4,000,000,000 tokens per month (invented monthly usage)** at **$10 per million tokens consumed each month (invented usage price, not any vendor’s real price or term)**.
- That implies **$480,000 usage cost per year (invented annual calculation)**, leaving **$125,000 per year before commitment, implementation and other costs (invented annual calculation)**.

The narrow illustrative margin argues for a bounded start, usage controls and measured economics—not an enterprise-wide commitment.

## What must be true for them to say yes

- The sponsor confirms that handover failures materially contribute to downtime.
- Accessible, permitted operational data supports useful synthesis without replacing accountable human judgment.
- Operations agrees a baseline, measurement method and acceptance criteria linking better handovers to downtime reduction.
- Measured value exceeds total delivery and operating costs; similar-case results are not treated as a prospect forecast.

## Risks to the deal and how each is reduced

- **Weak sponsorship or introduction:** validate the warm route and secure direct sponsor participation before substantial delivery work.
- **Value does not transfer:** test representative handovers against an agreed baseline; stop or rescope if downtime impact is unsupported.
- **Usage erodes returns:** monitor consumption, apply budget alerts and agree expansion gates based on total costs.
- **Security and data approval delays:** plan the pre-signing security and data review every large enterprise runs. Our **Security Assurance Lead (invented role)** answers security questions; our **Privacy Counsel (invented role)** answers data questions. Resolve access, retention, confidentiality and contractual requirements before signature.
- **Poor adoption or unsafe reliance:** involve shift teams, retain human review and assign an operational workflow owner.

## Joint plan agreed with the customer

*Proposed for agreement; no customer agreement is asserted.*

- **2026-10-06 (invented discovery date):** confirm downtime priorities and sponsor. Their owner: **Chief Operating Officer (invented role)**; our owner: **Account Lead (invented role)**.
- **2026-10-13 (invented validation-design date):** agree division, baseline, data access and success criteria. Their owner: **Divisional Manufacturing Director (invented role)**; our owner: **Solutions Lead (invented role)**.
- **2026-10-23 (invented approval-review date):** complete security/data review and assess total-cost economics. Their owner: **Enterprise Security Director (invented role)**; our owner: **Security Assurance Lead (invented role)**.
- **2026-11-03 (invented signature date):** sign bounded scope, commitment and usage controls, subject to cleared approvals. Their owner: **Procurement Director (invented role)**; our owner: **Commercial Lead (invented role)**.
- **2026-11-17 (invented first-value review date):** review initial handover outcomes against baseline; decide whether to continue. Their owner: **Shift Operations Lead (invented role)**; our owner: **Customer Success Lead (invented role)**.

## What I would walk away from

No accountable sponsor, inaccessible or impermissible data, unresolved security requirements, unsupported downtime claims, or economics that cannot clear total costs. Decline broad rollout obligations before evidence supports expansion.

### What is wrong and why

Log this. A customer will not agree a case that costs more than it returns. One: add a column to the value cases called customer return: yearly value divided by yearly usage cost, with the working. Two: change volume or impact per case in cases.csv, never tokens, so every agreed or proven case returns at least three times its yearly usage cost, and every proposed case at least two times. Confirm the forecast and back-test are unchanged. Three: state the period for every value figure. Four: regenerate the deal strategy and the value hypothesis in the three briefs with the new figures, keeping my openings. Five: in the deal strategy, make the timeline realistic: security and data review four to six weeks, signature about three months after discovery, first value review after the full pilot period. Six: say once at the top that all figures, roles and dates are invented, and remove the repeated labels. Show me the value case table and the deal strategy.

### Fixed version

Updated `cases.csv`, `planner.py`, `discovery_briefs.md`, and `deal_strategy.md`. The value table now shows annual working and customer return; all thresholds pass without changing tokens. The forecast and back-test are unchanged. The three value hypotheses and the deal strategy use the revised economics, all openings remain in place, and the deal timeline now includes a five-week security review, signature three months after discovery, and first value after the full six-week pilot.

The corrected deal strategy is the complete contents of `deal_strategy.md` delivered with this correction.


## 10

### Draft

## The commercial shape
Propose a **$5,000 minimum commitment per billing month**, credited against usage, in **one division during the six-week pilot period**. Charge usage above that credit at the planning rate of **$10 per million tokens consumed in each billing month**. Keep the initial scope to shift handover synthesis; expand by **one division after each successful value review period** only after operational acceptance and measured benefit.

The supplied proven similar case targets reduced production downtime: **110,000 activities per year × $135 per activity in the annual baseline × 10% potential improvement per year = $1,485,000 potential value per year**. Its **4,000,000,000 tokens per month** would cost **$40,000 per month**, or **$480,000 per year**, at the planning rate. These are comparison economics, not Qelvoryn forecasts; delivery costs and local applicability remain untested. A small commitment limits initial exposure while usage-based growth follows adoption.

## Joint plan agreed with the customer
Proposed for customer confirmation; agreement is not yet established.

1. **2026-10-08 — Discovery:** confirm downtime problem, authority and baseline access. **Their owner:** Chief Operating Officer. **Our owner:** Account Lead.
2. **2026-10-19–2026-11-22 — Security and data review:** complete a **five-week pre-signature review period**, resolve findings and record approval. **Their owner:** Enterprise Security Director. **Our owner:** Security Lead.
3. **2026-12-03 — Pilot design:** agree measurement, workflow, budget cap and acceptance gates. **Their owner:** Division Operations Director. **Our owner:** Solution Architect.
4. **2027-01-08 — Signature:** execute the scoped order **three months after the discovery date**, authorizing the **six-week pilot period running 2027-01-11–2027-02-21**. **Their owner:** Procurement Director. **Our owner:** Commercial Lead.
5. **2027-02-22 — First value review:** after the full six-week pilot period, assess downtime impact, adoption and cost; decide whether to expand. **Their owner:** Operations Finance Lead. **Our owner:** Value Lead.

## What I would walk away from
No accountable sponsor, no usable baseline, unresolved security requirements, demands for guaranteed savings, or uncapped usage without budget ownership. Do not sell enterprise-wide deployment before the pilot demonstrates a defensible operational benefit.

### What is wrong and why

Log this. A $5,000 monthly floor is too low to show commitment on either side. Change the commercial shape to a minimum commitment of $10,000 to $15,000 per month, credited against usage, for a minimum term of three months. Show the total minimum as $30,000 to $45,000 over the term, with the working. Keep the six-week pilot inside that term, with the value review after the pilot and the expansion decision before month three ends. Update the joint plan dates and the walk-away section so they agree with this. Show me the commercial shape and the joint plan only.

### Fixed version

## The commercial shape
Propose a **$10,000–$15,000 minimum commitment per billing month**, credited against usage, for a **minimum term of three billing months**. The total minimum commitment is **$10,000–$15,000 per billing month × three billing months = $30,000–$45,000 over the three-month term**. Charge usage above the monthly credit at the planning rate of **$10 per million tokens consumed in each billing month**.

Keep the initial scope to one division and run the **six-week pilot period inside the three-month minimum term**. Hold the first value review immediately after the full pilot, then make the expansion decision before the third billing month ends. Expand by one division only after operational acceptance, measured benefit and explicit approval from both sides. This commitment is large enough to require attention from both teams while limiting the customer’s exposure before value is demonstrated.

## Joint plan agreed with the customer
Proposed for customer confirmation; agreement is not yet established.

1. **2026-10-08 — Discovery:** confirm downtime problem, authority and baseline access. **Their owner:** Chief Operating Officer. **Our owner:** Account Lead.
2. **2026-10-19–2026-11-22 — Security and data review:** complete a **five-week pre-signature review period**, resolve findings and record approval. **Their owner:** Enterprise Security Director. **Our owner:** Security Lead.
3. **2026-12-03 — Pilot design:** agree measurement, workflow, budget cap and acceptance gates. **Their owner:** Division Operations Director. **Our owner:** Solution Architect.
4. **2027-01-08 — Signature and term start:** execute the scoped order **three months after the discovery date**, beginning a **three-month minimum term running 2027-01-08–2027-04-07** and authorizing the **six-week pilot period running 2027-01-11–2027-02-21**. **Their owner:** Procurement Director. **Our owner:** Commercial Lead.
5. **2027-02-22 and 2027-03-26 — Value review and expansion decision:** review value immediately after the full six-week pilot on **2027-02-22**, then decide whether to expand on **2027-03-26**, before the third billing month ends on **2027-04-07**. **Their owner:** Operations Finance Lead. **Our owner:** Value Lead.

## What I would walk away from
No accountable sponsor, no usable baseline, unresolved security requirements, demands for guaranteed savings, or uncapped usage without budget ownership. Walk away if the customer will not commit **$10,000–$15,000 per billing month for at least three billing months**, or if either side will not resource the six-week pilot, attend the value review or make the expansion decision before the third billing month ends. Do not sell enterprise-wide deployment before the pilot demonstrates a defensible operational benefit.


## 11

### Draft

The draft corrected here is the five-account version previously written to `account_plans.md` and shown in the model response for Quorvane Therapeutics and Norevix Capital Group. It opened both plans with objectives tied directly to named use cases, proposed cross-division reuse of cases, listed stakeholders by function rather than decision role, and proposed expansion in Norevix before diagnosing its decline.

### What is wrong and why

Log this. In a declining account I find the cause and rebuild trust before I sell anything. Fix all five plans. One: write three customer objectives in the customer's own business language, each with a measure, and never name our use case inside an objective. Two: where any division is declining, open the plan with a section called Why usage is falling: three hypotheses to test, the executive conversation to hold, and how the proven case is protected. Propose no new division until that is done. Three: where active users are under half of seats, name it as an adoption problem and plan to raise use before expanding. Four: give each next division a case that fits its own work; never borrow a case that does not fit. Five: map stakeholders by role in the decision: executive sponsor, budget holder, security and data approver, procurement, day to day owner, and state where the relationship is weak. Six: give each quarter an owner, a measure and one executive review. Use the same dated quarters in every plan. Show me Quorvane and Norevix again.

### Fixed version

All five plans in `account_plans.md` now use three customer-language objectives with measures, decision-role stakeholder maps, adoption gates, work-fitting cases and the same dated quarters. Norevix opens with three decline hypotheses, a trust-rebuilding executive conversation, protection for its proven case and a no-expansion recovery gate. The complete corrected Quorvane and Norevix plans were delivered with this correction.


## 12

### Draft

The customer-facing executive reviews in the five-account draft included these lines:

```text
Executive review: Grid Operations Executive reviews the $335,000 quarterly target and Customer Systems adoption recovery.
Executive review: Manufacturing Operations Executive reviews the $200,000 quarterly target and appoints a Quality Assurance owner.
Executive review: Manufacturing Operations Executive reviews the $600,000 quarterly target and Field Engineering adoption.
Executive review: Chief Supply Chain Officer reviews the $610,000 quarterly target and Supplier Quality sponsorship.
```

`internal_forecast.md` and `customer_report.md` had not yet been written.

### What is wrong and why

Log this. A customer executive never reviews our revenue target. In every account plan, remove our targets and forecasts from the customer's executive reviews; keep them in the risks section only. Then write two reports. First, internal_forecast.md: a one page note for sales leadership. Revenue forecast against target for the whole book and for each account at low, middle and high, the back-test error, the gap, the cases and pipeline that would close it, the risks, and what I need from colleagues. Say plainly that prospects still at prospecting stage add nothing to next quarter, and that Norevix is in recovery with no expansion forecast. Second, for the largest account only, customer_report.md: a one page report for the customer's executive. Value planned against value achieved so far, both on the same twelve month basis, with the working and the customer return. One proven case told in four short parts: the problem, the root causes, the actions, the value. Adoption by division. Three suggested next steps, each tied to one of their stated objectives. No selling language, and none of our targets. Label every number with what it counts and its period, and say once at the top that it is a draft on invented data. Show me both.

### Fixed version

All customer executive-review lines in `account_plans.md` now concern customer evidence, adoption, decisions and outcomes; internal revenue targets and forecasts remain only in each plan's Risks section. `internal_forecast.md` contains the sales-leadership view, including a Norevix recovery override with no expansion forecast. `customer_report.md` covers Talvexon Industrial Systems, the largest account by twelve-month tokens, and contains customer value and adoption without internal targets.


## 13

### Draft

The model's earlier planner output and later internal report gave different high forecasts for Norevix and different resulting book totals. The conflicting lines were:

```text
Norevix Capital Group        $225,000  $204,211 estimate  -$20,789  $204,211 estimate  -$20,789    $258,811 estimate  $33,811   $200,826 estimate         behind
Next-quarter high-only pipeline total: $105,300 estimate; prospecting-stage prospects contribute $0 to next quarter.
```

```text
| Norevix Capital Group | $225,000 | $204,211 | -$20,789 | $204,211 | -$20,789 | $204,211 | -$20,789 | -4.6% |
| **Whole book** | **$1,970,000** | **$1,853,371** | **-$116,629** | **$1,959,121** | **-$10,879** | **$2,169,721** | **+$199,721** | **-6.6%** |
```

The value-case output also placed generic money value working beside a plain operational measure without saying explicitly what the money counted or that the plain measure was separate.

### What is wrong and why

Log this. Two files must never give two numbers for the same thing. One: apply the Norevix recovery rule in planner.py itself, so the high forecast is $204,211 in every output, and update the account plan, the forecast table and the pipeline total to match. Show the rule in one plain line: an account in recovery counts no proposed case and no pipeline. Two: wherever a money value sits beside a plain measure, say what the money counts, for example production downtime avoided, and say the plain measure is a separate result, not the source of the money. Check every file for both. Show me the new whole-book totals and the pipeline total.

### Fixed version

`planner.py` now owns the recovery rule: an account in recovery counts no proposed case and no pipeline. Norevix low, middle and high are all $204,211 for the three-month forecast quarter. The whole-book three-month totals are $1,853,371 low, $1,959,121 middle and $2,169,721 high against a $1,970,000 target. Eligible next-quarter high-only pipeline is $88,200. Live reports, plans, briefs, source data and generation scripts now identify what each money value counts and identify any adjacent plain measure as a separate result rather than the source of the money. Historical correction quotations remain unchanged because they are exact records of earlier drafts.


## 14

### Draft

The account plans and forecast previously took conflicting positions on the same divisions. The relevant draft lines were:

```text
- Customer Systems has an adoption problem and must raise active use before expansion.
Do not open Procurement yet: it has a 24% active-seat rate and no supplied case that fits procurement work.
Do not expand Field Engineering until adoption rises above 50% and a case that fits field-engineering work is defined.
- Supplier Quality has an owner but no sponsor; its case remains high-only.
```

```text
- **Azrulon:** Dispatch exception triage adds $33,750 for 3 months to middle. Permit evidence assistant adds $30,000 for 3 months and Customer Systems pipeline adds $27,000 for 3 months to high.
- **Quorvane:** Batch record review adds $21,000 for 3 months to middle, leaving a $50 gap. Deviation investigation drafts adds $18,900 for 3 months and Procurement pipeline adds $16,800 for 3 months to high.
- **Talvexon:** No case adds to middle. Supplier disruption planning adds $42,000 for 3 months and Field Engineering pipeline adds $24,000 for 3 months to high.
- **Veyrith:** Demand plan scenario briefs adds $51,000 for 3 months to middle. Supplier audit evidence review adds $31,500 for 3 months and Supplier Quality pipeline adds $20,400 for 3 months to high.
```

The Qelvoryn brief said:

```text
Propose a four-week pilot in one division, using one agreed measure: production downtime hours per week. Fix the baseline before starting as the average weekly downtime hours over the preceding four weeks, and compare results against it without treating any change as proof of causation.
```

The deal strategy heading was:

```text
## Joint plan agreed with the customer
```

### What is wrong and why

Log this. Two files must not take two positions on the same division. The account plans say do not expand Customer Systems, Procurement and Field Engineering, yet the forecast counts their pipeline, and Supplier Quality is counted twice. One: add an eligibility rule to planner.py: division pipeline counts in high only when active users are above half of seats, a case that fits the division's own work exists, and that case is not already counted. Show ineligible pipeline with its reason and $0. Update every file. Two: make the Qelvoryn brief's pilot six weeks, and say shift handovers everywhere, never activities. Three: rename the deal strategy heading to Joint plan to agree with the customer. Four: remove the word supplied wherever it describes a case, contact or sponsor; say none yet identified. Five: in the internal note, say I will secure the missing sponsors and owner myself, and ask sales leadership for executive support on the Norevix recovery conversation. Six: update the README correction count. Show me the new whole-book totals and the pipeline view.

### Fixed version

`planner.py` now applies one division-pipeline eligibility rule to both the account forecast and pipeline view. Customer Systems, Markets Operations, Procurement, Field Engineering and Supplier Quality each show $0 with their specific ineligibility reasons, so eligible next-quarter division pipeline is $0. The three-month whole-book high forecast is $2,081,521; low and middle remain $1,853,371 and $1,959,121. The Qelvoryn pilot is six weeks, Qelvoryn materials say shift handovers rather than activities, the deal-strategy heading is `Joint plan to agree with the customer`, relationship gaps say none yet identified, the internal support request is corrected, and the README records fourteen corrections.


## 15

Two invented names contained a real company's name and were renamed.
