# FILL — the inference availability index

*As of 2026-09-20T10:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 94.8** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 90.2% | 70.6% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1435 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 769 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1393 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1196 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1647 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1903 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1728 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1082 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 993 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1194 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3069 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2766 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 748 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 4311 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 926 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1767 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 63.3% | 36.7% | 3667 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1240 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4337 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1260 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 681 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 572 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1070 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 899 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1009 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 833 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 650 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 796 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 71.7% | 0.0% | 1322 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 799 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 823 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 821 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1352 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1512 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1407 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1515 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1858 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 989 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1240 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1260 ms |
| deepseek | 100.0% | — | 0.0% | 1082 ms |
| gemini | 100.0% | 87.1% | 7.3% | 893 ms |
| mistral | 100.0% | — | 0.0% | 623 ms |
| openai | 99.5% | 90.7% | 0.0% | 892 ms |
| openrouter | 100.0% | — | 0.0% | 1424 ms |
| xai | 100.0% | — | 0.0% | 734 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 13 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
