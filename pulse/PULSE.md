# FILL — the inference availability index

*As of 2026-09-22T17:05:09+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 80.9** *(gap)* · FILL·FLEX 47.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 17.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.4% | — | 94.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 71.9% | — | 71.9% (n=96) | — |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1631 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 1013 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 895 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2695 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1070 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 4311 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 3081 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1961 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1343 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1122 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1407 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3425 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 43.3% | 43.3% | 30242 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 1154 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 50.0% | 48.3% | 3474 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1133 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2533 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 1.7% | 98.3% | 6167 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1647 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 16.7% | 83.3% | 3885 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 2074 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 870 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 751 ms |  |
| openai/gpt-4.1/standard | 4 | — | — | — ms |  |
| openai/gpt-5.5/flex | 12 | — | — | — ms |  |
| openai/gpt-5.5/standard | 12 | — | — | — ms |  |
| openai/gpt-5.6-luna/cache | 15 | — | — | — ms |  |
| openai/gpt-5.6-luna/flex | 60 | — | — | — ms |  |
| openai/gpt-5.6-luna/priority | 60 | — | — | — ms |  |
| openai/gpt-5.6-luna/standard | 60 | — | — | — ms |  |
| openai/gpt-5.6-sol/flex | 60 | — | — | — ms |  |
| openai/gpt-5.6-sol/standard | 60 | — | — | — ms |  |
| openai/gpt-5.6-terra/flex | 60 | — | — | — ms |  |
| openai/gpt-5.6-terra/priority | 12 | — | — | — ms |  |
| openai/gpt-5.6-terra/standard | 60 | — | — | — ms |  |
| openai/gpt-5/standard | 4 | — | — | — ms |  |
| openai/gpt-6-astra/flex | 12 | — | — | — ms |  |
| openai/gpt-6-astra/standard | 12 | — | — | — ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1926 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1957 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1524 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 848 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1567 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 2211 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1275 ms |
| deepseek | 100.0% | — | 0.0% | 1278 ms |
| gemini | 100.0% | 30.4% | 36.6% | 1230 ms |
| mistral | 100.0% | — | 0.0% | 797 ms |
| openai | — | — | — | — ms |
| openrouter | 100.0% | — | 0.0% | 1821 ms |
| xai | 100.0% | — | 0.0% | 911 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 95.8% | 2 min | 45 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 115 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 44 s | 24 min |
| openai | 96 | 86 | 0 | 10 | 69.8% | 112 s | 173 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
