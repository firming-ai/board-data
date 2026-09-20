# FILL — the inference availability index

*As of 2026-09-20T23:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 91.5** · FILL·FLEX 70.6

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 82.4% | 64.7% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 92.2% | 76.5% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1435 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 792 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 726 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1438 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1140 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1371 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2069 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1795 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1061 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 902 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1265 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2700 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2960 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 726 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 731 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 96.7% | 3.3% | 8342 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 884 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1774 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 2390 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1280 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 83.3% | 16.7% | 2269 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1263 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 577 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 964 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 850 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 713 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 911 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 638 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 93.3% | 0.0% | 1245 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 731 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 826 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1233 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1299 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1573 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1458 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1647 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 956 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 686 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1476 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1201 ms |
| deepseek | 100.0% | — | 0.0% | 1089 ms |
| gemini | 100.0% | 88.7% | 6.4% | 835 ms |
| mistral | 100.0% | — | 0.0% | 631 ms |
| openai | 100.0% | 98.0% | 0.0% | 830 ms |
| openrouter | 100.0% | — | 0.0% | 1349 ms |
| xai | 100.0% | — | 0.0% | 693 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 78 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 108 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 34 s | 211 min |
| openai | 96 | 94 | 2 | 0 | 100.0% | 68 s | 14 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
