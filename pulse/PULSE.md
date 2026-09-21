# FILL — the inference availability index

*As of 2026-09-21T14:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 87.1** · FILL·FLEX 58.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 70.6% | 41.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 72.9% | — | 72.9% (n=48) | — |
| OAI·FILL | 90.8% | 76.5% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1718 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 908 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2376 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1260 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2931 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2197 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1824 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1204 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1030 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1338 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 7488 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3338 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 1038 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 904 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 91.7% | 1.7% | 7624 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2237 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 45.0% | 50.0% | 13808 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1861 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 50.0% | 50.0% | 3696 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1441 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 706 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1415 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1404 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1488 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1143 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 70.0% | 0.0% | 6432 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 857 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 11.7% | 0.0% | 9947 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 2333 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1082 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1067 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1515 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1774 ms |  |
| openai/gpt-6-astra/standard | 12 | 75.0% | 0.0% | 3351 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1694 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1634 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1243 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 789 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1687 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1376 ms |
| deepseek | 100.0% | — | 0.0% | 1199 ms |
| gemini | 100.0% | 77.3% | 10.8% | 1011 ms |
| mistral | 100.0% | — | 0.0% | 780 ms |
| openai | 98.6% | 65.2% | 0.0% | 1201 ms |
| openrouter | 100.0% | — | 0.0% | 1521 ms |
| xai | 100.0% | — | 0.0% | 800 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 84 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 72.9% | 40 s | 211 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
