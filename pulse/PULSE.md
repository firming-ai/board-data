# FILL — the inference availability index

*As of 2026-10-21T14:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-22T14:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-21/14.json`; their sha256 `64e0b35d6196…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.2** · FILL·FLEX 74.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 83.3% | 66.7% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 87.4% | 78.1% (n=32) | 84.1% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1147 ms |
| bedrock | 100.0% | — | 0.0% | 755 ms |
| deepseek | 100.0% | — | 0.0% | 1291 ms |
| gemini | 100.0% | 69.9% | 16.6% | 1263 ms |
| mistral | 100.0% | — | 0.0% | 921 ms |
| openai | 99.5% | 83.1% | 0.0% | 1137 ms |
| openrouter | 100.0% | — | 0.0% | 1503 ms |
| xai | 100.0% | — | 0.0% | 852 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 94.7% | 98.5% | 99.6% | 100.0% | 100.0% | 110 s | 5 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 89.6% | 100.0% | 100.0% | 100.0% | 25 s | 25 min |
| openai | 264 | 258 | 6 | 0 | 73.3% | 76.7% | 86.0% | 95.1% | 100.0% | 67 s | 141 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
