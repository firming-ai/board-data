# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 54 day(s) (2026-09-11 → 2026-11-03). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1092 | 52% | 37% | 5.2/74.6s | 4.4/8.3s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 1092 | 81% | 14% | 3.0/32.3s | 2.6/3.3s | 35.5s | 0.70 | OPEN |
| gemini/gemini-3.5-flash-lite | 1092 | 93% | 2% | 1.1/15.2s | 1.2/1.5s | 15.8s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1092 | 30% | 52% | 10.8/130.5s | 3.2/5.1s | 63.7s | 1.06 | CHECKBOX |
| openai/gpt-5.6-luna | 636 | 98% | 0% | 1.2/4.9s | 1.2/2.7s | 5.3s | 0.53 | DEALER |
| openai/gpt-5.6-sol | 636 | 97% | 0% | 1.4/5.7s | 1.4/3.1s | 6.8s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 636 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6276 | 74% | 18% | 1.9/40.2s | 2.1/5.0s | 61.7s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.2289 USD.
