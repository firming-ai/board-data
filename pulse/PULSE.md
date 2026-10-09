# FILL — the inference availability index

*As of 2026-10-08T08:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-09T08:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-08/08.json`; their sha256 `6d67c705ca37…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.9** · FILL·FLEX 87.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.3% | — | 98.6% (n=218) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 93.9% | 100.0% (n=32) | 81.8% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1034 ms |
| bedrock | 100.0% | — | 0.0% | 717 ms |
| deepseek | 100.0% | — | 0.0% | 1228 ms |
| gemini | 100.0% | 82.5% | 6.1% | 952 ms |
| mistral | 100.0% | — | 0.0% | 755 ms |
| openai | 99.7% | 100.0% | 0.0% | 1092 ms |
| openrouter | 100.0% | — | 0.0% | 1586 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 220 | 215 | 5 | 0 | 87.9% | 93.5% | 99.1% | 100.0% | 100.0% | 3 min | 10 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 93.8% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 4 min |
| openai | 264 | 257 | 7 | 0 | 78.2% | 80.2% | 83.7% | 93.2% | 99.6% | 67 s | 283 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
