# FILL — the inference availability index

*As of 2026-10-06T13:05:01+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-07T13:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-06/13.json`; their sha256 `55a35d4df095…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.4** · FILL·FLEX 75.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.8% | — | 99.5% (n=216) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 94.9% | 90.6% (n=32) | 93.9% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1352 ms |
| bedrock | 100.0% | — | 0.0% | 723 ms |
| deepseek | 100.0% | — | 0.0% | 1346 ms |
| gemini | 100.0% | 77.8% | 11.3% | 1046 ms |
| mistral | 100.0% | — | 0.0% | 830 ms |
| openai | 99.5% | 88.8% | 0.0% | 1251 ms |
| openrouter | 100.0% | — | 0.0% | 1545 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 216 | 213 | 3 | 0 | 88.7% | 99.1% | 100.0% | 100.0% | 100.0% | 3 min | 6 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 97.9% | 100.0% | 100.0% | 100.0% | 40 s | 4 min |
| openai | 264 | 260 | 4 | 0 | 80.0% | 83.8% | 94.6% | 98.9% | 100.0% | 68 s | 63 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
