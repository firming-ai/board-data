# FILL — the inference availability index

*As of 2026-11-09T07:05:02+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-10T07:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-09/07.json`; their sha256 `9ee33337cff0…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.9** · FILL·FLEX 82.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.1% | — | 98.1% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 95.9% | 93.8% (n=32) | 93.9% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1322 ms |
| bedrock | 100.0% | — | 0.0% | 630 ms |
| deepseek | 100.0% | — | 0.0% | 1286 ms |
| gemini | 100.0% | 63.1% | 9.5% | 1087 ms |
| mistral | 100.0% | — | 0.0% | 736 ms |
| openai | 99.8% | 97.7% | 0.0% | 909 ms |
| openrouter | 100.0% | — | 0.0% | 1371 ms |
| xai | 100.0% | — | 0.0% | 761 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 94.3% | 96.2% | 98.1% | 100.0% | 100.0% | 99 s | 8 min |
| gemini | 96 | 95 | 1 | 0 | 90.5% | 95.8% | 100.0% | 100.0% | 100.0% | 2 min | 9 min |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 87.5% | 97.9% | 100.0% | 100.0% | 52 s | 36 min |
| openai | 312 | 311 | 1 | 0 | 84.9% | 88.7% | 94.2% | 98.1% | 100.0% | 66 s | 86 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
