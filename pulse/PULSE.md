# FILL — the inference availability index

*As of 2026-09-21T03:05:12+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.0** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 99.7% | 100.0% (n=17) | 99.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1319 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 799 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2517 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1240 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1500 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2053 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1785 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1213 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1030 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1196 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3278 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2777 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 781 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 8308 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 987 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1887 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 2799 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1296 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 2424 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1275 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 574 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1118 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1078 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1206 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 901 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 672 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 71.7% | 0.0% | 1206 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 941 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 716 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1120 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1230 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1728 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1506 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 98.3% | 0.0% | 1865 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 945 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1432 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1270 ms |
| deepseek | 100.0% | — | 0.0% | 1131 ms |
| gemini | 100.0% | 84.5% | 8.7% | 947 ms |
| mistral | 100.0% | — | 0.0% | 622 ms |
| openai | 100.0% | 91.2% | 0.0% | 846 ms |
| openrouter | 99.4% | — | 0.0% | 1407 ms |
| xai | 100.0% | — | 0.0% | 726 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 78 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 24 s | 211 min |
| openai | 96 | 94 | 2 | 0 | 98.9% | 68 s | 28 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
