# FILL — the inference availability index

*As of 2026-10-06T10:05:01+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-07T10:05:04+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-06/10.json`; their sha256 `3826fc70aa84…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.7** · FILL·FLEX 81.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=216) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.6% | 90.6% (n=32) | 96.2% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1283 ms |
| bedrock | 98.4% | — | 1.6% | 708 ms |
| deepseek | 100.0% | — | 0.0% | 1263 ms |
| gemini | 100.0% | 73.2% | 13.7% | 983 ms |
| mistral | 100.0% | — | 0.0% | 821 ms |
| openai | 99.5% | 90.9% | 0.0% | 1119 ms |
| openrouter | 100.0% | — | 0.0% | 1530 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 216 | 212 | 4 | 0 | 90.6% | 99.1% | 100.0% | 100.0% | 100.0% | 2 min | 5 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 100.0% | 100.0% | 100.0% | 100.0% | 33 s | 4 min |
| openai | 264 | 260 | 4 | 0 | 82.3% | 86.2% | 96.2% | 98.9% | 100.0% | 65 s | 42 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
