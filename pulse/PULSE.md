# FILL — the inference availability index

*As of 2026-09-20T14:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.1** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 838 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1548 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1173 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1828 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2012 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1760 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1118 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1327 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4329 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3391 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 752 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 780 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 8375 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1461 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 56.7% | 43.3% | 3801 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1371 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 4346 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1189 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 685 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 588 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1021 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1138 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 870 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 934 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 678 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1341 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 928 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 743 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 904 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 843 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1192 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1248 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1309 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1530 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1583 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1007 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 707 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1450 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1194 ms |
| deepseek | 100.0% | — | 0.0% | 1127 ms |
| gemini | 100.0% | 86.1% | 7.8% | 954 ms |
| mistral | 100.0% | — | 0.0% | 641 ms |
| openai | 99.5% | 96.6% | 0.0% | 874 ms |
| openrouter | 100.0% | — | 0.0% | 1330 ms |
| xai | 100.0% | — | 0.0% | 718 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 82 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 78 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 25 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 9 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
