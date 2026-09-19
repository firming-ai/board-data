# FILL — the inference availability index

*As of 2026-09-19T14:05:07+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 98.5** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=60) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=30) | — |
| MIS·FILL | 96.7% | — | 96.7% (n=30) | — |
| OAI·FILL | 98.3% | 100.0% (n=17) | 95.0% (n=60) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 836 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1346 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1147 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1861 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2032 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1749 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1131 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1044 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1393 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 4329 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3131 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 802 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 763 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 5914 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1788 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 38.3% | 4260 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1360 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 4052 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1447 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 716 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 596 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 865 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1046 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 808 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 915 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 717 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1184 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 874 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1189 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1228 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1418 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1497 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1843 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 36425 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1228 ms |
| deepseek | 100.0% | — | 0.0% | 1201 ms |
| gemini | 100.0% | 87.2% | 7.2% | 904 ms |
| mistral | 100.0% | — | 0.0% | 675 ms |
| openai | 100.0% | 98.5% | 0.0% | 881 ms |
| openrouter | 100.0% | — | 0.0% | 1438 ms |
| xai | 100.0% | — | 0.0% | 751 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 64 | 64 | 0 | 0 | 100.0% | 95 s | 2 min |
| gemini | 32 | 32 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 32 | 32 | 0 | 0 | 96.9% | 34 s | 4 min |
| openai | 64 | 63 | 1 | 0 | 95.2% | 67 s | 53 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
