# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 56 day(s) (2026-09-11 → 2026-11-05). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1139 | 52% | 37% | 5.2/74.6s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1139 | 81% | 14% | 3.1/32.3s | 2.6/3.3s | 35.5s | 0.70 | DEALER |
| gemini/gemini-3.5-flash-lite | 1139 | 93% | 2% | 1.1/15.4s | 1.2/1.5s | 16.4s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1139 | 29% | 53% | 10.9/130.4s | 3.2/5.2s | 63.7s | 1.06 | CHECKBOX |
| openai/gpt-5.6-luna | 683 | 98% | 0% | 1.2/4.9s | 1.2/2.6s | 5.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 683 | 96% | 0% | 1.4/5.7s | 1.4/3.0s | 6.7s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 683 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6605 | 74% | 18% | 1.9/39.6s | 2.1/5.0s | 61.9s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 17.0818 USD.
