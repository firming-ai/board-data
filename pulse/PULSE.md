# FILL — the inference availability index

*As of 2026-09-21T13:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 94.0** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 72.9% | — | 72.9% (n=48) | — |
| OAI·FILL | 90.8% | 76.5% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1596 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 876 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 760 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1618 ms |  |
| anthropic/claude-opus-5/standard | 60 | 80.0% | 20.0% | 1742 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2301 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2184 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1770 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1147 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1065 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1387 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3530 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3265 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 98.3% | 1.7% | 978 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 911 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 6393 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 995 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1937 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 65.0% | 31.7% | 10007 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1749 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 3909 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1455 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 730 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 674 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1156 ms |  |
| openai/gpt-5.5/flex | 12 | 83.3% | 0.0% | 1545 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1309 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1107 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1447 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 788 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 879 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 6.7% | 0.0% | 13671 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1371 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 820 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1225 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 997 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1322 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 3252 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1778 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1577 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1651 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1213 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1421 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 94.0% | — | 6.0% | 1524 ms |
| deepseek | 100.0% | — | 0.0% | 1194 ms |
| gemini | 100.0% | 87.1% | 6.7% | 995 ms |
| mistral | 100.0% | — | 0.0% | 685 ms |
| openai | 99.5% | 71.1% | 0.0% | 1100 ms |
| openrouter | 100.0% | — | 0.0% | 1491 ms |
| xai | 100.0% | — | 0.0% | 784 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 100.0% | 81 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 72.9% | 44 s | 211 min |
| openai | 96 | 96 | 0 | 0 | 95.8% | 68 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
