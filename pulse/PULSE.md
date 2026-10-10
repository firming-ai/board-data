# FILL — the inference availability index

*As of 2026-10-09T21:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-10T21:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-09/21.json`; their sha256 `bccb6f21a9f2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.6** · FILL·FLEX 91.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.7% | 100.0% (n=32) | 87.1% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1206 ms |
| bedrock | 100.0% | — | 0.0% | 754 ms |
| deepseek | 100.0% | — | 0.0% | 1255 ms |
| gemini | 100.0% | 91.2% | 2.9% | 1115 ms |
| mistral | 100.0% | — | 0.0% | 774 ms |
| openai | 100.0% | 99.0% | 0.0% | 1033 ms |
| openrouter | 100.0% | — | 0.0% | 1625 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 259 | 5 | 0 | 60.6% | 83.4% | 99.6% | 100.0% | 100.0% | 4 min | 34 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 91.7% | 93.8% | 100.0% | 100.0% | 100.0% | 43 s | 13 min |
| openai | 264 | 252 | 12 | 0 | 82.1% | 85.3% | 91.3% | 90.5% | 100.0% | 66 s | 311 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
