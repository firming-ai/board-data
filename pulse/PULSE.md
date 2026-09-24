# FILL — the inference availability index

*As of 2026-09-23T11:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T11:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/11.json`; their sha256 `9a03c8a98323…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.4** · FILL·FLEX 86.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 96.8% | — | 93.5% (n=124) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 86.2% | 79.0% (n=19) | 79.6% (n=152) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1412 ms |
| bedrock | 100.0% | — | 0.0% | 731 ms |
| deepseek | 100.0% | — | 0.0% | 1273 ms |
| gemini | 100.0% | 83.5% | 8.4% | 1080 ms |
| mistral | 100.0% | — | 0.0% | 745 ms |
| openai | 94.5% | 77.6% | 0.0% | 1091 ms |
| openrouter | 100.0% | — | 0.0% | 1628 ms |
| xai | 100.0% | — | 0.0% | 825 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 126 | 120 | 6 | 0 | 96.7% | 3 min | 45 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 86 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 55 s | 44 min |
| openai | 156 | 138 | 8 | 10 | 82.4% | 67 s | 127 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
