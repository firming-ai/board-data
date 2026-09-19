# FILL — the inference availability index

*As of 2026-09-19T03:11:05+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 94.8** · FILL·FLEX 90.9

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 33.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=16) | 100.0% (n=4) |
| GEM·FILL | 90.6% | 81.2% (n=16) | 100.0% (n=8) | — |
| MIS·FILL | 87.5% | — | 87.5% (n=8) | — |
| OAI·FILL | 93.8% | 100.0% (n=17) | 81.2% (n=16) | 100.0% (n=13) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1476 ms |  |
| anthropic/claude-haiku-4-5/cache | 6 | 100.0% | 0.0% | 906 ms | ▲ |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 683 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1278 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1098 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1548 ms |  |
| anthropic/claude-sonnet-5/cache | 6 | 100.0% | 0.0% | 1984 ms | ▲ |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1742 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1243 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 1072 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1263 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 4 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 4 | 100.0% | 0.0% | 3385 ms |  |
| gemini/gemini-3.5-flash-lite/cache | 12 | 100.0% | 0.0% | 924 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 766 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 739 ms |  |
| gemini/gemini-3.5-flash/cache | 6 | 100.0% | 0.0% | 1248 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 6575 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 974 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1577 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 60.0% | 40.0% | 4460 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1180 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 75.0% | 25.0% | 2568 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1365 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 714 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 585 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 1003 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 1063 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1136 ms |  |
| openai/gpt-5.6-luna/cache | 12 | 100.0% | 0.0% | 991 ms | ▲ |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 1038 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 687 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 664 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 100.0% | 0.0% | 1286 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 993 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 786 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 1076 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1127 ms |  |
| openai/gpt-6-astra/flex | 12 | 91.7% | 0.0% | 1296 ms |  |
| openai/gpt-6-astra/standard | 12 | 91.7% | 0.0% | 1704 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1438 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1641 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 911 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 757 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1455 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1118 ms |
| deepseek | 100.0% | — | 0.0% | 1159 ms |
| gemini | 100.0% | 85.4% | 8.2% | 897 ms |
| mistral | 100.0% | — | 0.0% | 645 ms |
| openai | 99.5% | 99.5% | 0.0% | 850 ms |
| openrouter | 100.0% | — | 0.0% | 1376 ms |
| xai | 100.0% | — | 0.0% | 763 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 20 | 20 | 0 | 0 | 100.0% | 80 s | 2 min |
| gemini | 10 | 10 | 0 | 0 | 100.0% | 85 s | 107 s |
| mistral | 10 | 10 | 0 | 0 | 90.0% | 53 s | 45 min |
| openai | 20 | 20 | 0 | 0 | 85.0% | 68 s | 79 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
