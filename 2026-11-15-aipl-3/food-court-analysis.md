# Food Court: independently replayed workshop and TDS results

**Data refreshed 18 Nov 2026** via `npm run realtime:sync -- --game food-court --json` in ~/code/tds-network-games. Sync returned 7 scheduled sessions, 174 rooms, 715 session-entrants, 7,334 chat messages, 0 new events, 0 replay failures, 0 skipped sessions. An earlier 8 Nov pilot (1 room, 4 entrants, 768 saves) is **excluded from the comparison**. Three 10–11 Nov TDS sessions + three 15 Nov AIPL sessions yield 173 rooms, 711 session-entrants. These counts include repeat entrants, not distinct individuals. The first AIPL session is the primary in-meeting comparison, not the two later sessions or all three pooled.

## Rules and metric definitions verified from production source

Read ~/code/tds-network-games/src/realtime/games/food-court/{game.ts,model.ts}. The session uses 4 or 5 stalls; 12 months; monthly discounts 0%, 10%, 20%; twenty-minute live game with one-minute save grace. Everyone starts with all 0%. A Save commits a single restaurant's 12 choices. Checkpoints at 7, 12, 17, 21 minutes. Last negotiation 17–19 m, then final save 19–20, server grace to 21. Plans visible to others. 

**Team score** = normalized combined food-court 12-month profit versus exactly attainable maximum for that room size. **Individual score** = normalized stall profit versus attainable individual maximum (different from team normalization). **Final score / grade** = 60% team + 40% individual, with both components averaged across four checkpoints. The server's results.csv team column is the **mean of four checkpoint team scores**, identical per teammate. Do not average participant rows across rooms (would upweight larger rooms); use distinct room IDs. Do not label the combined score as final checkpoint profit. The fourth-checkpoint plan differs from the time-average performance. Save counts are recorded actions, not necessarily distinct meaningful modifications.

### All six sessions, room-weighted team score and exact final saved discount cells

| Session (local scheduled time) | Entrants | Rooms | Team score mean /100 | Final cells at 20% | Saves | Chats |
|---|---:|---:|---:|---:|---:|---:|
| TDS 10 Nov 18:00 IST | 247 | 61 | 92.51 | 736/2964 (24.83%) | 1629 | 2327 |
| TDS 11 Nov 07:30 IST | 106 | 25 | 95.57 | 192/1272 (15.09%) | 459 | 1157 |
| TDS 11 Nov 21:00 IST | 305 | 75 | 94.13 | 900/3660 (24.59%) | 1801 | 3548 |
| AIPL 15 Nov 12:00 SGT (first, live debrief) | 32 | 7 | **88.06** | **193/384 (50.26%)** | 260 | 161 |
| AIPL 15 Nov 12:30 SGT | 12 | 3 | 89.73 | 49/144 (34.03%) | 32 | 44 |
| AIPL 15 Nov 13:00 SGT | 9 | 2 | 84.71 | 84/108 (77.78%) | 71 | 97 |
| **TDS pooled** | **658** | **161** | **93.74** | **1828/7896 (23.15%)** | **3889** | **7032** |
| **AIPL pooled** | **53** | **12** | **87.92** | **326/636 (51.26%)** | **363** | **302** |

Pooled arithmetic uses all rooms, not simple mean of each sitting's mean. TDS 482 unique email identities over 658 seats; AIPL 43 unique over 53 seats. First AIPL: 8/32 IITM student-domain emails, 4/32 appeared in the three earlier TDS sittings. All three AIPL sittings respectively 8, 7, 9 IITM-domain entrants, so note **all 9 in the third run have IITM addresses**. These later runs are not an independent professional cohort. First run alone is the live talk's core comparison.

**Correction to earlier companion chat:** 49.4% was reported for AIPL maximum discounts, and ~24.7/15.2/24.5% for the earlier sittings. Replaying the currently synced full chronological saves (initial all zero, update actor column) gives the exact final saved values above. The discrepancy may be snapshot or method; use the reproducible values, or simply "about half vs about a quarter." 95.56 vs 95.57 is a rounding issue, not substantive.

### Checkpoints: did repeated negotiations help?

| Session | 7m | 12m | 17m | 21m | Rooms with decline from 7→21m |
|---|---:|---:|---:|---:|---:|
| TDS 10 Nov | 92.38 | 93.64 | 91.93 | 92.10 | 28/61 |
| TDS 11 Nov morning | 96.00 | 96.61 | 94.87 | 94.79 | 9/25 |
| TDS 11 Nov evening | 94.82 | 94.81 | 94.23 | 92.68 | 44/75 |
| AIPL first | **91.81** | **87.83** | **86.66** | **85.95** | **6/7** |
| AIPL second | 89.90 | 89.79 | 89.93 | 89.30 | 1/3 |
| AIPL third | 86.52 | 85.24 | 86.87 | 80.21 | 2/2 |
| TDS pooled | 94.08 | 94.64 | 93.46 | 92.79 | 81/161 |
| AIPL pooled | 90.45 | 87.89 | 87.51 | 85.83 | 9/12 |

AIPL first fell **5.86 points**; TDS pooled fell **1.29 points**. The six worsening rooms don't prove chats caused deterioration; room interactions, incentive structure and selection could produce patterns. At least one team improved.

