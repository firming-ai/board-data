# FILL — the inference availability index

*As of 2026-09-22T19:05:01+00:00 · probe pulse-1.3.0 · methodology 1.2.1*

*Published 2026-09-22T19:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-22/19.json`; their sha256 `ef0b84c636e1…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.1** · FILL·FLEX 70.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.4% | — | 94.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 90.3% | 100.0% (n=17) | 70.8% (n=96) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1138 ms |
| deepseek | 100.0% | — | 0.0% | 1093 ms |
| gemini | 100.0% | 53.9% | 24.5% | 981 ms |
| mistral | 100.0% | — | 0.0% | 651 ms |
| openai | 100.0% | 100.0% | 0.0% | 1089 ms |
| openrouter | 100.0% | — | 0.0% | 1521 ms |
| xai | 100.0% | — | 0.0% | 767 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 94.8% | 2 min | 55 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 115 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 44 s | 24 min |
| openai | 96 | 83 | 3 | 10 | 73.1% | 96 s | 113 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
