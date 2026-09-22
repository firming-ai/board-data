# FILL — the inference availability index

*As of 2026-09-22T16:05:02+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 75.3** *(gap)* · FILL·FLEX 5.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 17.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.9% | — | 95.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 52.9% | 5.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 75.0% | — | 75.0% (n=96) | — |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1651 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 895 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 781 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 3358 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1152 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 4689 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2948 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1968 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1296 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1034 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1371 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3200 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 15.0% | 76.7% | 46212 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 1288 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 56.7% | 35.0% | 9127 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1115 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2296 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 2115 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 2310 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 797 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 681 ms |  |
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
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1918 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1945 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1503 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 813 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1573 ms |  |
| xai/grok-4.7/standard | 12 | 91.7% | 0.0% | 2211 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1357 ms |
| deepseek | 100.0% | — | 0.0% | 1187 ms |
| gemini | 100.0% | 22.2% | 41.0% | 1268 ms |
| mistral | 100.0% | — | 0.0% | 749 ms |
| openai | — | — | — | — ms |
| openrouter | 100.0% | — | 0.0% | 1753 ms |
| xai | 98.7% | — | 0.0% | 841 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 95.8% | 113 s | 45 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 112 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 48 s | 24 min |
| openai | 96 | 90 | 0 | 6 | 71.9% | 2 min | 186 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
