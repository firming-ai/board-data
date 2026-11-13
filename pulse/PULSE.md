# FILL — the inference availability index

*As of 2026-11-12T20:05:14+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-13T20:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-12/20.json`; their sha256 `28c299638792…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 87.2** · FILL·FLEX 74.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 51.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=312) | 100.0% (n=30) |
| GEM·FILL | 68.4% | 36.8% (n=19) | 100.0% (n=144) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 93.1% | 96.9% (n=32) | 82.4% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1162 ms |
| bedrock | 100.0% | — | 0.0% | 704 ms |
| deepseek | 100.0% | — | 0.0% | 1333 ms |
| gemini | 99.4% | 55.5% | 18.1% | 1479 ms |
| mistral | 50.0% | — | 0.0% | 890 ms |
| openai | 99.8% | 96.1% | 0.0% | 1174 ms |
| openrouter | 100.0% | — | 0.0% | 1605 ms |
| xai | 100.0% | — | 0.0% | 876 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 312 | 312 | 0 | 0 | 98.4% | 99.7% | 100.0% | 100.0% | 100.0% | 104 s | 3 min |
| gemini | 144 | 143 | 1 | 0 | 95.1% | 96.5% | 100.0% | 100.0% | 100.0% | 2 min | 4 min |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 95.8% | 100.0% | 100.0% | 100.0% | 38 s | 2 min |
| openai | 312 | 285 | 27 | 0 | 81.1% | 83.5% | 89.5% | 84.6% | 100.0% | 67 s | 568 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
