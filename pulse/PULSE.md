# FILL — the inference availability index

*As of 2026-09-23T18:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T18:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/18.json`; their sha256 `1a6381c8896c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 82.0** · FILL·FLEX 58.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 94.2% | — | 88.4% (n=138) | 100.0% (n=30) |
| GEM·FILL | 64.7% | 29.4% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 87.0% | 84.2% (n=19) | 76.7% (n=180) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1216 ms |
| bedrock | 100.0% | — | 0.0% | 736 ms |
| deepseek | 100.0% | — | 0.0% | 1253 ms |
| gemini | 100.0% | 28.9% | 38.7% | 1228 ms |
| mistral | 100.0% | — | 0.0% | 754 ms |
| openai | 96.6% | 90.3% | 0.0% | 1163 ms |
| openrouter | 100.0% | — | 0.0% | 1906 ms |
| xai | 100.0% | — | 0.0% | 810 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 140 | 130 | 10 | 0 | 94.6% | 3 min | 60 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 95 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 52 s | 44 min |
| openai | 184 | 172 | 12 | 0 | 82.0% | 67 s | 146 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
