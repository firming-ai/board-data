# FILL — the inference availability index

*As of 2026-10-27T09:05:02+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-10-28T09:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-27/09.json`; their sha256 `9ac7de602931…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.9** · FILL·FLEX 76.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 80.6% | 61.1% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 83.2% | 84.4% (n=32) | 65.3% (n=268) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1260 ms |
| bedrock | 100.0% | — | 0.0% | 770 ms |
| deepseek | 100.0% | — | 0.0% | 1401 ms |
| gemini | 99.4% | 62.6% | 11.4% | 1283 ms |
| mistral | 100.0% | — | 0.0% | 895 ms |
| openai | 99.8% | 87.2% | 0.0% | 1110 ms |
| openrouter | 100.0% | — | 0.0% | 1558 ms |
| xai | 100.0% | — | 0.0% | 886 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 95.5% | 98.5% | 100.0% | 100.0% | 100.0% | 108 s | 4 min |
| gemini | 96 | 96 | 0 | 0 | 97.9% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 22 s | 72 s |
| openai | 270 | 259 | 11 | 0 | 56.0% | 58.7% | 68.7% | 72.3% | 75.4% | 3 min | 636 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
