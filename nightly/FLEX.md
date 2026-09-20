# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 10 day(s) (2026-09-11 → 2026-09-20). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 52 | 65% | 21% | 4.4/42.7s | 4.3/5.0s | 65.5s | 0.86 | CHECKBOX |
| gemini/gemini-3.5-flash | 52 | 87% | 13% | 2.8/18.7s | 2.1/2.3s | 32.3s | 0.67 | DEALER |
| gemini/gemini-3.5-flash-lite | 52 | 100% | 0% | 0.7/3.0s | 0.7/0.8s | 3.0s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 52 | 48% | 46% | 6.2/24.0s | 1.7/2.3s | 61.4s | 0.93 | CHECKBOX |
| openai/gpt-5.6-luna | 52 | 98% | 0% | 2.9/13.0s | 2.9/4.3s | 12.9s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 52 | 75% | 0% | 3.4/9.7s | 3.1/3.9s | 8.8s | 0.79 | OPEN |
| openai/gpt-5.6-terra | 52 | 98% | 0% | 2.5/3.5s | 2.7/3.3s | 4.0s | 0.53 | DEALER |
| **pooled** | 364 | 82% | 12% | 2.8/13.5s | 2.3/4.5s | 25.3s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.8610 USD.
