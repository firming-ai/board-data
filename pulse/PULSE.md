# FILL — the inference availability index

*As of 2026-11-09T22:05:13+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-10T22:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-09/22.json`; their sha256 `68d32aa1193a…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.1** · FILL·FLEX 76.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.1% | — | 98.1% (n=264) | 100.0% (n=30) |
| GEM·FILL | 82.8% | 66.7% (n=18) | 99.0% (n=96) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 91.3% | 81.2% (n=32) | 92.6% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1129 ms |
| bedrock | 100.0% | — | 0.0% | 632 ms |
| deepseek | 100.0% | — | 0.0% | 1309 ms |
| gemini | 100.0% | 63.6% | 5.7% | 1223 ms |
| mistral | 100.0% | — | 0.0% | 841 ms |
| openai | 100.0% | 96.1% | 0.0% | 1049 ms |
| openrouter | 100.0% | — | 0.0% | 1509 ms |
| xai | 100.0% | — | 0.0% | 840 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 94.7% | 96.6% | 98.1% | 100.0% | 100.0% | 98 s | 7 min |
| gemini | 96 | 96 | 0 | 0 | 84.4% | 86.5% | 99.0% | 100.0% | 100.0% | 2 min | 17 min |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 89.6% | 97.9% | 100.0% | 100.0% | 54 s | 36 min |
| openai | 312 | 292 | 20 | 0 | 90.8% | 92.8% | 97.9% | 94.6% | 100.0% | 50 s | 20 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
