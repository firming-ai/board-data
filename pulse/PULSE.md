# FILL — the inference availability index

*As of 2026-10-02T17:05:01+00:00 · probe pulse-1.4.2 · methodology 1.3.1*

*Published 2026-10-03T17:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-02/17.json`; their sha256 `10a342e936b1…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 94.8** · FILL·FLEX 89.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=192) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 99.2% | 100.0% (n=32) | 97.5% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1418 ms |
| bedrock | 100.0% | — | 0.0% | 681 ms |
| deepseek | 100.0% | — | 0.0% | 1182 ms |
| gemini | 100.0% | 74.7% | 9.9% | 972 ms |
| mistral | 100.0% | — | 0.0% | 706 ms |
| openai | 98.7% | 99.0% | 0.0% | 1016 ms |
| openrouter | 100.0% | — | 0.0% | 1561 ms |
| xai | 100.0% | — | 0.0% | 937 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 192 | 0 | 0 | 96.9% | 99.5% | 100.0% | — | — | 2 min | 4 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 85.4% | 85.4% | 100.0% | — | — | 23 s | 22 min |
| openai | 240 | 239 | 1 | 0 | 79.1% | 83.7% | 97.5% | — | — | 67 s | 40 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
