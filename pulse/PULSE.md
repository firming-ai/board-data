# FILL — the inference availability index

*As of 2026-09-21T20:05:02+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 93.2** · FILL·FLEX 79.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 91.2% | 82.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 88.3% | 76.5% (n=17) | 88.5% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1644 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 911 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1382 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1278 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1497 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2016 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1753 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1161 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 972 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1263 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 8561 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3311 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 846 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 850 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 78.3% | 18.3% | 12320 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1061 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1701 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 55.0% | 45.0% | 4551 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1521 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 3956 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1338 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 657 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1115 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1447 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1349 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 53.3% | 0.0% | 7624 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 766 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 865 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 6.7% | 0.0% | 10148 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1115 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 901 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1235 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1452 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1722 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 2158 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1539 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1681 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1368 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1577 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1314 ms |
| deepseek | 100.0% | — | 0.0% | 1120 ms |
| gemini | 100.0% | 77.8% | 11.9% | 1005 ms |
| mistral | 100.0% | — | 0.0% | 717 ms |
| openai | 100.0% | 58.8% | 0.0% | 1048 ms |
| openrouter | 100.0% | — | 0.0% | 1497 ms |
| xai | 100.0% | — | 0.0% | 777 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 93 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 76 s | 105 s |
| mistral | 48 | 48 | 0 | 0 | 89.6% | 38 s | 116 min |
| openai | 96 | 91 | 5 | 0 | 91.2% | 69 s | 97 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
