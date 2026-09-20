# FILL — the inference availability index

*As of 2026-09-20T04:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 99.0** · FILL·FLEX 97.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 96.9% | 93.8% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1322 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 745 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2305 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1238 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1357 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1828 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1194 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 970 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1322 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2376 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3220 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 730 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 746 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 6802 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1573 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 73.3% | 26.7% | 4959 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1429 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 16.7% | 5739 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1149 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 690 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 566 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1050 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 780 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 976 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 675 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1111 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 754 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 853 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1189 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1447 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1533 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1608 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1346 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1007 ms |
| deepseek | 100.0% | — | 0.0% | 1159 ms |
| gemini | 100.0% | 88.6% | 5.8% | 879 ms |
| mistral | 100.0% | — | 0.0% | 632 ms |
| openai | 100.0% | 96.1% | 0.0% | 838 ms |
| openrouter | 100.0% | — | 0.0% | 1384 ms |
| xai | 100.0% | — | 0.0% | 789 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 47 | 1 | 0 | 100.0% | 34 s | 11 min |
| openai | 96 | 95 | 1 | 0 | 100.0% | 67 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
