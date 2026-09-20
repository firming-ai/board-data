# FILL — the inference availability index

*As of 2026-09-20T05:05:01+00:00 · probe pulse-1.2.1 · methodology 1.2.0*

**FILL 95.1** · FILL·FLEX 85.3

Share of frontier discount-lane work that got its discount inside the budget — flex inside 60 s, batch inside 1 h, a warm prompt served from the cache — the mean of OAI·FILL, ANT·FILL and GEM·FILL. FILL·FLEX is the flex leg alone (last five minutes, n = 34.0): the headline before methodology 1.2.

| child | FILL | flex (60 s, 5 min) | batch (1 h, 24 h) | cache (warm hit, 1 h) |
| :-- | --: | --: | --: | --: |
| ANT·FILL | 100.0% | — | 100.0% (n=96) | 100.0% (n=30) |
| GEM·FILL | 85.3% | 70.6% (n=17) | 100.0% (n=48) | — |
| MIS·FILL | 100.0% | — | 100.0% (n=48) | — |
| OAI·FILL | 100.0% | 100.0% (n=17) | 100.0% (n=96) | 100.0% (n=15) |

| lane | n | fill@60 | shed | TTFT p50 | gap |
| :-- | --: | --: | --: | --: | :-: |
| anthropic/claude-fable-5-1/standard | 12 | 100.0% | 0.0% | 1461 ms |  |
| anthropic/claude-haiku-4-5/cache | 15 | 100.0% | 0.0% | 799 ms |  |
| anthropic/claude-haiku-4-5/standard | 60 | 100.0% | 0.0% | 708 ms |  |
| anthropic/claude-opus-4-8/standard | 4 | 100.0% | 0.0% | 1223 ms |  |
| anthropic/claude-opus-5/standard | 60 | 100.0% | 0.0% | 1177 ms |  |
| anthropic/claude-sonnet-4-6/standard | 4 | 100.0% | 0.0% | 1301 ms |  |
| anthropic/claude-sonnet-5/cache | 15 | 100.0% | 0.0% | 1795 ms |  |
| anthropic/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1011 ms |  |
| deepseek/deepseek-flash/standard | 12 | 100.0% | 0.0% | 1104 ms |  |
| deepseek/deepseek-v4-flash/standard | 60 | 100.0% | 0.0% | 976 ms |  |
| deepseek/deepseek-v4-pro/standard | 60 | 100.0% | 0.0% | 1187 ms |  |
| gemini/gemini-3.1-pro-preview/flex | 2 | — | — | — ms |  |
| gemini/gemini-3.1-pro-preview/standard | 2 | 100.0% | 0.0% | 2329 ms |  |
| gemini/gemini-3.5-flash-lite/flex | 60 | 100.0% | 0.0% | 745 ms |  |
| gemini/gemini-3.5-flash-lite/standard | 60 | 100.0% | 0.0% | 733 ms |  |
| gemini/gemini-3.5-flash/flex | 60 | 98.3% | 1.7% | 9828 ms |  |
| gemini/gemini-3.5-flash/standard | 60 | 100.0% | 0.0% | 949 ms |  |
| gemini/gemini-3.6-flash/standard | 4 | 100.0% | 0.0% | 1518 ms |  |
| gemini/gemini-3.7-flash/flex | 60 | 61.7% | 38.3% | 3771 ms |  |
| gemini/gemini-3.7-flash/standard | 12 | 100.0% | 0.0% | 1301 ms |  |
| gemini/gemini-3.8-flash/flex | 12 | 91.7% | 0.0% | 4661 ms |  |
| gemini/gemini-3.8-flash/standard | 12 | 100.0% | 0.0% | 1250 ms |  |
| mistral/mistral-large/standard | 60 | 100.0% | 0.0% | 677 ms |  |
| mistral/mistral-small/standard | 60 | 100.0% | 0.0% | 598 ms |  |
| openai/gpt-4.1/standard | 4 | 100.0% | 0.0% | 966 ms |  |
| openai/gpt-5.5/flex | 12 | 100.0% | 0.0% | 926 ms |  |
| openai/gpt-5.5/standard | 12 | 100.0% | 0.0% | 1053 ms |  |
| openai/gpt-5.6-luna/cache | 15 | 100.0% | 0.0% | 777 ms |  |
| openai/gpt-5.6-luna/flex | 60 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-luna/priority | 60 | 100.0% | 0.0% | 666 ms |  |
| openai/gpt-5.6-luna/standard | 60 | 100.0% | 0.0% | 770 ms |  |
| openai/gpt-5.6-sol/flex | 60 | 88.3% | 0.0% | 1201 ms |  |
| openai/gpt-5.6-sol/standard | 60 | 100.0% | 0.0% | 895 ms |  |
| openai/gpt-5.6-terra/flex | 60 | 100.0% | 0.0% | 757 ms |  |
| openai/gpt-5.6-terra/priority | 12 | 100.0% | 0.0% | 805 ms |  |
| openai/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 743 ms |  |
| openai/gpt-5/standard | 4 | 100.0% | 0.0% | 1091 ms |  |
| openai/gpt-6-astra/flex | 12 | 100.0% | 0.0% | 1152 ms |  |
| openai/gpt-6-astra/standard | 12 | 100.0% | 0.0% | 1393 ms |  |
| openrouter/claude-sonnet-5/standard | 60 | 100.0% | 0.0% | 1586 ms |  |
| openrouter/gemini-3.7-flash/standard | 60 | 100.0% | 0.0% | 1615 ms |  |
| openrouter/gpt-5.6-terra/standard | 60 | 100.0% | 0.0% | 934 ms |  |
| xai/grok-4.20/standard | 60 | 100.0% | 0.0% | 723 ms |  |
| xai/grok-4.5/standard | 4 | 100.0% | 0.0% | 1314 ms |  |

**Every venue, last complete hour** — AVAIL is the standard lane; FILL the discount lane.

| venue | AVAIL | FILL | shed | TTFT p50 |
| :-- | --: | --: | --: | --: |
| anthropic | 100.0% | — | 0.0% | 1005 ms |
| deepseek | 100.0% | — | 0.0% | 1078 ms |
| gemini | 100.0% | 87.0% | 7.0% | 892 ms |
| mistral | 100.0% | — | 0.0% | 640 ms |
| openai | 100.0% | 96.6% | 0.0% | 804 ms |
| openrouter | 100.0% | — | 0.0% | 1382 ms |
| xai | 100.0% | — | 0.0% | 733 ms |

**Batch, last 24 h of submits** — one one-request job per lane every 30 min, polled to its end.

| venue | submitted | done | open | lost | done in 1 h | turnaround p50 | p95 |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| anthropic | 96 | 96 | 0 | 0 | 100.0% | 86 s | 2 min |
| gemini | 48 | 48 | 0 | 0 | 100.0% | 85 s | 113 s |
| mistral | 48 | 48 | 0 | 0 | 100.0% | 34 s | 15 min |
| openai | 96 | 96 | 0 | 0 | 100.0% | 68 s | 18 min |

Every number carries n; a gap flag marks an hour with fewer than 55 samples. Marks are struck once at 00:10Z and never restated. Methodology: METHODOLOGY.md.
