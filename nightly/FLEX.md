# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 16 day(s) (2026-09-11 → 2026-09-26). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 178 | 62% | 33% | 4.6/41.3s | 4.3/5.2s | 63.8s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 178 | 73% | 24% | 6.6/45.4s | 2.3/2.5s | 56.8s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 178 | 95% | 3% | 0.8/28.6s | 0.9/1.1s | 31.6s | 0.61 | DEALER |
| gemini/gemini-3.7-flash | 178 | 33% | 65% | 4.6/22.4s | 2.0/2.9s | 31.9s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 178 | 34% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 178 | 26% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.62 | CHECKBOX |
| openai/gpt-5.6-terra | 178 | 34% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1246 | 51% | 18% | 3.0/25.9s | 2.2/4.6s | 34.5s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 4.0508 USD.
