# FILL — the inference availability index

*As of 2026-10-02T11:05:13+00:00 · probe pulse-1.4.2 · methodology 1.3.1*

*Published 2026-10-03T11:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-02/11.json`; their sha256 `9fcc09259452…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 95.0** · FILL·FLEX 95.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.7% | — | 85.4% (n=192) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.3% | 100.0% (n=32) | 95.0% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1384 ms |
| bedrock | 100.0% | — | 0.0% | 692 ms |
| deepseek | 100.0% | — | 0.0% | 1253 ms |
| gemini | 100.0% | 82.5% | 9.6% | 960 ms |
| mistral | 100.0% | — | 0.0% | 730 ms |
| openai | 99.2% | 99.0% | 0.0% | 977 ms |
| openrouter | 100.0% | — | 0.0% | 1447 ms |
| xai | 100.0% | — | 0.0% | 924 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 192 | 0 | 0 | 75.5% | 76.6% | 89.6% | — | — | 2 min | 70 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 91.7% | 91.7% | 100.0% | — | — | 22 s | 17 min |
| openai | 240 | 231 | 3 | 6 | 75.1% | 82.3% | 96.2% | — | — | 80 s | 35 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
