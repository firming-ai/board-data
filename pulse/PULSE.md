# FILL — the inference availability index

*As of 2026-09-22T11:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 92.0** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 98.4% | — | 96.9% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 91.7% | — | 91.7% (n=48) | — |
| OAI·FILL | 92.4% | 100.0% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1778 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 850 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 766 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1521 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1360 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2020 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2228 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1922 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1140 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1055 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1338 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 46677 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 6940 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 830 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 800 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 93.3% | 5.0% | 9018 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1984 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 58.3% | 40.0% | 5372 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1527 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3659 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1268 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 631 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1070 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1024 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1107 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 930 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1177 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 853 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1194 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1120 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 852 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1070 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1030 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1161 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1248 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1914 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1667 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1691 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1173 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1401 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 2507 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1401 ms |
| deepseek | 100.0% | — | 0.0% | 1173 ms |
| gemini | 100.0% | 83.5% | 8.7% | 972 ms |
| mistral | 100.0% | — | 0.0% | 711 ms |
| openai | 100.0% | 98.5% | 0.0% | 1030 ms |
| openrouter | 100.0% | — | 0.0% | 1518 ms |
| xai | 100.0% | — | 0.0% | 808 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 94 | 2 | 0 | 96.8% | 108 s | 27 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 95.8% | 49 s | 31 min |
| openai | 96 | 95 | 1 | 0 | 76.8% | 96 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
