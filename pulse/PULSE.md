# FILL — the inference availability index

*As of 2026-09-20T00:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 98.0** · FILL·FLEX 97.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 96.9% | 93.8% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 97.1% | 100.0% (n=17) | 97.9% (n=96) | 93.3% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1828 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 857 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 707 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1319 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1230 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1968 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1674 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1140 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1206 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 2972 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2652 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 770 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 763 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 4311 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1512 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 53.3% | 46.7% | 3358 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1208 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2615 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1087 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 569 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 904 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1161 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1080 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 823 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1005 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 641 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 677 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 83.3% | 0.0% | 1147 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 780 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 808 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 993 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1506 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1365 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1503 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1612 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1473 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1036 ms |
| deepseek | 100.0% | — | 0.0% | 1076 ms |
| gemini | 100.0% | 84.5% | 8.8% | 874 ms |
| mistral | 100.0% | — | 0.0% | 627 ms |
| openai | 100.0% | 94.6% | 0.0% | 830 ms |
| openrouter | 100.0% | — | 0.0% | 1343 ms |
| xai | 100.0% | — | 0.0% | 694 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 34 s | 11 min |
| openai | 96 | 95 | 1 | 0 | 100.0% | 67 s | 27 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
