# FILL — the inference availability index

*As of 2026-09-22T03:05:03+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 95.8** · FILL·FLEX 94.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.5% | — | 99.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 93.8% | 100.0% (n=17) | 81.2% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1644 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 780 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 706 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1325 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1373 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1854 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1404 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1208 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1199 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1100 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1275 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 4184 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3175 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 830 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 813 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 76.7% | 15.0% | 11328 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1003 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1704 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 38.3% | 3245 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1432 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 2896 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1258 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 721 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 638 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1196 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1007 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1065 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1005 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 919 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 783 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 767 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1309 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 999 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 780 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1059 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 935 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1243 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1268 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1694 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1667 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1795 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1118 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 758 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1421 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1208 ms |
| deepseek | 100.0% | — | 0.0% | 1199 ms |
| gemini | 100.0% | 80.4% | 9.6% | 951 ms |
| mistral | 100.0% | — | 0.0% | 687 ms |
| openai | 99.5% | 100.0% | 0.0% | 922 ms |
| openrouter | 100.0% | — | 0.0% | 1470 ms |
| xai | 100.0% | — | 0.0% | 766 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 99.0% | 99 s | 7 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 61 s | 116 min |
| openai | 96 | 93 | 3 | 0 | 83.9% | 83 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
