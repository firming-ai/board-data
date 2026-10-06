# FILL — the inference availability index

*As of 2026-10-05T15:05:06+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-06T15:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-05/15.json`; their sha256 `7d2b49ffa26e…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.5** · FILL·FLEX 71.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=216) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=48) | — |
| OAI·FILL | 97.8% | 93.8% (n=32) | 99.6% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1206 ms |
| bedrock | 100.0% | — | 0.0% | 754 ms |
| deepseek | 100.0% | — | 0.0% | 1365 ms |
| gemini | 100.0% | 54.1% | 24.1% | 1196 ms |
| mistral | 99.2% | — | 0.8% | 886 ms |
| openai | 98.5% | 90.4% | 0.0% | 1411 ms |
| openrouter | 100.0% | — | 0.0% | 1638 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 216 | 216 | 0 | 0 | 98.6% | 99.1% | 100.0% | 100.0% | 100.0% | 97 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 93.8% | 95.8% | 100.0% | 100.0% | 57 s | 25 min |
| openai | 264 | 261 | 3 | 0 | 91.6% | 96.2% | 100.0% | 100.0% | 100.0% | 66 s | 9 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
