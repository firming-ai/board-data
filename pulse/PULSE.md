# FILL — the inference availability index

*As of 2026-09-20T06:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.8** · FILL·FLEX 87.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 87.5% | 75.0% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 789 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 734 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1248 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1177 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1365 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1674 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1021 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1322 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1057 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1275 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2273 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2755 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 835 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 60.0% | 31.7% | 5693 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 939 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1647 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 68.3% | 31.7% | 3855 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1273 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3239 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1173 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 592 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 954 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 922 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 799 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1111 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 658 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1032 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 743 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 892 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1225 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1739 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1243 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1476 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1628 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 941 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 711 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1309 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1021 ms |
| deepseek | 100.0% | — | 0.0% | 1177 ms |
| gemini | 100.0% | 76.7% | 11.7% | 917 ms |
| mistral | 100.0% | — | 0.0% | 659 ms |
| openai | 100.0% | 96.6% | 0.0% | 818 ms |
| openrouter | 100.0% | — | 0.0% | 1384 ms |
| xai | 100.0% | — | 0.0% | 716 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 27 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
