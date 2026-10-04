# FILL — the inference availability index

*As of 2026-10-03T10:05:02+00:00 · probe pulse-1.5.0 · methodology 1.4.0*

*Published 2026-10-04T10:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-03/10.json`; their sha256 `4aab2355d48f…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 99.6** · FILL·FLEX 100.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=204) | 100.0% (n=30) |
| GEM·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.8% | 100.0% (n=32) | 96.4% (n=252) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1111 ms |
| bedrock | 100.0% | — | 0.0% | 707 ms |
| deepseek | 100.0% | — | 0.0% | 1196 ms |
| gemini | 100.0% | 87.1% | 7.3% | 995 ms |
| mistral | 100.0% | — | 0.0% | 710 ms |
| openai | 100.0% | 99.2% | 0.0% | 961 ms |
| openrouter | 100.0% | — | 0.0% | 1441 ms |
| xai | 100.0% | — | 0.0% | 899 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 205 | 205 | 0 | 0 | 97.1% | 100.0% | 100.0% | 100.0% | 100.0% | 2 min | 5 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 118 s | 3 min |
| mistral | 48 | 47 | 1 | 0 | 89.4% | 93.6% | 100.0% | 100.0% | 100.0% | 31 s | 18 min |
| openai | 253 | 253 | 0 | 0 | 85.8% | 89.7% | 96.8% | 99.6% | 96.7% | 57 s | 27 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
