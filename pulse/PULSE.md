# FILL — the inference availability index

*As of 2026-09-23T20:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T20:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/20.json`; their sha256 `ee10e814bfb7…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 81.9** · FILL·FLEX 58.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.0% | — | 88.0% (n=142) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 87.1% | 84.2% (n=19) | 77.1% (n=188) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1265 ms |
| bedrock | 100.0% | — | 0.0% | 743 ms |
| deepseek | 100.0% | — | 0.0% | 1189 ms |
| gemini | 100.0% | 39.7% | 34.0% | 1122 ms |
| mistral | 99.2% | — | 0.8% | 784 ms |
| openai | 97.5% | 81.6% | 0.0% | 1306 ms |
| openrouter | 100.0% | — | 0.0% | 1739 ms |
| xai | 100.0% | — | 0.0% | 877 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 141 | 3 | 0 | 89.4% | 4 min | 178 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 95 s | 119 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 40 s | 44 min |
| openai | 192 | 186 | 6 | 0 | 80.6% | 67 s | 282 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
