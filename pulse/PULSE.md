# FILL — the inference availability index

*As of 2026-09-19T15:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.5** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=64) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=32) | — |
| MIS·FILL | 96.9% | — | 96.9% (n=32) | — |
| OAI·FILL | 98.4% | 100.0% (n=17) | 95.3% (n=64) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1767 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 883 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 754 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1599 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1225 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 3175 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2094 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1778 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1314 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1067 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1309 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 2984 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3143 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 823 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 792 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 7716 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1708 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 53.3% | 46.7% | 5558 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1322 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3412 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1518 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1192 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1129 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1854 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 726 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 697 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 98.3% | 0.0% | 1265 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 993 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 820 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1040 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 826 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1268 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1273 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1555 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1674 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1019 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1485 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1263 ms |
| deepseek | 100.0% | — | 0.0% | 1206 ms |
| gemini | 100.0% | 84.2% | 8.9% | 966 ms |
| mistral | 100.0% | — | 0.0% | 689 ms |
| openai | 100.0% | 99.0% | 0.0% | 869 ms |
| openrouter | 100.0% | — | 0.0% | 1379 ms |
| xai | 100.0% | — | 0.0% | 758 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 68 | 68 | 0 | 0 | 100.0% | 93 s | 2 min |
| gemini | 34 | 34 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 34 | 34 | 0 | 0 | 97.1% | 34 s | 4 min |
| openai | 68 | 67 | 1 | 0 | 95.5% | 67 s | 51 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
