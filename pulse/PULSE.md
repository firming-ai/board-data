# FILL — the inference availability index

*As of 2026-10-21T07:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-22T07:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-21/07.json`; their sha256 `01201d09dc6a…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.5** · FILL·FLEX 80.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.6% | — | 99.2% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 85.4% | — | 85.4% (n=48) | — |
| OAI·FILL | 91.2% | 90.6% (n=32) | 83.0% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1288 ms |
| bedrock | 98.4% | — | 1.6% | 737 ms |
| deepseek | 100.0% | — | 0.0% | 1387 ms |
| gemini | 98.8% | 63.1% | 7.6% | 1228 ms |
| mistral | 100.0% | — | 0.0% | 825 ms |
| openai | 100.0% | 99.2% | 0.0% | 1110 ms |
| openrouter | 100.0% | — | 0.0% | 1482 ms |
| xai | 100.0% | — | 0.0% | 902 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 93.6% | 97.7% | 99.2% | 100.0% | 100.0% | 111 s | 7 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 119 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 62.5% | 70.8% | 89.6% | 100.0% | 100.0% | 43 s | 90 min |
| openai | 264 | 263 | 1 | 0 | 70.3% | 73.8% | 82.9% | 95.1% | 100.0% | 68 s | 227 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
