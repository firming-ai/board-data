# FILL — the inference availability index

*As of 2026-09-20T19:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.1** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 89.6% | — | 89.6% (n=48) | — |
| OAI·FILL | 94.1% | 82.3% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1488 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 796 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 720 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1240 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1189 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1401 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2045 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1767 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1098 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 960 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1245 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2631 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2861 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 815 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 769 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 6106 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1722 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 66.7% | 33.3% | 3278 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 3432 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1349 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 734 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 565 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 956 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1133 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 799 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1854 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 649 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 760 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 83.3% | 0.0% | 1089 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 769 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 951 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1245 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1455 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1555 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1664 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 98.3% | 0.0% | 954 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1760 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1216 ms |
| deepseek | 100.0% | — | 0.0% | 1129 ms |
| gemini | 100.0% | 87.6% | 7.0% | 906 ms |
| mistral | 100.0% | — | 0.0% | 635 ms |
| openai | 99.5% | 95.1% | 0.0% | 853 ms |
| openrouter | 99.4% | — | 0.0% | 1407 ms |
| xai | 100.0% | — | 0.0% | 726 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 79 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 108 s |
| mistral | 48 | 41 | 7 | 0 | 100.0% | 22 s | 112 s |
| openai | 96 | 95 | 1 | 0 | 100.0% | 68 s | 12 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
