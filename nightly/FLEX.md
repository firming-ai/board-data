# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 57 day(s) (2026-09-11 → 2026-11-06). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1154 | 52% | 36% | 5.2/73.0s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1154 | 81% | 14% | 3.1/31.7s | 2.6/3.3s | 35.5s | 0.70 | DEALER |
| gemini/gemini-3.5-flash-lite | 1154 | 93% | 2% | 1.1/15.2s | 1.2/1.5s | 16.2s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1154 | 29% | 53% | 10.9/131.3s | 3.3/5.2s | 63.7s | 1.06 | CHECKBOX |
| openai/gpt-5.6-luna | 698 | 98% | 0% | 1.2/5.0s | 1.2/2.6s | 5.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 698 | 96% | 0% | 1.4/5.8s | 1.4/3.0s | 6.8s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 698 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6710 | 75% | 18% | 1.9/39.5s | 2.1/5.0s | 62.0s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 17.3321 USD.
