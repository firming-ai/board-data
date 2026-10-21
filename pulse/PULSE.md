# FILL — the inference availability index

*As of 2026-10-20T18:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-21T18:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-20/18.json`; their sha256 `c868e49deea1…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.3** · FILL·FLEX 74.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 68.8% | — | 68.8% (n=48) | — |
| OAI·FILL | 90.8% | 81.2% (n=32) | 91.3% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1053 ms |
| bedrock | 98.4% | — | 1.6% | 730 ms |
| deepseek | 100.0% | — | 0.0% | 1248 ms |
| gemini | 100.0% | 57.3% | 19.8% | 1325 ms |
| mistral | 100.0% | — | 0.0% | 855 ms |
| openai | 100.0% | 82.0% | 0.0% | 1164 ms |
| openrouter | 100.0% | — | 0.0% | 1485 ms |
| xai | 100.0% | — | 0.0% | 813 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 89.4% | 97.0% | 99.2% | 100.0% | 100.0% | 2 min | 7 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 36.2% | 42.6% | 68.1% | 100.0% | 100.0% | 21 min | 155 min |
| openai | 264 | 248 | 16 | 0 | 81.9% | 85.9% | 95.2% | 98.1% | 100.0% | 67 s | 56 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
