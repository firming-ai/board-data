# FILL — the inference availability index

*As of 2026-10-28T03:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-29T03:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-28/03.json`; their sha256 `439e0f16eb75…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.3** · FILL·FLEX 80.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 77.8% | 55.6% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.2% | 93.8% (n=32) | 77.0% (n=304) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1120 ms |
| bedrock | 98.4% | — | 1.6% | 812 ms |
| deepseek | 100.0% | — | 0.0% | 1398 ms |
| gemini | 100.0% | 61.2% | 20.6% | 1283 ms |
| mistral | 100.0% | — | 0.0% | 910 ms |
| openai | 98.8% | 99.0% | 0.0% | 1146 ms |
| openrouter | 100.0% | — | 0.0% | 1539 ms |
| xai | 100.0% | — | 0.0% | 945 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 97.0% | 99.2% | 100.0% | 100.0% | 100.0% | 106 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 100.0% | 100.0% | 100.0% | 100.0% | 24 s | 98 s |
| openai | 306 | 304 | 2 | 0 | 64.1% | 69.1% | 78.0% | 84.9% | 93.6% | 110 s | 603 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
