# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 11 day(s) (2026-09-11 → 2026-09-21). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 61 | 70% | 18% | 4.4/26.6s | 4.3/5.0s | 65.1s | 0.81 | OPEN |
| gemini/gemini-3.5-flash | 61 | 85% | 15% | 2.8/21.0s | 2.1/2.3s | 29.7s | 0.67 | DEALER |
| gemini/gemini-3.5-flash-lite | 61 | 100% | 0% | 0.8/2.6s | 0.7/0.8s | 2.6s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 61 | 52% | 43% | 4.6/23.2s | 1.7/2.3s | 61.1s | 0.88 | CHECKBOX |
| openai/gpt-5.6-luna | 61 | 97% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.54 | DEALER |
| openai/gpt-5.6-sol | 61 | 74% | 0% | 3.2/9.2s | 3.1/3.9s | 8.2s | 0.78 | OPEN |
| openai/gpt-5.6-terra | 61 | 98% | 0% | 2.5/3.3s | 2.6/3.3s | 3.8s | 0.53 | DEALER |
| **pooled** | 427 | 82% | 11% | 2.7/13.4s | 2.1/4.5s | 22.5s | 0.70 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 1.0245 USD.
