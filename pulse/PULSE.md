# FILL — the inference availability index

*As of 2026-11-07T21:05:03+00:00 · probe pulse-1.5.1 · methodology 1.4.0*

*Published 2026-11-08T21:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-11-07/21.json`; their sha256 `5080d44bf36e…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.0** · FILL·FLEX 88.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 50.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=264) | 100.0% (n=30) |
| GEM·FILL | 83.3% | 66.7% (n=18) | 100.0% (n=96) | — |
| MIS·FILL | 95.8% | — | 95.8% (n=48) | — |
| OAI·FILL | 95.6% | 100.0% (n=32) | 86.9% (n=312) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1304 ms |
| bedrock | 82.8% | — | 17.2% | 786 ms |
| deepseek | 100.0% | — | 0.0% | 1201 ms |
| gemini | 100.0% | 70.9% | 5.7% | 1042 ms |
| mistral | 100.0% | — | 0.0% | 777 ms |
| openai | 100.0% | 97.7% | 0.0% | 933 ms |
| openrouter | 100.0% | — | 0.0% | 1319 ms |
| xai | 100.0% | — | 0.0% | 774 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 264 | 262 | 2 | 0 | 96.6% | 98.1% | 100.0% | 100.0% | 100.0% | 92 s | 3 min |
| gemini | 96 | 96 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 97.9% | 2 min | 4 min |
| mistral | 48 | 48 | 0 | 0 | 93.8% | 93.8% | 100.0% | 95.8% | 100.0% | 58 s | 14 min |
| openai | 312 | 300 | 12 | 0 | 83.7% | 85.3% | 90.0% | 89.7% | 100.0% | 66 s | 319 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
