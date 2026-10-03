# FILL — the inference availability index

*As of 2026-10-02T00:05:13+00:00 · probe pulse-1.4.1 · methodology 1.3.1*

*Published 2026-10-03T00:05:06+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-02/00.json`; their sha256 `446744ba6cc8…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 91.2** · FILL·FLEX 89.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.7% | — | 85.4% (n=192) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 95.6% | 100.0% (n=32) | 86.7% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1357 ms |
| bedrock | 98.4% | — | 1.6% | 757 ms |
| deepseek | 100.0% | — | 0.0% | 1233 ms |
| gemini | 100.0% | 85.0% | 7.8% | 1096 ms |
| mistral | 100.0% | — | 0.0% | 761 ms |
| openai | 99.7% | 99.2% | 0.0% | 1066 ms |
| openrouter | 100.0% | — | 0.0% | 1482 ms |
| xai | 98.7% | — | 0.0% | 1074 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 192 | 0 | 0 | 47.4% | 57.8% | 85.4% | — | — | 6 min | 73 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 118 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 89.6% | 100.0% | — | — | 22 s | 19 min |
| openai | 240 | 212 | 0 | 28 | 62.5% | 71.7% | 87.5% | — | — | 95 s | 36 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
