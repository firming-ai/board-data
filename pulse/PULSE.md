# FILL — the inference availability index

*As of 2026-10-01T21:05:02+00:00 · probe pulse-1.4.1 · methodology 1.3.1*

*Published 2026-10-02T21:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/21.json`; their sha256 `a75301342508…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 88.8** · FILL·FLEX 85.7

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.7% | — | 85.4% (n=192) | 100.0% (n=30) |
| GEM·FILL | 79.4% | 58.8% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 94.4% | 100.0% (n=32) | 83.3% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1536 ms |
| bedrock | 100.0% | — | 0.0% | 736 ms |
| deepseek | 45.5% | — | 0.0% | 6267 ms |
| gemini | 100.0% | 67.5% | 17.7% | 1115 ms |
| mistral | 100.0% | — | 0.0% | 796 ms |
| openai | 100.0% | 99.7% | 0.0% | 1137 ms |
| openrouter | 100.0% | — | 0.0% | 1564 ms |
| xai | 100.0% | — | 0.0% | 995 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 191 | 1 | 0 | 47.1% | 57.6% | 85.3% | — | — | 6 min | 73 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 119 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 89.6% | 100.0% | — | — | 22 s | 19 min |
| openai | 240 | 205 | 1 | 34 | 61.5% | 70.7% | 84.5% | — | — | 88 s | 37 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
