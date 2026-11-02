# FILL — the inference availability index

*As of 2026-11-01T02:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-02T02:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-01/02.json`; their sha256 `05b40b7dbb70…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.1** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=48) | — |
| OAI·FILL | 95.7% | 100.0% (n=32) | 87.2% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1341 ms |
| bedrock | 100.0% | — | 0.0% | 583 ms |
| deepseek | 100.0% | — | 0.0% | 1243 ms |
| gemini | 100.0% | 68.0% | 14.9% | 981 ms |
| mistral | 100.0% | — | 0.0% | 718 ms |
| openai | 100.0% | 100.0% | 0.0% | 986 ms |
| openrouter | 100.0% | — | 0.0% | 1280 ms |
| xai | 100.0% | — | 0.0% | 745 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 93 s | 2 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 68.8% | 68.8% | 95.8% | 100.0% | 100.0% | 56 s | 51 min |
| openai | 312 | 312 | 0 | 0 | 78.2% | 81.1% | 87.8% | 98.7% | 100.0% | 67 s | 131 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
