# FILL — the inference availability index

*As of 2026-09-25T01:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-26T01:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-25/01.json`; their sha256 `25ec8dccd8d4…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.3** · FILL·FLEX 86.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=144) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 91.7% | 94.7% (n=19) | 80.2% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1438 ms |
| bedrock | 100.0% | — | 0.0% | 733 ms |
| deepseek | 100.0% | — | 0.0% | 1263 ms |
| gemini | 100.0% | 70.1% | 15.1% | 1028 ms |
| mistral | 100.0% | — | 0.0% | 767 ms |
| openai | 98.3% | 93.9% | 0.0% | 1166 ms |
| openrouter | 100.0% | — | 0.0% | 1691 ms |
| xai | 100.0% | — | 0.0% | 835 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 144 | 0 | 0 | 100.0% | 116 s | 10 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 8 min |
| openai | 192 | 183 | 9 | 0 | 83.1% | 72 s | 511 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
