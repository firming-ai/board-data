# FILL — the inference availability index

*As of 2026-09-23T08:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T08:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/08.json`; their sha256 `5fc997be2a54…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.7** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.3% | — | 96.6% (n=118) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 85.5% | 73.7% (n=19) | 82.9% (n=140) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.5% | — | 0.5% | 1452 ms |
| bedrock | 100.0% | — | 0.0% | 711 ms |
| deepseek | 89.4% | — | 1.5% | 1235 ms |
| gemini | 100.0% | 82.0% | 9.3% | 1013 ms |
| mistral | 100.0% | — | 0.0% | 729 ms |
| openai | 94.9% | 74.6% | 0.0% | 1046 ms |
| openrouter | 100.0% | — | 0.0% | 1548 ms |
| xai | 100.0% | — | 0.0% | 777 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 120 | 116 | 4 | 0 | 96.6% | 3 min | 46 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 81 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 40 s | 35 min |
| openai | 144 | 131 | 3 | 10 | 84.4% | 67 s | 127 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
