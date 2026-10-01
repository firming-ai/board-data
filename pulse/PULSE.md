# FILL — the inference availability index

*As of 2026-09-30T05:05:12+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-01T05:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-30/05.json`; their sha256 `66965fc987d4…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.8** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 80.6% | — | 61.2% (n=188) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 94.6% | 84.2% (n=19) | 99.5% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1608 ms |
| bedrock | 100.0% | — | 0.0% | 718 ms |
| deepseek | 100.0% | — | 0.0% | 1161 ms |
| gemini | 99.3% | 82.5% | 10.2% | 1003 ms |
| mistral | 100.0% | — | 0.0% | 657 ms |
| openai | 94.9% | 83.8% | 0.0% | 997 ms |
| openrouter | 100.0% | — | 0.0% | 1552 ms |
| xai | 100.0% | — | 0.0% | 853 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 190 | 170 | 16 | 4 | 62.6% | 32 min | 103 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 32 s | 13 min |
| openai | 192 | 192 | 0 | 0 | 99.5% | 67 s | 22 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
