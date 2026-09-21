# FILL — the inference availability index

*As of 2026-09-21T04:05:12+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 96.7** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 93.1% | 82.3% (n=17) | 96.9% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1412 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 781 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 2657 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1260 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1491 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2124 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1698 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1082 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1011 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1213 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3137 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2948 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 754 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 5925 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 947 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 2246 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 71.7% | 28.3% | 3460 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1278 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2805 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1341 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 651 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 555 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1048 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 911 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 991 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 653 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1325 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 947 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 713 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 962 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1255 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1220 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1476 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1452 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1742 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1013 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1360 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1301 ms |
| deepseek | 100.0% | — | 0.0% | 1118 ms |
| gemini | 100.0% | 89.2% | 6.1% | 913 ms |
| mistral | 100.0% | — | 0.0% | 620 ms |
| openai | 100.0% | 98.5% | 0.0% | 830 ms |
| openrouter | 100.0% | — | 0.0% | 1407 ms |
| xai | 100.0% | — | 0.0% | 748 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 24 s | 211 min |
| openai | 96 | 93 | 3 | 0 | 98.9% | 68 s | 28 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
