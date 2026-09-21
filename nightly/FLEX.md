# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 11 day(s) (2026-09-11 → 2026-09-21). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 59 | 69% | 19% | 4.4/26.8s | 4.3/5.0s | 65.2s | 0.82 | OPEN |
| gemini/gemini-3.5-flash | 59 | 86% | 14% | 2.8/21.1s | 2.1/2.3s | 30.3s | 0.67 | DEALER |
| gemini/gemini-3.5-flash-lite | 59 | 100% | 0% | 0.8/2.7s | 0.7/0.8s | 2.7s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 59 | 53% | 42% | 4.7/23.3s | 1.7/2.3s | 61.2s | 0.89 | CHECKBOX |
| openai/gpt-5.6-luna | 59 | 98% | 0% | 2.8/12.7s | 2.7/4.3s | 12.6s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 59 | 75% | 0% | 3.2/9.3s | 3.1/3.9s | 8.3s | 0.79 | OPEN |
| openai/gpt-5.6-terra | 59 | 98% | 0% | 2.5/3.3s | 2.6/3.3s | 3.8s | 0.53 | DEALER |
| **pooled** | 413 | 83% | 11% | 2.7/13.3s | 2.1/4.5s | 23.0s | 0.71 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.9838 USD.
