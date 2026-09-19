# FILL — the inference availability index

*As of 2026-09-19T22:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 98.7** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=92) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=46) | — |
| MIS·FILL | 97.8% | — | 97.8% (n=46) | — |
| OAI·FILL | 98.9% | 100.0% (n=17) | 96.7% (n=92) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1580 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 825 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2548 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1184 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1799 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1799 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1583 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1034 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 941 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1223 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 8928 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3258 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 748 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 740 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 1.7% | 16564 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1732 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 66.7% | 33.3% | 2990 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1149 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 2861 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1184 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 587 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 901 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1213 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1050 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1030 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 694 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 693 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 90.0% | 0.0% | 999 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 784 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 797 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1230 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1206 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1621 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1494 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1552 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1007 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1233 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1109 ms |
| deepseek | 100.0% | — | 0.0% | 1096 ms |
| gemini | 100.0% | 86.7% | 6.9% | 886 ms |
| mistral | 100.0% | — | 0.0% | 630 ms |
| openai | 100.0% | 95.6% | 0.0% | 835 ms |
| openrouter | 100.0% | — | 0.0% | 1390 ms |
| xai | 100.0% | — | 0.0% | 727 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 34 s | 10 min |
| openai | 96 | 96 | 0 | 0 | 96.9% | 67 s | 37 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
