# FILL — the inference availability index

*As of 2026-10-28T18:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-29T18:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-28/18.json`; their sha256 `a8057b3e2831…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.8** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 97.9% | 100.0% (n=32) | 93.6% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1138 ms |
| bedrock | 98.4% | — | 1.6% | 864 ms |
| deepseek | 100.0% | — | 0.0% | 1354 ms |
| gemini | 100.0% | 60.7% | 20.6% | 1368 ms |
| mistral | 90.8% | — | 9.2% | 939 ms |
| openai | 99.8% | 98.4% | 0.0% | 1241 ms |
| openrouter | 100.0% | — | 0.0% | 1612 ms |
| xai | 100.0% | — | 0.0% | 960 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 98.5% | 100.0% | 100.0% | 100.0% | 100.0% | 100 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 27 s | 95 s |
| openai | 312 | 312 | 0 | 0 | 83.0% | 86.2% | 94.9% | 94.9% | 100.0% | 67 s | 60 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
