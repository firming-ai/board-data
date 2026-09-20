# FILL — the inference availability index

*As of 2026-09-20T17:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.8** · FILL·FLEX 76.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 90.2% | 70.6% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1742 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 843 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 713 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1552 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1173 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1412 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1980 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1788 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1243 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1115 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3378 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2990 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 786 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 788 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5426 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1596 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 3972 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1412 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3870 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1327 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 718 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 594 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 954 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 979 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1149 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 699 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 807 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 83.3% | 0.0% | 1949 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 774 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 872 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 789 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1319 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1527 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1488 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1725 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1019 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 754 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1421 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1216 ms |
| deepseek | 100.0% | — | 0.0% | 1184 ms |
| gemini | 100.0% | 85.6% | 8.1% | 904 ms |
| mistral | 100.0% | — | 0.0% | 654 ms |
| openai | 100.0% | 95.1% | 0.0% | 860 ms |
| openrouter | 100.0% | — | 0.0% | 1341 ms |
| xai | 100.0% | — | 0.0% | 764 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 83 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 113 s |
| mistral | 48 | 45 | 3 | 0 | 100.0% | 23 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 12 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
