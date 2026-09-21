# FILL — the inference availability index

*As of 2026-09-21T11:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.3** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 79.2% | — | 79.2% (n=48) | — |
| OAI·FILL | 88.8% | 70.6% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1482 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 850 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 788 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1447 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1230 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1865 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2115 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1828 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1145 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1003 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1330 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 5287 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2873 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 841 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 821 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 6995 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 987 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1694 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 48.3% | 50.0% | 5019 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1485 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3118 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1398 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 524 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 635 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1040 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1314 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1255 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 730 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 826 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 10.0% | 0.0% | 14115 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1373 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 825 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 884 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1327 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 3002 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1876 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1491 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1691 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1140 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1312 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1338 ms |
| deepseek | 100.0% | — | 0.0% | 1145 ms |
| gemini | 100.0% | 83.0% | 9.3% | 958 ms |
| mistral | 100.0% | — | 0.0% | 613 ms |
| openai | 100.0% | 72.5% | 0.0% | 1011 ms |
| openrouter | 100.0% | — | 0.0% | 1407 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 106 s |
| mistral | 48 | 44 | 4 | 0 | 81.8% | 36 s | 217 min |
| openai | 96 | 95 | 1 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
