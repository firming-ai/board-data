# FILL — the inference availability index

*As of 2026-10-08T11:05:13+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-09T11:05:12+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-08/11.json`; their sha256 `0c4092e376c2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 93.7** · FILL·FLEX 85.7

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.3% | — | 98.7% (n=224) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.5% | 87.5% (n=32) | 84.1% (n=264) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1154 ms |
| bedrock | 100.0% | — | 0.0% | 729 ms |
| deepseek | 100.0% | — | 0.0% | 1206 ms |
| gemini | 100.0% | 85.0% | 7.6% | 890 ms |
| mistral | 100.0% | — | 0.0% | 731 ms |
| openai | 99.7% | 86.7% | 0.0% | 1058 ms |
| openrouter | 100.0% | — | 0.0% | 1458 ms |
| xai | 0.0% | — | 0.0% | — ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 226 | 220 | 6 | 0 | 76.8% | 85.0% | 98.6% | 100.0% | 100.0% | 3 min | 17 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | 93.8% | 97.9% | 100.0% | 100.0% | 100.0% | 22 s | 4 min |
| openai | 264 | 258 | 6 | 0 | 79.5% | 82.2% | 86.0% | 93.2% | 99.6% | 67 s | 223 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
