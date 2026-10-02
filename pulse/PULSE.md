# FILL — the inference availability index

*As of 2026-10-01T05:05:01+00:00 · probe pulse-1.3.1 · methodology 1.2.1*

*Published 2026-10-02T05:05:00+00:00 — the public board runs 24 h behind the tape. The live board and every lane are on the keyed feed. This hour's bytes are `pulse/hourly/2026-10-01/05.json`; their sha256 `08f83c7a77a2…` was signed and published at the hour in `pulse/commitments/`, so what appears here a day later is what was struck.*

**FILL 86.1** · FILL·FLEX 93.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 49.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 75.0% | — | 50.0% (n=192) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 92.2% | 100.0% (n=32) | 76.7% (n=236) | 100.0% (n=15) |


**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1567 ms |
| bedrock | 100.0% | — | 0.0% | 748 ms |
| deepseek | 100.0% | — | 0.0% | 1201 ms |
| gemini | 100.0% | 79.4% | 11.3% | 1091 ms |
| mistral | 100.0% | — | 0.0% | 758 ms |
| openai | 99.7% | 99.7% | 0.0% | 1084 ms |
| openrouter | 100.0% | — | 0.0% | 1573 ms |
| xai | 100.0% | — | 0.0% | 976 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 5 min | done in 10 min | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 192 | 191 | 1 | 0 | — | — | 53.9% | 40 min | 133 min |
| gemini | 48 | 48 | 0 | 0 | — | — | 100.0% | 2 min | 3 min |
| mistral | 48 | 48 | 0 | 0 | — | — | 100.0% | 23 s | 3 min |
| openai | 238 | 191 | 1 | 46 | — | — | 75.9% | 66 s | 70 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
