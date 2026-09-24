# FILL — the inference availability index

*As of 2026-09-23T22:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T22:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/22.json`; their sha256 `4ed64c2f9f02…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.1** · FILL·FLEX 86.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.1% | — | 88.2% (n=144) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 91.0% | 94.7% (n=19) | 78.1% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1243 ms |
| bedrock | 100.0% | — | 0.0% | 711 ms |
| deepseek | 100.0% | — | 0.0% | 1301 ms |
| gemini | 99.3% | 68.0% | 18.3% | 1040 ms |
| mistral | 100.0% | — | 0.0% | 748 ms |
| openai | 97.5% | 90.3% | 0.0% | 1104 ms |
| openrouter | 100.0% | — | 0.0% | 1634 ms |
| xai | 100.0% | — | 0.0% | 812 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 142 | 2 | 0 | 89.4% | 4 min | 239 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 96 s | 2 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 39 s | 41 min |
| openai | 192 | 189 | 3 | 0 | 79.9% | 67 s | 279 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
