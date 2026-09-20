# FILL — the inference availability index

*As of 2026-09-20T13:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.1** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1785 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 794 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1270 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1159 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1634 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2099 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1778 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1175 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1278 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 5151 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 4209 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 789 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 769 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 7094 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 983 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2069 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 46.7% | 50.0% | 4861 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1552 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 4109 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1373 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 672 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 591 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 921 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1136 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 760 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 985 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 85.0% | 0.0% | 1258 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 899 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 850 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 796 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1194 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1278 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1608 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1728 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 983 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1338 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1225 ms |
| deepseek | 100.0% | — | 0.0% | 1138 ms |
| gemini | 100.0% | 83.0% | 9.0% | 934 ms |
| mistral | 100.0% | — | 0.0% | 647 ms |
| openai | 100.0% | 95.6% | 0.0% | 848 ms |
| openrouter | 100.0% | — | 0.0% | 1382 ms |
| xai | 100.0% | — | 0.0% | 729 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 83 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 25 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 13 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
