# FILL — the inference availability index

*As of 2026-09-19T09:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.6** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=40) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=20) | — |
| MIS·FILL | 95.0% | — | 95.0% (n=20) | — |
| OAI·FILL | 89.7% | 76.5% (n=17) | 92.5% (n=40) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1770 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 820 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1464 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1091 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2861 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 93.3% | 0.0% | 2041 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1725 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1204 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 997 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1273 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 3689 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3537 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 764 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 6279 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 943 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1671 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 40.0% | 60.0% | 5009 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1404 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3809 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1354 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 714 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 571 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1129 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1255 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1120 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 853 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 1048 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 670 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 81.7% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 858 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1017 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 865 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1161 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1253 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1778 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1435 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 979 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1647 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1166 ms |
| deepseek | 100.0% | — | 0.0% | 1129 ms |
| gemini | 100.0% | 80.1% | 11.2% | 913 ms |
| mistral | 100.0% | — | 0.0% | 666 ms |
| openai | 100.0% | 93.6% | 0.0% | 911 ms |
| openrouter | 100.0% | — | 0.0% | 1338 ms |
| xai | 100.0% | — | 0.0% | 733 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 44 | 44 | 0 | 0 | 100.0% | 96 s | 2 min |
| gemini | 22 | 22 | 0 | 0 | 100.0% | 86 s | 116 s |
| mistral | 22 | 22 | 0 | 0 | 95.5% | 34 s | 4 min |
| openai | 44 | 43 | 1 | 0 | 93.0% | 68 s | 60 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
