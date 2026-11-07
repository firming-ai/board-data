# FILL — the inference availability index

*As of 2026-11-06T06:05:02+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-07T06:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-06/06.json`; their sha256 `203e5461f3cc…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.1** · FILL·FLEX 90.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 86.1% | 72.2% (n=18) | 100.0% (n=94) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.3% | 100.0% (n=32) | 88.8% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1368 ms |
| bedrock | 100.0% | — | 0.0% | 650 ms |
| deepseek | 100.0% | — | 0.0% | 1330 ms |
| gemini | 100.0% | 68.0% | 10.6% | 1159 ms |
| mistral | 100.0% | — | 0.0% | 758 ms |
| openai | 100.0% | 100.0% | 0.0% | 984 ms |
| openrouter | 100.0% | — | 0.0% | 1330 ms |
| xai | 100.0% | — | 0.0% | 792 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 258 | 6 | 0 | 98.4% | 99.6% | 100.0% | 100.0% | 100.0% | 103 s | 3 min |
| gemini | 96 | 94 | 0 | 2 | 98.9% | 100.0% | 97.9% | 97.9% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 89.6% | 100.0% | 100.0% | 100.0% | 51 s | 22 min |
| openai | 312 | 304 | 8 | 0 | 83.2% | 85.9% | 90.8% | 91.7% | 100.0% | 66 s | 336 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
