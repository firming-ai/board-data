# FILL — the inference availability index

*As of 2026-09-21T19:05:01+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 86.6** · FILL·FLEX 55.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 76.5% | 52.9% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 83.2% | 58.8% (n=17) | 90.6% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 11 | 100.0% | 0.0% | 1795 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 820 ms |  |
| anthropic/claude-haiku-4-5/standard | 58 | 100.0% | 0.0% | 796 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1552 ms |  |
| anthropic/claude-opus-5/standard | 58 | 100.0% | 0.0% | 1228 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1596 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2065 ms |  |
| anthropic/claude-sonnet-5/standard | 58 | 100.0% | 0.0% | 1722 ms |  |
| deepseek/deepseek-flash/standard | 11 | 100.0% | 0.0% | 1019 ms |  |
| deepseek/deepseek-v4-flash/standard | 58 | 100.0% | 0.0% | 966 ms |  |
| deepseek/deepseek-v4-pro/standard | 58 | 100.0% | 0.0% | 1243 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 50.0% | 50.0% | 4822 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3711 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 58 | 100.0% | 0.0% | 879 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 58 | 100.0% | 0.0% | 833 ms |  |
| gemini/gemini-3.5-flash/flex | 58 | 41.4% | 41.4% | 22181 ms |  |
| gemini/gemini-3.5-flash/standard | 58 | 100.0% | 0.0% | 1046 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1976 ms |  |
| gemini/gemini-3.7-flash/flex | 58 | 34.5% | 56.9% | 10250 ms |  |
| gemini/gemini-3.7-flash/standard | 11 | 100.0% | 0.0% | 1657 ms |  |
| gemini/gemini-3.8-flash/flex | 11 | 54.5% | 45.5% | 6748 ms |  |
| gemini/gemini-3.8-flash/standard | 11 | 100.0% | 0.0% | 1338 ms |  |
| mistral/mistral-large/standard | 58 | 100.0% | 0.0% | 757 ms |  |
| mistral/mistral-small/standard | 58 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1265 ms |  |
| openai/gpt-5.5/flex | 11 | 100.0% | 0.0% | 3703 ms |  |
| openai/gpt-5.5/standard | 11 | 100.0% | 0.0% | 1327 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1050 ms |  |
| openai/gpt-5.6-luna/flex | 58 | 69.0% | 0.0% | 6155 ms |  |
| openai/gpt-5.6-luna/priority | 58 | 100.0% | 0.0% | 848 ms |  |
| openai/gpt-5.6-luna/standard | 58 | 100.0% | 0.0% | 913 ms |  |
| openai/gpt-5.6-sol/flex | 58 | 12.1% | 0.0% | 10291 ms |  |
| openai/gpt-5.6-sol/standard | 58 | 100.0% | 0.0% | 1199 ms |  |
| openai/gpt-5.6-terra/flex | 58 | 100.0% | 0.0% | 952 ms |  |
| openai/gpt-5.6-terra/priority | 11 | 100.0% | 0.0% | 1196 ms |  |
| openai/gpt-5.6-terra/standard | 58 | 100.0% | 0.0% | 1059 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1444 ms |  |
| openai/gpt-6-astra/flex | 11 | 90.9% | 0.0% | 1596 ms |  |
| openai/gpt-6-astra/standard | 11 | 100.0% | 0.0% | 1813 ms |  |
| openrouter/claude-sonnet-5/standard | 58 | 100.0% | 0.0% | 1552 ms |  |
| openrouter/gemini-3.7-flash/standard | 58 | 100.0% | 0.0% | 1644 ms |  |
| openrouter/gpt-5.6-terra/standard | 58 | 100.0% | 0.0% | 1268 ms |  |
| xai/grok-4.20/standard | 58 | 100.0% | 0.0% | 865 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1488 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1268 ms |
| deepseek | 100.0% | — | 0.0% | 1063 ms |
| gemini | 100.0% | 58.3% | 19.0% | 1009 ms |
| mistral | 100.0% | — | 0.0% | 706 ms |
| openai | 100.0% | 64.3% | 0.0% | 1104 ms |
| openrouter | 100.0% | — | 0.0% | 1518 ms |
| xai | 100.0% | — | 0.0% | 888 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 89 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 38 s | 116 min |
| openai | 96 | 91 | 5 | 0 | 93.4% | 68 s | 73 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
