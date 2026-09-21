# FILL — the inference availability index

*As of 2026-09-21T08:05:12+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.3** · FILL·FLEX 82.4

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 88.8% | 70.6% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1718 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 838 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 775 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1435 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1346 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1625 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2132 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1843 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1235 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1070 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1299 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 14429 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3156 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 804 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 5.0% | 8982 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 968 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1770 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 73.3% | 26.7% | 2978 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1327 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 2821 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1548 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 711 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 594 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1131 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1194 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1206 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1059 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 706 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 800 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 21.7% | 0.0% | 2086 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 799 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1007 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 904 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1268 ms |  |
| openai/gpt-6-astra/flex | 12 | 83.3% | 0.0% | 1365 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1674 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1612 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1644 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1107 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 733 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1641 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1410 ms |
| deepseek | 100.0% | — | 0.0% | 1192 ms |
| gemini | 100.0% | 89.7% | 5.8% | 945 ms |
| mistral | 100.0% | — | 0.0% | 675 ms |
| openai | 99.5% | 75.5% | 0.0% | 926 ms |
| openrouter | 100.0% | — | 0.0% | 1461 ms |
| xai | 100.0% | — | 0.0% | 736 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 105 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 30 s | 211 min |
| openai | 96 | 95 | 1 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
