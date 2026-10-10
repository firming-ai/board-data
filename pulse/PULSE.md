# FILL — the inference availability index

*As of 2026-10-09T07:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-10T07:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-09/07.json`; their sha256 `8d365934139c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 97.1** · FILL·FLEX 98.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.6% (n=264) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 94.4% | 100.0% (n=32) | 83.3% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1255 ms |
| bedrock | 100.0% | — | 0.0% | 737 ms |
| deepseek | 100.0% | — | 0.0% | 1248 ms |
| gemini | 99.3% | 88.1% | 5.8% | 943 ms |
| mistral | 100.0% | — | 0.0% | 724 ms |
| openai | 99.7% | 98.7% | 0.0% | 1144 ms |
| openrouter | 100.0% | — | 0.0% | 1573 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 263 | 1 | 0 | 62.4% | 72.6% | 99.6% | 100.0% | 100.0% | 4 min | 31 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 91.5% | 93.6% | 100.0% | 100.0% | 100.0% | 28 s | 16 min |
| openai | 264 | 259 | 5 | 0 | 76.4% | 81.1% | 84.9% | 89.8% | 100.0% | 67 s | 397 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
