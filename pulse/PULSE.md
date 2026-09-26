# FILL — the inference availability index

*As of 2026-09-25T06:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-26T06:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-25/06.json`; their sha256 `af6fc3090d90…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 90.5** · FILL·FLEX 77.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.3% | — | 98.6% (n=144) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 89.9% | 89.5% (n=19) | 80.2% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1509 ms |
| bedrock | 100.0% | — | 0.0% | 734 ms |
| deepseek | 100.0% | — | 0.0% | 1243 ms |
| gemini | 100.0% | 70.1% | 16.9% | 1072 ms |
| mistral | 100.0% | — | 0.0% | 720 ms |
| openai | 96.6% | 95.2% | 0.0% | 1122 ms |
| openrouter | 100.0% | — | 0.0% | 1555 ms |
| xai | 100.0% | — | 0.0% | 845 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 144 | 143 | 1 | 0 | 99.3% | 116 s | 11 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 8 min |
| openai | 192 | 191 | 1 | 0 | 80.1% | 89 s | 485 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
