# FILL — the inference availability index

*As of 2026-10-01T20:05:02+00:00 · probe pulse-1.4.1 · methodology 1.3.1*

*Published 2026-10-02T20:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/20.json`; their sha256 `a83ae8712db4…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 92.6** · FILL·FLEX 93.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 92.7% | — | 85.4% (n=192) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 93.8% | 100.0% (n=32) | 81.2% (n=240) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1618 ms |
| bedrock | 100.0% | — | 0.0% | 781 ms |
| deepseek | 71.2% | — | 0.0% | 1742 ms |
| gemini | 100.0% | 73.7% | 13.1% | 1175 ms |
| mistral | 100.0% | — | 0.0% | 828 ms |
| openai | 99.7% | 99.5% | 0.0% | 1164 ms |
| openrouter | 100.0% | — | 0.0% | 1638 ms |
| xai | 100.0% | — | 0.0% | 1057 ms |

**Batch** — one one-request job per lane every 30 min, polled to its end. Counts and minute/hour columns cover the last 24 h of submits; 4 h and 24 h percentages use separate mature 24-hour cohorts ending 4 h and 24 h ago.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | done in 4 h | done in 24 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 192 | 0 | 0 | 46.4% | 57.3% | 85.4% | — | — | 6 min | 73 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 100.0% | 100.0% | — | — | 119 s | 3 min |
| mistral | 48 | 47 | 1 | 0 | 89.4% | 89.4% | 100.0% | — | — | 22 s | 19 min |
| openai | 240 | 199 | 5 | 36 | 61.7% | 70.2% | 83.4% | — | — | 84 s | 32 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
