# FILL — the inference availability index

*As of 2026-09-23T21:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T21:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/21.json`; their sha256 `fecdd4ede20d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.4** · FILL·FLEX 75.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.1% | — | 88.2% (n=144) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 85.7% | 79.0% (n=19) | 78.1% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1255 ms |
| bedrock | 100.0% | — | 0.0% | 724 ms |
| deepseek | 100.0% | — | 0.0% | 1233 ms |
| gemini | 100.0% | 48.5% | 28.2% | 1063 ms |
| mistral | 100.0% | — | 0.0% | 733 ms |
| openai | 97.0% | 83.8% | 0.0% | 1180 ms |
| openrouter | 100.0% | — | 0.0% | 1728 ms |
| xai | 100.0% | — | 0.0% | 804 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 142 | 2 | 0 | 88.7% | 4 min | 239 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 95 s | 2 min |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 40 s | 41 min |
| openai | 192 | 187 | 5 | 0 | 79.7% | 67 s | 281 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
