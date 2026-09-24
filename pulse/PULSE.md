# FILL — the inference availability index

*As of 2026-09-23T13:05:02+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T13:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/13.json`; their sha256 `d156f1e50b3d…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 85.0** · FILL·FLEX 63.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.5% | — | 93.0% (n=128) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 85.1% | 79.0% (n=19) | 76.2% (n=160) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1753 ms |
| bedrock | 100.0% | — | 0.0% | 767 ms |
| deepseek | 100.0% | — | 0.0% | 1319 ms |
| gemini | 100.0% | 67.5% | 16.3% | 1118 ms |
| mistral | 100.0% | — | 0.0% | 987 ms |
| openai | 95.3% | 91.7% | 0.0% | 1136 ms |
| openrouter | 100.0% | — | 0.0% | 1749 ms |
| xai | 100.0% | — | 0.0% | 895 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 130 | 124 | 6 | 0 | 96.0% | 3 min | 44 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 86 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 52 s | 44 min |
| openai | 164 | 142 | 12 | 10 | 80.3% | 67 s | 135 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
