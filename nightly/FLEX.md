# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 54 day(s) (2026-09-11 → 2026-11-03). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1070 | 52% | 36% | 5.2/75.5s | 4.4/8.3s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 1070 | 80% | 15% | 3.0/32.6s | 2.6/3.3s | 35.7s | 0.70 | OPEN |
| gemini/gemini-3.5-flash-lite | 1070 | 93% | 3% | 1.1/14.6s | 1.1/1.5s | 15.4s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 1070 | 31% | 51% | 10.8/130.5s | 3.2/5.1s | 63.7s | 1.05 | CHECKBOX |
| openai/gpt-5.6-luna | 614 | 99% | 0% | 1.2/4.6s | 1.2/2.7s | 4.8s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 614 | 96% | 0% | 1.4/5.9s | 1.4/3.1s | 6.8s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 614 | 100% | 0% | 1.1/2.7s | 1.2/2.6s | 2.7s | 0.51 | DEALER |
| **pooled** | 6122 | 74% | 18% | 2.0/41.0s | 2.1/5.0s | 61.6s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.8402 USD.
