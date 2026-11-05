# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 56 day(s) (2026-09-11 → 2026-11-05). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1131 | 52% | 37% | 5.2/74.8s | 4.4/8.3s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 1131 | 81% | 14% | 3.1/32.4s | 2.6/3.3s | 35.5s | 0.70 | DEALER |
| gemini/gemini-3.5-flash-lite | 1131 | 93% | 2% | 1.1/15.2s | 1.2/1.5s | 16.3s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1131 | 29% | 53% | 10.8/130.5s | 3.2/5.2s | 63.7s | 1.06 | CHECKBOX |
| openai/gpt-5.6-luna | 675 | 98% | 0% | 1.2/4.9s | 1.2/2.6s | 5.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 675 | 96% | 0% | 1.4/5.6s | 1.4/3.0s | 6.7s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 675 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6549 | 74% | 18% | 1.9/39.5s | 2.1/5.0s | 61.8s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.9323 USD.
