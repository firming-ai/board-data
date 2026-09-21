# FILL — the inference availability index

*As of 2026-09-21T23:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 94.5** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 89.6% | — | 89.6% (n=48) | — |
| OAI·FILL | 89.3% | 82.3% (n=17) | 85.4% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1580 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 848 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 743 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1235 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1306 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1788 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1452 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1312 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1136 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1352 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4381 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3075 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 828 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 812 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 7608 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1034 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1914 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 3467 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1384 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3344 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1306 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 623 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1346 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1270 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1180 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1048 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 60.0% | 0.0% | 5796 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 739 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 802 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 91.7% | 0.0% | 1228 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 978 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 796 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1296 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1273 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1778 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1421 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1681 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1223 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1393 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1218 ms |
| deepseek | 100.0% | — | 0.0% | 1159 ms |
| gemini | 100.0% | 88.7% | 6.4% | 983 ms |
| mistral | 100.0% | — | 0.0% | 687 ms |
| openai | 99.5% | 84.3% | 0.0% | 958 ms |
| openrouter | 100.0% | — | 0.0% | 1412 ms |
| xai | 100.0% | — | 0.0% | 774 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 96 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 78 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 42 s | 116 min |
| openai | 96 | 92 | 4 | 0 | 88.0% | 80 s | 131 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
