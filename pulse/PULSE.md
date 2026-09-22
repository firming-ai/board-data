# FILL — the inference availability index

*As of 2026-09-22T02:30:52+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 91.6** · FILL·FLEX 81.8

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.5% | — | 99.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 81.3% | 62.5% (n=16) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 94.1% | 100.0% (n=17) | 82.3% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1458 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 860 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1243 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1742 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1441 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1491 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1189 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1346 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1050 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1291 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2584 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2850 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 830 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 797 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 65.0% | 30.0% | 12125 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1850 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 68.3% | 31.7% | 3741 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1365 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 3100 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1327 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 596 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1136 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1036 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1147 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 989 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 754 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1206 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 805 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1057 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 937 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1233 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1384 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1674 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1835 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1104 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1432 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1194 ms |
| deepseek | 100.0% | — | 0.0% | 1189 ms |
| gemini | 100.0% | 79.4% | 10.8% | 983 ms |
| mistral | 100.0% | — | 0.0% | 664 ms |
| openai | 99.5% | 99.0% | 0.0% | 921 ms |
| openrouter | 100.0% | — | 0.0% | 1479 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 92 | 4 | 0 | 100.0% | 96 s | 4 min |
| gemini | 48 | 47 | 1 | 0 | 100.0% | 80 s | 107 s |
| mistral | 48 | 47 | 1 | 0 | 87.2% | 56 s | 117 min |
| openai | 96 | 91 | 5 | 0 | 84.6% | 81 s | 186 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
