# FILL — the inference availability index

*As of 2026-09-22T10:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 94.3** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.4% | — | 96.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 90.4% | 94.1% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1980 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 874 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1357 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1725 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2124 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1861 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1230 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1042 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 50.0% | 62630 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2861 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 797 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 9653 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1763 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 25.0% | 10971 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1432 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2966 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1312 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 760 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 616 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 987 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1082 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1019 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 805 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1127 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 789 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1319 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1333 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1899 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1625 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1806 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1129 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1404 ms |  |
| xai/grok-4.7/standard | 12 | 83.3% | 0.0% | 2219 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1357 ms |
| deepseek | 100.0% | — | 0.0% | 1143 ms |
| gemini | 100.0% | 83.0% | 5.8% | 978 ms |
| mistral | 100.0% | — | 0.0% | 681 ms |
| openai | 100.0% | 100.0% | 0.0% | 1003 ms |
| openrouter | 100.0% | — | 0.0% | 1476 ms |
| xai | 97.4% | — | 0.0% | 789 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 96.9% | 106 s | 25 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 91.7% | 58 s | 69 min |
| openai | 96 | 95 | 1 | 0 | 76.8% | 98 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
