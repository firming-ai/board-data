# FILL — the inference availability index

*As of 2026-09-29T19:05:03+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-09-30T19:05:02+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-09-29/19.json`; their sha256 `c0357eb1c5e3…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 89.0** · FILL·FLEX 80.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 36.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 86.6% | — | 73.2% (n=168) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 98.1% | 94.7% (n=19) | 99.5% (n=192) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1482 ms |
| bedrock | 87.5% | — | 12.5% | 769 ms |
| deepseek | 100.0% | — | 0.0% | 1218 ms |
| gemini | 100.0% | 63.9% | 18.6% | 979 ms |
| mistral | 100.0% | — | 0.0% | 724 ms |
| openai | 97.9% | 93.9% | 0.0% | 1299 ms |
| openrouter | 100.0% | — | 0.0% | 1657 ms |
| xai | 100.0% | — | 0.0% | 845 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 170 | 157 | 9 | 4 | 72.7% | 3 min | 83 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 0 | 1 | 97.9% | 35 s | 13 min |
| openai | 192 | 191 | 1 | 0 | 99.5% | 67 s | 27 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
