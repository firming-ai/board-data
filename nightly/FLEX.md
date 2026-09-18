# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 8 day(s) (2026-09-11 → 2026-09-18). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 42 | 67% | 17% | 4.4/61.4s | 4.3/5.1s | 65.6s | 0.89 | CHECKBOX |
| gemini/gemini-3.5-flash | 42 | 86% | 14% | 2.1/15.6s | 2.1/2.3s | 29.2s | 0.66 | DEALER |
| gemini/gemini-3.5-flash-lite | 42 | 100% | 0% | 0.8/3.4s | 0.7/0.8s | 3.4s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 42 | 50% | 43% | 6.2/24.5s | 1.7/2.4s | 61.7s | 0.92 | CHECKBOX |
| openai/gpt-5.6-luna | 42 | 98% | 0% | 3.0/13.3s | 2.9/4.4s | 13.3s | 0.53 | DEALER |
| openai/gpt-5.6-sol | 42 | 69% | 0% | 3.5/10.9s | 3.2/4.0s | 9.4s | 0.82 | OPEN |
| openai/gpt-5.6-terra | 42 | 98% | 0% | 2.7/3.8s | 2.7/3.3s | 4.2s | 0.53 | DEALER |
| **pooled** | 294 | 81% | 11% | 2.9/14.3s | 2.6/4.6s | 30.8s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.7414 USD.
