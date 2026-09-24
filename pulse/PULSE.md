# FILL — the inference availability index

*As of 2026-09-23T03:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T03:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/03.json`; their sha256 `ca47fd2efda8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.6** · FILL·FLEX 94.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.2% | — | 94.4% (n=108) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 92.5% | 100.0% (n=19) | 77.5% (n=120) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1273 ms |
| bedrock | 100.0% | — | 0.0% | 716 ms |
| deepseek | 100.0% | — | 0.0% | 1208 ms |
| gemini | 100.0% | 90.7% | 5.2% | 970 ms |
| mistral | 100.0% | — | 0.0% | 677 ms |
| openai | 96.6% | 95.6% | 0.0% | 993 ms |
| openrouter | 100.0% | — | 0.0% | 1479 ms |
| xai | 100.0% | — | 0.0% | 857 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 110 | 108 | 2 | 0 | 94.4% | 3 min | 61 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 50 s | 35 min |
| openai | 124 | 114 | 0 | 10 | 79.8% | 70 s | 130 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
