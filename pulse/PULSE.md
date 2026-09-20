# FILL — the inference availability index

*As of 2026-09-20T18:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.1** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 93.8% | — | 93.8% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1599 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 780 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1715 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1182 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1327 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2000 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1753 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1258 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1149 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1233 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 50.0% | 2448 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3175 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 772 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 749 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5997 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 911 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1708 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 71.7% | 28.3% | 3831 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 58.3% | 41.7% | 3460 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1530 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 697 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 609 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 958 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 874 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1003 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1082 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 73.3% | 0.0% | 1260 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 928 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 774 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 775 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1087 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-6-astra/standard | 12 | 83.3% | 0.0% | 1542 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1470 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 707 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1592 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1275 ms |
| deepseek | 100.0% | — | 0.0% | 1208 ms |
| gemini | 100.0% | 88.1% | 6.7% | 886 ms |
| mistral | 100.0% | — | 0.0% | 658 ms |
| openai | 99.1% | 92.2% | 0.0% | 836 ms |
| openrouter | 100.0% | — | 0.0% | 1322 ms |
| xai | 100.0% | — | 0.0% | 716 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 80 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 113 s |
| mistral | 48 | 43 | 5 | 0 | 100.0% | 22 s | 108 s |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 12 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
