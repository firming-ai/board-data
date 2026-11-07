# FILL — the inference availability index

*As of 2026-11-06T19:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-07T19:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-06/19.json`; their sha256 `24d96fac8891…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.5** · FILL·FLEX 84.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 77.8% | 55.6% (n=18) | 100.0% (n=94) | — |
| MIS·FILL | 60.4% | — | 60.4% (n=48) | — |
| OAI·FILL | 96.6% | 100.0% (n=32) | 89.7% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1497 ms |
| bedrock | 98.4% | — | 1.6% | 704 ms |
| deepseek | 100.0% | — | 0.0% | 1384 ms |
| gemini | 100.0% | 59.7% | 13.9% | 1275 ms |
| mistral | 100.0% | — | 0.0% | 930 ms |
| openai | 98.8% | 92.5% | 0.0% | 1146 ms |
| openrouter | 100.0% | — | 0.0% | 1552 ms |
| xai | 100.0% | — | 0.0% | 945 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 97.0% | 100.0% | 100.0% | 100.0% | 100.0% | 101 s | 3 min |
| gemini | 96 | 93 | 1 | 2 | 98.9% | 98.9% | 97.9% | 97.9% | 100.0% | 2 min | 4 min |
| mistral | 48 | 29 | 19 | 0 | 93.1% | 93.1% | 93.1% | 72.9% | 100.0% | 50 s | 146 min |
| openai | 312 | 306 | 6 | 0 | 82.7% | 86.3% | 91.5% | 93.3% | 100.0% | 66 s | 234 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
