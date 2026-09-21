# FILL — the inference availability index

*As of 2026-09-21T15:05:12+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 86.1** · FILL·FLEX 52.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 73.5% | 47.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 72.9% | — | 72.9% (n=48) | — |
| OAI·FILL | 84.9% | 58.8% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1674 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 954 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 739 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1473 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1384 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 3756 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2180 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1846 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1240 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1093 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1335 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 0.0% | 0.0% | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3419 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 85.0% | 0.0% | 20313 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 1024 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 55.0% | 38.3% | 9072 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 1089 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1988 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 13.3% | 63.3% | 23837 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 2175 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 25.0% | 75.0% | 5448 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1795 ms |  |
| mistral/mistral-large/standard | 60 | 98.3% | 1.7% | 855 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1218 ms |  |
| openai/gpt-5.5/flex | 12 | 91.7% | 0.0% | 1708 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1373 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 1129 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 76.7% | 0.0% | 14229 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 864 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 972 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 16.7% | 0.0% | 10127 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 2700 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 985 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1113 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1725 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 4101 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1817 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1681 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1245 ms |  |
| xai/grok-4.20/standard | 60 | 98.3% | 0.0% | 786 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1634 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1447 ms |
| deepseek | 100.0% | — | 0.0% | 1189 ms |
| gemini | 100.0% | 49.0% | 20.4% | 1100 ms |
| mistral | 99.2% | — | 0.8% | 761 ms |
| openai | 99.5% | 67.7% | 0.0% | 1235 ms |
| openrouter | 100.0% | — | 0.0% | 1564 ms |
| xai | 98.4% | — | 0.0% | 792 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 85 s | 3 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 82 s | 106 s |
| mistral | 48 | 48 | 0 | 0 | 72.9% | 38 s | 211 min |
| openai | 96 | 95 | 1 | 0 | 95.8% | 69 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
