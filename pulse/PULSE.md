# FILL — the inference availability index

*As of 2026-09-23T06:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T06:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/06.json`; their sha256 `a156934c681c…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.1** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.8% | — | 95.6% (n=114) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 87.2% | 79.0% (n=19) | 82.6% (n=132) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1296 ms |
| bedrock | 100.0% | — | 0.0% | 692 ms |
| deepseek | 100.0% | — | 0.0% | 1194 ms |
| gemini | 100.0% | 78.9% | 11.9% | 952 ms |
| mistral | 100.0% | — | 0.0% | 654 ms |
| openai | 94.9% | 92.5% | 0.0% | 949 ms |
| openrouter | 100.0% | — | 0.0% | 1491 ms |
| xai | 98.7% | — | 0.0% | 1194 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 116 | 113 | 3 | 0 | 95.6% | 3 min | 52 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 45 s | 35 min |
| openai | 136 | 125 | 1 | 10 | 83.0% | 67 s | 127 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
