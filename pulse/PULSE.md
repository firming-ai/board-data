# FILL — the inference availability index

*As of 2026-09-24T10:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T10:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/10.json`; their sha256 `305bebf0241c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.2** · FILL·FLEX 80.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.8% | — | 89.6% (n=144) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.6% | 89.5% (n=19) | 82.3% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1552 ms |
| bedrock | 100.0% | — | 0.0% | 726 ms |
| deepseek | 100.0% | — | 0.0% | 1211 ms |
| gemini | 99.3% | 67.5% | 18.6% | 1034 ms |
| mistral | 100.0% | — | 0.0% | 767 ms |
| openai | 98.7% | 89.0% | 0.0% | 1007 ms |
| openrouter | 100.0% | — | 0.0% | 1589 ms |
| xai | 100.0% | — | 0.0% | 846 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 90.3% | 2 min | 170 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 112 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 36 s | 5 min |
| openai | 192 | 189 | 3 | 0 | 83.6% | 67 s | 240 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
