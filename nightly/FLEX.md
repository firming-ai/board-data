# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 14 day(s) (2026-09-11 → 2026-09-24). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 121 | 63% | 30% | 4.6/36.3s | 4.3/4.9s | 64.4s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 121 | 80% | 17% | 3.7/52.1s | 2.2/2.6s | 61.9s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 121 | 95% | 2% | 0.8/24.4s | 0.8/1.1s | 26.5s | 0.62 | DEALER |
| gemini/gemini-3.7-flash | 121 | 37% | 60% | 5.0/24.0s | 1.8/2.7s | 35.1s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 121 | 50% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.52 | CHECKBOX |
| openai/gpt-5.6-sol | 121 | 38% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.66 | CHECKBOX |
| openai/gpt-5.6-terra | 121 | 50% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | OPEN |
| **pooled** | 847 | 59% | 16% | 2.9/23.6s | 2.2/4.6s | 35.5s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 2.5918 USD.
