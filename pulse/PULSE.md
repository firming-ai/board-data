# FILL — the inference availability index

*As of 2026-09-22T14:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 86.0** · FILL·FLEX 67.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.9% | — | 95.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 67.6% | 35.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 92.4% | 100.0% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1708 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 952 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 772 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1615 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1161 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 4949 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2343 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1910 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1098 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 951 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1335 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3862 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 96.7% | 0.0% | 12444 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 83.3% | 15.0% | 10583 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1040 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2016 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 13.3% | 86.7% | 6155 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1884 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1746 ms |  |
| mistral/mistral-large/standard | 60 | 98.3% | 1.7% | 970 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1104 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1159 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1145 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1046 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1570 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 2711 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 911 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1230 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1154 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1470 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1512 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1906 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1763 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1918 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1352 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1479 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 2094 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1357 ms |
| deepseek | 100.0% | — | 0.0% | 1109 ms |
| gemini | 100.0% | 59.8% | 21.8% | 1087 ms |
| mistral | 99.2% | — | 0.8% | 789 ms |
| openai | 100.0% | 99.5% | 0.0% | 1248 ms |
| openrouter | 100.0% | — | 0.0% | 1628 ms |
| xai | 100.0% | — | 0.0% | 821 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 95.8% | 119 s | 44 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 112 s |
| mistral | 48 | 47 | 1 | 0 | 97.9% | 42 s | 25 min |
| openai | 96 | 96 | 0 | 0 | 77.1% | 2 min | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
