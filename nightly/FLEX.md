# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 6 day(s) (2026-09-11 → 2026-09-16). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 32 | 72% | 12% | 4.5/77.0s | 4.0/4.8s | 65.7s | 0.89 | CHECKBOX |
| gemini/gemini-3.5-flash | 32 | 94% | 6% | 2.0/10.0s | 2.1/2.3s | 19.5s | 0.58 | DEALER |
| gemini/gemini-3.5-flash-lite | 32 | 100% | 0% | 0.8/7.9s | 0.7/0.8s | 7.9s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 32 | 50% | 44% | 4.2/22.8s | 1.7/1.8s | 61.4s | 0.90 | CHECKBOX |
| openai/gpt-5.6-luna | 32 | 97% | 0% | 3.3/13.8s | 2.9/3.4s | 13.8s | 0.53 | DEALER |
| openai/gpt-5.6-sol | 32 | 72% | 0% | 3.5/9.3s | 3.2/4.0s | 8.8s | 0.80 | OPEN |
| openai/gpt-5.6-terra | 32 | 97% | 0% | 2.7/3.5s | 2.9/3.3s | 4.0s | 0.55 | DEALER |
| **pooled** | 224 | 83% | 9% | 2.9/14.5s | 2.6/4.3s | 26.7s | 0.72 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.5632 USD.
