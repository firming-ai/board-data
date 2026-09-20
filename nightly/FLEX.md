# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 10 day(s) (2026-09-11 → 2026-09-20). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 55 | 67% | 20% | 4.5/33.3s | 4.3/5.0s | 65.3s | 0.85 | OPEN |
| gemini/gemini-3.5-flash | 55 | 87% | 13% | 2.8/17.9s | 2.1/2.3s | 31.5s | 0.66 | DEALER |
| gemini/gemini-3.5-flash-lite | 55 | 100% | 0% | 0.8/2.8s | 0.7/0.8s | 2.8s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 55 | 51% | 44% | 5.4/23.7s | 1.7/2.3s | 61.3s | 0.91 | CHECKBOX |
| openai/gpt-5.6-luna | 55 | 98% | 0% | 2.8/12.8s | 2.8/4.3s | 12.8s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 55 | 76% | 0% | 3.3/9.4s | 3.1/3.9s | 8.6s | 0.78 | OPEN |
| openai/gpt-5.6-terra | 55 | 98% | 0% | 2.5/3.4s | 2.7/3.3s | 3.9s | 0.53 | DEALER |
| **pooled** | 385 | 83% | 11% | 2.8/13.3s | 2.3/4.5s | 24.5s | 0.71 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.9058 USD.
