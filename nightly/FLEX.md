# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 52 day(s) (2026-09-11 → 2026-11-01). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1043 | 52% | 37% | 5.2/71.7s | 4.4/8.5s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 1043 | 80% | 15% | 3.1/33.5s | 2.6/3.3s | 36.1s | 0.71 | OPEN |
| gemini/gemini-3.5-flash-lite | 1043 | 93% | 3% | 1.1/14.6s | 1.1/1.5s | 15.2s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 1043 | 32% | 51% | 10.7/130.0s | 3.2/5.1s | 63.7s | 1.05 | CHECKBOX |
| openai/gpt-5.6-luna | 587 | 99% | 0% | 1.2/4.5s | 1.2/2.8s | 4.6s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 587 | 96% | 0% | 1.4/6.3s | 1.4/3.1s | 7.0s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 587 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.7s | 0.51 | DEALER |
| **pooled** | 5933 | 74% | 19% | 2.0/41.0s | 2.1/5.0s | 61.1s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.3711 USD.
