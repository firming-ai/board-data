# FILL — the inference availability index

*As of 2026-09-19T13:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.4** · FILL·FLEX 94.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=56) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=28) | — |
| MIS·FILL | 96.4% | — | 96.4% (n=28) | — |
| OAI·FILL | 98.2% | 100.0% (n=17) | 94.6% (n=56) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1615 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 845 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 721 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1194 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1122 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1545 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2061 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1760 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1233 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1055 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1343 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | 100.0% | 0.0% | 6033 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 2733 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 835 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 799 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 7503 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1577 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 56.7% | 41.7% | 6292 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1427 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 66.7% | 33.3% | 4260 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1373 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 708 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 596 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 956 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1063 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1044 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 892 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 2589 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 683 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 699 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1154 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 816 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1283 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1398 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1612 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1788 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 743 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1548 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1196 ms |
| deepseek | 100.0% | — | 0.0% | 1194 ms |
| gemini | 100.0% | 84.7% | 8.3% | 943 ms |
| mistral | 100.0% | — | 0.0% | 666 ms |
| openai | 100.0% | 99.0% | 0.0% | 881 ms |
| openrouter | 100.0% | — | 0.0% | 1452 ms |
| xai | 100.0% | — | 0.0% | 749 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 60 | 60 | 0 | 0 | 100.0% | 95 s | 2 min |
| gemini | 30 | 30 | 0 | 0 | 100.0% | 85 s | 116 s |
| mistral | 30 | 30 | 0 | 0 | 96.7% | 32 s | 4 min |
| openai | 60 | 59 | 1 | 0 | 94.9% | 67 s | 55 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
