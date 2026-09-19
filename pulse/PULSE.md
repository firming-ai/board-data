# FILL — the inference availability index

*As of 2026-09-19T08:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 93.8** · FILL·FLEX 82.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=36) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=18) | — |
| MIS·FILL | 94.4% | — | 94.4% (n=18) | — |
| OAI·FILL | 93.3% | 88.2% (n=17) | 91.7% (n=36) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1373 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 764 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1159 ms |  |
| anthropic/claude-opus-5/standard | 60 | 98.3% | 1.7% | 1168 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1654 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2037 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 98.3% | 1.7% | 1677 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1225 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1009 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1322 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 50.0% | 50.0% | 2705 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2390 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 752 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5459 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1567 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 48.3% | 48.3% | 4842 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1533 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 58.3% | 41.7% | 2990 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1250 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 707 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 598 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 872 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1118 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 840 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 857 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 662 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 96.7% | 0.0% | 1034 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 850 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 999 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 852 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1283 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1429 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1404 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 917 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1228 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 99.0% | — | 1.0% | 1263 ms |
| deepseek | 100.0% | — | 0.0% | 1156 ms |
| gemini | 100.0% | 80.6% | 10.3% | 904 ms |
| mistral | 100.0% | — | 0.0% | 644 ms |
| openai | 99.5% | 97.5% | 0.0% | 864 ms |
| openrouter | 100.0% | — | 0.0% | 1357 ms |
| xai | 100.0% | — | 0.0% | 737 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 40 | 40 | 0 | 0 | 100.0% | 97 s | 3 min |
| gemini | 20 | 20 | 0 | 0 | 100.0% | 86 s | 116 s |
| mistral | 20 | 20 | 0 | 0 | 95.0% | 34 s | 7 min |
| openai | 40 | 39 | 1 | 0 | 92.3% | 68 s | 62 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
