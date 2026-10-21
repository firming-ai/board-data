# FILL — the inference availability index

*As of 2026-10-20T11:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-21T11:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-20/11.json`; their sha256 `2f9e00529d26…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.9** · FILL·FLEX 86.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.4% | — | 98.9% (n=264) | 100.0% (n=30) |
| GEM·FILL | 86.1% | 72.2% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 66.7% | — | 66.7% (n=48) | — |
| OAI·FILL | 96.2% | 93.8% (n=32) | 94.7% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1076 ms |
| bedrock | 95.3% | — | 4.7% | 737 ms |
| deepseek | 100.0% | — | 0.0% | 1258 ms |
| gemini | 100.0% | 66.5% | 10.9% | 1147 ms |
| mistral | 100.0% | — | 0.0% | 825 ms |
| openai | 100.0% | 87.8% | 0.0% | 1033 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 843 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 89.8% | 96.2% | 98.9% | 100.0% | 100.0% | 2 min | 8 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 46 | 2 | 0 | 30.4% | 39.1% | 67.4% | 100.0% | 100.0% | 31 min | 155 min |
| openai | 264 | 256 | 8 | 0 | 84.8% | 88.7% | 96.5% | 98.9% | 100.0% | 66 s | 38 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
