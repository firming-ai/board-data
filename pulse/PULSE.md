# FILL — the inference availability index

*As of 2026-09-20T07:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.4** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 94.1% | 88.2% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 98.0% | 94.1% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1644 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 796 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 703 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1107 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1228 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1447 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1980 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1684 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1238 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1096 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1296 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3239 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 764 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 764 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 93.3% | 5.0% | 3118 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1515 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 48.3% | 46.7% | 3839 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1424 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3996 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1206 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 687 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 583 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 876 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1048 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 731 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 701 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 769 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 90.0% | 0.0% | 981 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 755 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 846 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 752 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1133 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1177 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1427 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1570 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1657 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 930 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1260 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1218 ms |
| deepseek | 100.0% | — | 0.0% | 1175 ms |
| gemini | 100.0% | 81.2% | 9.4% | 877 ms |
| mistral | 100.0% | — | 0.0% | 626 ms |
| openai | 100.0% | 97.1% | 0.0% | 841 ms |
| openrouter | 100.0% | — | 0.0% | 1393 ms |
| xai | 100.0% | — | 0.0% | 755 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 24 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
