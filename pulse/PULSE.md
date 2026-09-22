# FILL — the inference availability index

*As of 2026-09-22T05:05:01+00:00 · probe pulse-1.2.3 · methodology 1.2.0*

**FILL 96.7** · FILL·FLEX 97.1

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 99.5% | — | 99.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=48) | — |
| OAI·FILL | 93.4% | 100.0% (n=17) | 80.2% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1301 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 820 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1398 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1235 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1691 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1491 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1218 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1228 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1001 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1228 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2867 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2919 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 815 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 784 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 95.0% | 3.3% | 13056 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1005 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1621 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 80.0% | 20.0% | 2942 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1325 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 100.0% | 0.0% | 2487 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1253 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 610 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1015 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1063 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 964 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 805 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 737 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1138 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 928 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 98.3% | 0.0% | 784 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1034 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 915 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1421 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1304 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1803 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1704 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1701 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1080 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 743 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1412 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1180 ms |
| deepseek | 100.0% | — | 0.0% | 1127 ms |
| gemini | 100.0% | 92.3% | 4.1% | 964 ms |
| mistral | 100.0% | — | 0.0% | 657 ms |
| openai | 99.5% | 98.0% | 0.0% | 870 ms |
| openrouter | 100.0% | — | 0.0% | 1482 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 93 | 3 | 0 | 98.9% | 100 s | 8 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 84 s | 107 s |
| mistral | 48 | 48 | 0 | 0 | 87.5% | 66 s | 116 min |
| openai | 96 | 92 | 4 | 0 | 82.6% | 100 s | 185 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
