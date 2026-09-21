# FILL — the inference availability index

*As of 2026-09-21T06:05:02+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.6** · FILL·FLEX 88.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 88.2% | 76.5% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 83.3% | — | 83.3% (n=48) | — |
| OAI·FILL | 98.6% | 100.0% (n=17) | 95.8% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1589 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 830 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 745 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1283 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1362 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1586 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 2197 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1832 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1260 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1026 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1268 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 2631 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2487 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 816 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 774 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 100.0% | 0.0% | 2816 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 981 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1781 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 70.0% | 30.0% | 3432 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1293 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 2925 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1187 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 692 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 591 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1026 ms |  |
| openai/gpt-5.5/flex | 12 | 83.3% | 0.0% | 2016 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1199 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 985 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 860 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 681 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 836 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 93.3% | 0.0% | 1283 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 1032 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 792 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1053 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 845 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1100 ms |  |
| openai/gpt-6-astra/flex | 12 | 75.0% | 0.0% | 1444 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1527 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1661 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1760 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 1067 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 748 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1503 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1362 ms |
| deepseek | 100.0% | — | 0.0% | 1120 ms |
| gemini | 100.0% | 90.2% | 5.5% | 941 ms |
| mistral | 100.0% | — | 0.0% | 657 ms |
| openai | 99.5% | 95.6% | 0.0% | 926 ms |
| openrouter | 100.0% | — | 0.0% | 1512 ms |
| xai | 100.0% | — | 0.0% | 757 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 77 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 75 s | 102 s |
| mistral | 48 | 48 | 0 | 0 | 83.3% | 27 s | 211 min |
| openai | 96 | 95 | 1 | 0 | 95.8% | 68 s | 41 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
