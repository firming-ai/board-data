# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 59 day(s) (2026-09-11 → 2026-11-08). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1210 | 53% | 35% | 5.2/79.6s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1210 | 82% | 14% | 3.1/30.1s | 2.7/3.3s | 34.9s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1210 | 94% | 2% | 1.1/14.6s | 1.2/1.5s | 15.4s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1210 | 28% | 53% | 12.1/135.4s | 3.3/5.1s | 63.7s | 1.07 | CHECKBOX |
| openai/gpt-5.6-luna | 754 | 99% | 0% | 1.2/5.3s | 1.2/2.6s | 5.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 754 | 96% | 0% | 1.4/5.7s | 1.4/3.0s | 6.7s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 754 | 100% | 0% | 1.1/2.6s | 1.2/2.5s | 2.6s | 0.51 | DEALER |
| **pooled** | 7102 | 75% | 18% | 1.9/39.9s | 2.1/5.0s | 62.2s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 18.3037 USD.
