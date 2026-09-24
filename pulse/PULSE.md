# FILL — the inference availability index

*As of 2026-09-23T16:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T16:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/16.json`; their sha256 `b89cfdb118d3…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 82.8** · FILL·FLEX 61.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.8% | — | 89.5% (n=134) | 100.0% (n=30) |
| GEM·FILL | 67.6% | 35.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 86.0% | 84.2% (n=19) | 73.8% (n=172) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1330 ms |
| bedrock | 100.0% | — | 0.0% | 757 ms |
| deepseek | 100.0% | — | 0.0% | 1268 ms |
| gemini | 98.7% | 35.6% | 32.6% | 1161 ms |
| mistral | 100.0% | — | 0.0% | 830 ms |
| openai | 97.9% | 89.0% | 0.0% | 1299 ms |
| openrouter | 100.0% | — | 0.0% | 1806 ms |
| xai | 100.0% | — | 0.0% | 850 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 136 | 124 | 12 | 0 | 96.0% | 3 min | 44 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 94 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 54 s | 44 min |
| openai | 176 | 155 | 17 | 4 | 83.0% | 67 s | 137 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
