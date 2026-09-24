# FILL — the inference availability index

*As of 2026-09-23T17:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T17:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/17.json`; their sha256 `6532bcb5e355…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 78.4** · FILL·FLEX 47.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.5% | — | 89.0% (n=136) | 100.0% (n=30) |
| GEM·FILL | 55.9% | 11.8% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 84.7% | 79.0% (n=19) | 75.0% (n=176) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1312 ms |
| bedrock | 100.0% | — | 0.0% | 764 ms |
| deepseek | 100.0% | — | 0.0% | 1291 ms |
| gemini | 100.0% | 22.2% | 39.8% | 1199 ms |
| mistral | 100.0% | — | 0.0% | 786 ms |
| openai | 97.5% | 91.2% | 0.0% | 1270 ms |
| openrouter | 100.0% | — | 0.0% | 1824 ms |
| xai | 100.0% | — | 0.0% | 881 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 138 | 127 | 11 | 0 | 96.1% | 3 min | 47 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 94 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 52 s | 44 min |
| openai | 180 | 166 | 14 | 0 | 83.1% | 67 s | 141 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
