# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 54 day(s) (2026-09-11 → 2026-11-03). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1083 | 52% | 37% | 5.2/75.1s | 4.4/8.3s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 1083 | 81% | 14% | 3.0/32.5s | 2.6/3.3s | 35.5s | 0.70 | OPEN |
| gemini/gemini-3.5-flash-lite | 1083 | 93% | 2% | 1.1/14.7s | 1.2/1.5s | 15.4s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1083 | 31% | 51% | 10.8/130.5s | 3.2/5.1s | 63.7s | 1.05 | CHECKBOX |
| openai/gpt-5.6-luna | 627 | 98% | 0% | 1.2/4.7s | 1.2/2.7s | 5.0s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 627 | 96% | 0% | 1.4/5.8s | 1.4/3.1s | 6.8s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 627 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6213 | 74% | 18% | 1.9/40.8s | 2.1/5.0s | 61.7s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.0715 USD.
