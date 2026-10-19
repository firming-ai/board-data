# FILL — the inference availability index

*As of 2026-10-18T00:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-19T00:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-18/00.json`; their sha256 `1b62380e57db…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.3** · FILL·FLEX 88.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 86.1% | 72.2% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 96.7% | 96.9% (n=32) | 100.0% (n=264) | 93.3% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 890 ms |
| bedrock | 100.0% | — | 0.0% | 736 ms |
| deepseek | 100.0% | — | 0.0% | 1182 ms |
| gemini | 100.0% | 63.1% | 20.4% | 1100 ms |
| mistral | 100.0% | — | 0.0% | 631 ms |
| openai | 100.0% | 97.1% | 0.0% | 986 ms |
| openrouter | 100.0% | — | 0.0% | 1250 ms |
| xai | 100.0% | — | 0.0% | 792 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 264 | 0 | 0 | 98.1% | 100.0% | 100.0% | 100.0% | 100.0% | 106 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 45 | 3 | 0 | 80.0% | 82.2% | 84.4% | 97.9% | 100.0% | 24 s | 175 min |
| openai | 264 | 263 | 1 | 0 | 92.8% | 93.9% | 100.0% | 100.0% | 100.0% | 50 s | 11 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
