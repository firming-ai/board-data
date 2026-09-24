# FILL — the inference availability index

*As of 2026-09-23T01:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T01:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/01.json`; their sha256 `e05b8f2e5da4…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.8** · FILL·FLEX 86.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.6% | — | 93.3% (n=104) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 87.6% | 89.5% (n=19) | 73.2% (n=112) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1211 ms |
| bedrock | 100.0% | — | 0.0% | 711 ms |
| deepseek | 100.0% | — | 0.0% | 1131 ms |
| gemini | 100.0% | 83.5% | 9.0% | 979 ms |
| mistral | 100.0% | — | 0.0% | 650 ms |
| openai | 97.9% | 95.6% | 0.0% | 966 ms |
| openrouter | 100.0% | — | 0.0% | 1521 ms |
| xai | 100.0% | — | 0.0% | 731 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 106 | 105 | 1 | 0 | 94.3% | 2 min | 63 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 45 s | 35 min |
| openai | 116 | 104 | 2 | 10 | 75.4% | 70 s | 134 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
