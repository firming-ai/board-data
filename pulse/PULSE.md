# FILL — the inference availability index

*As of 2026-09-23T12:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-24T12:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-23/12.json`; their sha256 `985195874f59…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.1** · FILL·FLEX 69.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.2% | — | 94.4% (n=126) | 100.0% (n=30) |
| GEM·FILL | 76.5% | 52.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 87.5% | 84.2% (n=19) | 78.2% (n=156) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1596 ms |
| bedrock | 100.0% | — | 0.0% | 731 ms |
| deepseek | 100.0% | — | 0.0% | 1265 ms |
| gemini | 100.0% | 75.3% | 12.2% | 1089 ms |
| mistral | 100.0% | — | 0.0% | 761 ms |
| openai | 92.4% | 84.2% | 0.0% | 1032 ms |
| openrouter | 100.0% | — | 0.0% | 1583 ms |
| xai | 100.0% | — | 0.0% | 823 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 128 | 123 | 5 | 0 | 95.9% | 3 min | 44 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 55 s | 44 min |
| openai | 160 | 140 | 10 | 10 | 81.3% | 67 s | 135 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
