# FILL — the inference availability index

*As of 2026-10-19T15:05:03+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-20T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-19/15.json`; their sha256 `7b73c520f98d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.5** · FILL·FLEX 72.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 75.0% | 50.0% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 75.0% | — | 75.0% (n=48) | — |
| OAI·FILL | 93.9% | 84.4% (n=32) | 97.3% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1444 ms |
| bedrock | 81.2% | — | 18.8% | 830 ms |
| deepseek | 100.0% | — | 0.0% | 1376 ms |
| gemini | 100.0% | 58.2% | 23.1% | 1349 ms |
| mistral | 100.0% | — | 0.0% | 952 ms |
| openai | 100.0% | 83.3% | 0.0% | 1202 ms |
| openrouter | 100.0% | — | 0.0% | 1555 ms |
| xai | 100.0% | — | 0.0% | 913 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 91.6% | 97.7% | 99.2% | 100.0% | 100.0% | 2 min | 8 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 46 | 2 | 0 | 26.1% | 34.8% | 73.9% | 100.0% | 100.0% | 27 min | 135 min |
| openai | 264 | 259 | 5 | 0 | 88.4% | 91.9% | 98.5% | 99.6% | 100.0% | 40 s | 25 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
