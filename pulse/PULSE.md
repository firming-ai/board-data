# FILL — the inference availability index

*As of 2026-09-21T17:05:03+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 84.7** · FILL·FLEX 50.0

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 67.6% | 35.3% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 75.0% | — | 75.0% (n=48) | — |
| OAI·FILL | 86.5% | 64.7% (n=17) | 94.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1770 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 892 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1444 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1216 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 2211 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2120 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1767 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1152 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1026 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1293 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 12222 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3572 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 1122 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 872 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 36.7% | 58.3% | 17659 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1026 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1760 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 8.3% | 71.7% | 23790 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1899 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 41.7% | 58.3% | 8476 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1684 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 739 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1322 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1268 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1424 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1147 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 71.7% | 0.0% | 9868 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 1015 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 5.0% | 0.0% | 10689 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1288 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 1011 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1312 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1140 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1677 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1965 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1788 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1671 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1732 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1268 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 783 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1631 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1288 ms |
| deepseek | 100.0% | — | 0.0% | 1159 ms |
| gemini | 100.0% | 48.5% | 24.7% | 989 ms |
| mistral | 100.0% | — | 0.0% | 704 ms |
| openai | 100.0% | 62.8% | 0.0% | 1163 ms |
| openrouter | 100.0% | — | 0.0% | 1561 ms |
| xai | 100.0% | — | 0.0% | 796 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 80 s | 105 s |
| mistral | 48 | 48 | 0 | 0 | 79.2% | 38 s | 162 min |
| openai | 96 | 93 | 3 | 0 | 95.7% | 69 s | 47 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
