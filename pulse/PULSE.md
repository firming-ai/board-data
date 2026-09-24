# FILL — the inference availability index

*As of 2026-09-23T02:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T02:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/02.json`; their sha256 `33b8db6c4366…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 95.5** · FILL·FLEX 97.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.7% | — | 93.4% (n=106) | 100.0% (n=30) |
| GEM·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 89.9% | 94.7% (n=19) | 75.0% (n=116) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1273 ms |
| bedrock | 100.0% | — | 0.0% | 699 ms |
| deepseek | 100.0% | — | 0.0% | 1170 ms |
| gemini | 100.0% | 82.0% | 10.2% | 976 ms |
| mistral | 100.0% | — | 0.0% | 668 ms |
| openai | 95.3% | 93.0% | 0.0% | 995 ms |
| openrouter | 100.0% | — | 0.0% | 1521 ms |
| xai | 97.4% | — | 0.0% | 850 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 108 | 105 | 3 | 0 | 94.3% | 2 min | 63 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 113 s |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 50 s | 35 min |
| openai | 120 | 109 | 1 | 10 | 78.2% | 70 s | 133 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