First AIPL room-level data, rounded; room identifiers are internal locators, use anonymous labels in public. Final 20%-choice count across 12×seat cells:

| Room | Stalls | Checkpoint 7m | Checkpoint 21m | Saves | Chat | 20% cells |
|---|---:|---:|---:|---:|---:|---:|
| r001 | 5 | 85.77 | 79.51 | 68 | 10 | 45/60 |
| r002 | 5 | 95.21 | 79.69 | 56 | 11 | 47/60 |
| r003 | 5 | 94.49 | 89.22 | 9 | 8 | 21/60 |
| r004 | 5 | 91.70 | 86.63 | 31 | 17 | 22/60 |
| r005 | 4 | 94.55 | 87.91 | 48 | 43 | 21/48 |
| r006 | 4 | 89.67 | 86.14 | 14 | 11 | 24/48 |
| r007 | 4 | 91.27 | 92.56 | 34 | 61 | 13/48 |

Notice r002's collapse −15.52 points despite substantial changes. The high-chat improving room is a counterexample to "talking harms": r007 chatted 61 times, improved ~1.29 points. Low-chat r003 had the highest **overall team score** 91.84 (mean of checkpoints), not highest final checkpoint. Don't confuse the two. First AIPL scores across rooms ranged 83.84–91.84, 2/7 at least 90. TDS 122/161 at least 90. Median in-game chat messages 11 for first AIPL, 29/38/41 for three TDS sessions. 

First workshop average 37.14 saves/room vs pooled TDS 24.16 (+54% approximately); chat 23.0 vs 43.68 (−47%). Exact arithmetic based on counts gives about **54%** more saves, not a difference in verified player effort. Four five-person AIPL rooms had fewer chat messages than three four-person rooms; room size is a confound. Across all sittings, stratification doesn't remove score gap: 4-stall AIPL 7 rooms mean 88.26 vs TDS 147 rooms 93.82; 5-stall AIPL 5 rooms 87.44 vs TDS 14 rooms 92.91. This is descriptive, heavily confounded and includes mixed/repeat participants. Do not claim randomization or causal significance.

## Exact-model explorable

From model.ts (read only): discount step x_i = percentage / 10, x_i ∈ {0,1,2}, previous January step=0. Attraction a_i = exp(0.9*x_i + 0.2*previous_x_i). Share = 0.45/N + 0.55*a_i/sum(a). Footfall factor = 1 + 0.5*(1 − exp(−sum(x))), i.e. diminishing group demand benefit. Profit_i in model units = (6 − x_i) × share_i × footfall × seasonal demand. Monthly season multipliers Jan–Dec = [0.8,0.9,0.95,1.1,1.2,1.0,0.95,1.1,1.25,1.15,1.0,0.9]. Rupee display uses ×10,000; simulated price ₹200 and cost ₹80. Exact 12-month team ceilings: N=4 95.24064064675935; N=5 96.81393790275395. Individual ceilings N=4 36.81052427429191 and N=5 32.96915732315067. Normalized team score is 100 * total / team ceiling. Individual score is 100 * own profit / individual ceiling. Final composite is 0.6 team + 0.4 individual.

Independent recomputation of fixed policies (12 months, team score, not combined mean/final grade):

| Policy | 4 stalls | 5 stalls |
|---|---:|---:|
| All 0%, every month | 77.49 | 76.23 |
| All 10%, every month | 96.27 | 95.07 |
| All 20%, every month | 77.48 | 76.23 |
| Rotate two 10% promoters and rest 0%, cycling pairs (indices 2t mod N, (2t+1) mod N) | 100.00 | 100.00 |

Rotation rounds to 100, but don't claim a mathematically identical optimal solution for every seasonal array/model variant. Check full precision before claiming exact equality. This validates the lecture's qualitative claim within this model. It does **not** imply every player gets 100 individually, nor that this is a stable or lawful strategy for independent commercial competitors. In the game, incentives are designed around a shared food-court score. An independently optimizing agent may defect. Show the tension using exact own/team numbers for a one-month change or a 12-month plan, not a real business prescription. Price wars may benefit actual consumers; the game does not measure their welfare.

## Reproduce / data provenance

Session folders under ~/code/tds-network-games/.private/realtime/food-court/. IDs:
- food-court-20261110-1800, food-court-20261111-0730, food-court-20261111-2100;
- food-court-aipl-20261115-1200, ...-1230, ...-1300.

Read session.json rooms (size, room_id); results.csv (team repeated per entrant); rooms/<room_id>.events.jsonl with seq, at, actor, type, data. For each room in event-log order: initialize N×12 zeros; on type=save replace row actor with data.column; on checkpoint score current array, collect by data.index 0–3; increment counts of save and chat events; after all events count final occurrences 20. Verify distinct room team in results.csv equals mean of four independently computed scores rounded to two decimals (tolerance 0.00501). **All 173 comparison rooms passed**; the production sync replay itself reported no mismatches. This is a stronger verification than comparing prior analysis's summaries. User identifiers were used only for aggregate overlap counts and not copied here. Keep full raw logs and participant names private. No scoring/deployment changes were made. The separate .private analysis README is a design prototype; distinguish its hypothetical ablations and recommendations from deployed model and real data.
