# FILL — the inference availability index

*As of 2026-09-23T19:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T19:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/19.json`; their sha256 `3e0d648ce1c8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 81.6** · FILL·FLEX 55.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 93.9% | — | 87.9% (n=140) | 100.0% (n=30) |
| GEM·FILL | 67.6% | 35.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 83.4% | 73.7% (n=19) | 76.6% (n=184) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1223 ms |
| bedrock | 100.0% | — | 0.0% | 736 ms |
| deepseek | 100.0% | — | 0.0% | 1230 ms |
| gemini | 100.0% | 39.7% | 34.0% | 1104 ms |
| mistral | 100.0% | — | 0.0% | 745 ms |
| openai | 94.5% | 88.6% | 0.0% | 1275 ms |
| openrouter | 100.0% | — | 0.0% | 1698 ms |
| xai | 100.0% | — | 0.0% | 840 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 142 | 138 | 4 | 0 | 90.6% | 4 min | 130 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 95 s | 119 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 43 s | 44 min |
| openai | 188 | 179 | 9 | 0 | 80.4% | 67 s | 270 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
