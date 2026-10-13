# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 33 day(s) (2026-09-11 → 2026-10-13). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 587 | 66% | 26% | 5.0/68.8s | 4.5/6.2s | 64.3s | 0.87 | CHECKBOX |
| gemini/gemini-3.5-flash | 587 | 76% | 21% | 3.5/37.9s | 2.3/2.9s | 46.9s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 587 | 96% | 3% | 0.9/12.8s | 1.1/1.4s | 14.6s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 587 | 38% | 58% | 6.2/82.4s | 2.5/4.9s | 61.6s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 587 | 22% | 0% | 1.5/6.7s | 1.2/3.4s | 6.6s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 587 | 20% | 0% | 1.8/8.8s | 1.4/3.8s | 8.6s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 587 | 22% | 0% | 1.2/3.0s | 1.3/3.2s | 3.1s | 0.50 | CHECKBOX |
| **pooled** | 4109 | 48% | 16% | 2.8/42.6s | 2.3/5.0s | 54.7s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.7996 USD.
