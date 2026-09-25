# FILL — the inference availability index

*As of 2026-09-24T04:05:12+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-25T04:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-24/04.json`; their sha256 `4ba82e4726b8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.5** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 93.8% | — | 87.5% (n=144) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.2% | 89.5% (n=19) | 78.1% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1398 ms |
| bedrock | 100.0% | — | 0.0% | 716 ms |
| deepseek | 100.0% | — | 0.0% | 1147 ms |
| gemini | 99.3% | 74.2% | 14.8% | 1055 ms |
| mistral | 100.0% | — | 0.0% | 710 ms |
| openai | 98.7% | 97.8% | 0.0% | 970 ms |
| openrouter | 100.0% | — | 0.0% | 1401 ms |
| xai | 100.0% | — | 0.0% | 808 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 87.5% | 3 min | 254 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 105 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 35 s | 9 min |
| openai | 192 | 192 | 0 | 0 | 78.6% | 68 s | 276 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
