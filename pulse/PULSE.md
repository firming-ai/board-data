# FILL — the inference availability index

*As of 2026-10-08T09:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-09T09:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-08/09.json`; their sha256 `3d03e3500ec8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.9** · FILL·FLEX 98.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.5% | — | 99.1% (n=220) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 94.1% | 100.0% (n=32) | 82.2% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1138 ms |
| bedrock | 100.0% | — | 0.0% | 717 ms |
| deepseek | 100.0% | — | 0.0% | 1218 ms |
| gemini | 100.0% | 80.9% | 5.2% | 939 ms |
| mistral | 100.0% | — | 0.0% | 777 ms |
| openai | 99.7% | 99.2% | 0.0% | 1049 ms |
| openrouter | 100.0% | — | 0.0% | 1596 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 222 | 218 | 4 | 0 | 85.3% | 92.7% | 99.1% | 100.0% | 100.0% | 3 min | 11 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 93.8% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 4 min |
| openai | 264 | 260 | 4 | 0 | 78.1% | 80.4% | 84.2% | 93.2% | 99.6% | 67 s | 283 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
