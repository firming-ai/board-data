# FILL — the inference availability index

*As of 2026-09-20T09:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 97.7** · FILL·FLEX 91.2

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 97.1% | 94.1% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 96.1% | 88.2% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1552 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 774 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 694 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 8047 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1168 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1509 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1984 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1671 ms |  |
| deepseek/deepseek-flash/standard | 12 | 75.0% | 16.7% | 1258 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 80.0% | 11.7% | 1061 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 95.0% | 0.0% | 1278 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | 100.0% | 0.0% | 3509 ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 3112 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 734 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 742 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 7563 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 945 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1647 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 38.3% | 4320 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1325 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 8.3% | 3318 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1245 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 661 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 563 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 974 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 945 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1089 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 743 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 98.3% | 0.0% | 930 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 668 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 90.0% | 0.0% | 1371 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 970 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 96.7% | 0.0% | 739 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 890 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 791 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1296 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1317 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1506 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1479 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1621 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 701 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1382 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1296 ms |
| deepseek | 86.4% | — | 6.8% | 1187 ms |
| gemini | 100.0% | 87.1% | 7.3% | 908 ms |
| mistral | 100.0% | — | 0.0% | 625 ms |
| openai | 99.5% | 95.6% | 0.0% | 874 ms |
| openrouter | 100.0% | — | 0.0% | 1280 ms |
| xai | 100.0% | — | 0.0% | 716 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 32 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 67 s | 13 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
