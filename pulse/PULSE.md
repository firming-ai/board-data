# FILL — the inference availability index

*As of 2026-09-29T09:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-30T09:05:02+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-29/09.json`; their sha256 `0bb6969c3043…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.7** · FILL·FLEX 69.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.3% | — | 92.6% (n=148) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.3% | 89.5% (n=19) | 99.5% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1631 ms |
| bedrock | 89.1% | — | 10.9% | 697 ms |
| deepseek | 100.0% | — | 0.0% | 1189 ms |
| gemini | 100.0% | 60.8% | 20.4% | 981 ms |
| mistral | 100.0% | — | 0.0% | 745 ms |
| openai | 97.9% | 86.0% | 0.0% | 991 ms |
| openrouter | 100.0% | — | 0.0% | 1612 ms |
| xai | 100.0% | — | 0.0% | 828 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 150 | 150 | 0 | 0 | 94.0% | 2 min | 129 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 100.0% | 25 s | 5 min |
| openai | 192 | 192 | 0 | 0 | 99.5% | 67 s | 25 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
