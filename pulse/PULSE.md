# FILL — the inference availability index

*As of 2026-09-22T13:05:12+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 87.9** · FILL·FLEX 73.5

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 97.9% | — | 95.8% (n=96) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 97.9% | — | 97.9% (n=48) | — |
| OAI·FILL | 92.4% | 100.0% (n=17) | 77.1% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1704 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 876 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 858 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1674 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1322 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 4900 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2167 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1843 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1373 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1076 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1293 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 100.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3213 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 1283 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 893 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 999 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1788 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 18.3% | 70.0% | 10067 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1687 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 33.3% | 66.7% | 5470 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1644 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 658 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1248 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1275 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1129 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 932 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1291 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 908 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 991 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1387 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 924 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1168 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1163 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1756 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1552 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1941 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1711 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1756 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1228 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 807 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1641 ms |  |
| xai/grok-4.7/standard | 12 | 100.0% | 0.0% | 2433 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1418 ms |
| deepseek | 100.0% | — | 0.0% | 1208 ms |
| gemini | 100.0% | 69.6% | 15.1% | 947 ms |
| mistral | 100.0% | — | 0.0% | 658 ms |
| openai | 100.0% | 99.5% | 0.0% | 1145 ms |
| openrouter | 100.0% | — | 0.0% | 1561 ms |
| xai | 100.0% | — | 0.0% | 836 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 95 | 1 | 0 | 95.8% | 110 s | 45 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 112 s |
| mistral | 48 | 48 | 0 | 0 | 97.9% | 42 s | 24 min |
| openai | 96 | 96 | 0 | 0 | 77.1% | 2 min | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
