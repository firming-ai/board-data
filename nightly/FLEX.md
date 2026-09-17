# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 7 day(s) (2026-09-11 → 2026-09-17). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 36 | 72% | 11% | 4.4/67.6s | 4.3/5.1s | 65.7s | 0.87 | CHECKBOX |
| gemini/gemini-3.5-flash | 36 | 89% | 11% | 2.0/15.0s | 2.1/2.3s | 22.3s | 0.63 | DEALER |
| gemini/gemini-3.5-flash-lite | 36 | 100% | 0% | 0.8/5.9s | 0.7/0.8s | 5.9s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 36 | 47% | 47% | 4.7/25.9s | 1.7/2.4s | 61.3s | 0.89 | CHECKBOX |
| openai/gpt-5.6-luna | 36 | 97% | 0% | 3.0/13.6s | 2.9/4.4s | 13.6s | 0.53 | DEALER |
| openai/gpt-5.6-sol | 36 | 69% | 0% | 3.5/11.3s | 3.1/4.0s | 10.0s | 0.80 | OPEN |
| openai/gpt-5.6-terra | 36 | 97% | 0% | 2.7/3.4s | 2.8/3.3s | 3.9s | 0.54 | DEALER |
| **pooled** | 252 | 82% | 10% | 2.8/14.9s | 2.6/4.6s | 28.3s | 0.71 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.6676 USD.
