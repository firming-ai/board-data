# FILL — the inference availability index

*As of 2026-09-20T12:05:07+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 99.0** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1599 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 767 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 729 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1223 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1225 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1573 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2012 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1735 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1145 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 974 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1379 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3385 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2727 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 6967 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 962 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1922 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 3711 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1296 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 4363 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1352 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 694 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 586 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1046 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1074 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1154 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 775 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 690 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1288 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 784 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 987 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 843 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1204 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1677 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1567 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1539 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1561 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 985 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1357 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1286 ms |
| deepseek | 100.0% | — | 0.0% | 1177 ms |
| gemini | 100.0% | 85.0% | 8.4% | 926 ms |
| mistral | 100.0% | — | 0.0% | 642 ms |
| openai | 100.0% | 100.0% | 0.0% | 883 ms |
| openrouter | 100.0% | — | 0.0% | 1390 ms |
| xai | 100.0% | — | 0.0% | 737 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 83 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 25 s | 15 min |
| openai | 96 | 95 | 1 | 0 | 100.0% | 68 s | 10 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
