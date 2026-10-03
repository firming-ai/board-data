# FILL — the inference availability index

*As of 2026-10-02T02:05:02+00:00 · probe pulse-1.4.2 · methodology 1.3.1*

*Published 2026-10-03T02:05:01+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-02/02.json`; their sha256 `d7a7406e97dc…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 96.3** · FILL·FLEX 100.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.7% | — | 85.4% (n=192) | 100.0% (n=30) |
| GEM·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.1% | 100.0% (n=32) | 88.3% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1245 ms |
| bedrock | 100.0% | — | 0.0% | 716 ms |
| deepseek | 100.0% | — | 0.0% | 1161 ms |
| gemini | 99.3% | 85.6% | 5.8% | 1005 ms |
| mistral | 100.0% | — | 0.0% | 740 ms |
| openai | 100.0% | 99.7% | 0.0% | 1000 ms |
| openrouter | 100.0% | — | 0.0% | 1455 ms |
| xai | 100.0% | — | 0.0% | 993 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 192 | 0 | 0 | 50.0% | 57.8% | 85.4% | — | — | 5 min | 73 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 117 s | 3 min |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 89.6% | 100.0% | — | — | 22 s | 19 min |
| openai | 240 | 216 | 0 | 24 | 63.3% | 73.3% | 89.2% | — | — | 98 s | 36 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
