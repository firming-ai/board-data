# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 58 day(s) (2026-09-11 → 2026-11-07). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1186 | 53% | 36% | 5.3/74.6s | 4.4/8.3s | 64.3s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1186 | 82% | 14% | 3.1/31.0s | 2.7/3.3s | 35.0s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1186 | 93% | 2% | 1.1/14.9s | 1.2/1.5s | 15.5s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1186 | 29% | 53% | 11.5/135.2s | 3.3/5.2s | 63.7s | 1.07 | CHECKBOX |
| openai/gpt-5.6-luna | 730 | 98% | 0% | 1.2/5.3s | 1.2/2.6s | 5.4s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 730 | 96% | 0% | 1.4/5.9s | 1.4/3.0s | 6.8s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 730 | 100% | 0% | 1.1/2.6s | 1.2/2.5s | 2.7s | 0.51 | DEALER |
| **pooled** | 6934 | 75% | 18% | 1.9/39.5s | 2.1/5.0s | 62.1s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 17.8872 USD.
