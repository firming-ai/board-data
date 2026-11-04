# FILL — the inference availability index

*As of 2026-11-03T18:05:07+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-04T18:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-03/18.json`; their sha256 `104b0f954314…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.4** · FILL·FLEX 78.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 75.0% | 50.0% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 91.7% | — | 91.7% (n=48) | — |
| OAI·FILL | 90.3% | 93.8% (n=32) | 77.2% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1175 ms |
| bedrock | 100.0% | — | 0.0% | 661 ms |
| deepseek | 100.0% | — | 0.0% | 1184 ms |
| gemini | 100.0% | 57.3% | 18.8% | 1341 ms |
| mistral | 100.0% | — | 0.0% | 864 ms |
| openai | 99.8% | 89.6% | 0.0% | 1146 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 774 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.3% | 99.6% | 100.0% | 100.0% | 100.0% | 96 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 46 | 2 | 0 | 80.4% | 82.6% | 91.3% | 100.0% | 100.0% | 64 s | 95 min |
| openai | 312 | 298 | 14 | 0 | 66.8% | 70.8% | 80.9% | 93.9% | 100.0% | 75 s | 169 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
