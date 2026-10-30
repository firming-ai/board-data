# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 50 day(s) (2026-09-11 → 2026-10-30). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 995 | 51% | 37% | 5.2/72.7s | 4.5/8.9s | 64.3s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 995 | 79% | 15% | 3.0/34.0s | 2.6/3.3s | 37.1s | 0.71 | OPEN |
| gemini/gemini-3.5-flash-lite | 995 | 92% | 3% | 1.1/14.8s | 1.1/1.5s | 15.7s | 0.58 | DEALER |
| gemini/gemini-3.7-flash | 995 | 32% | 51% | 9.4/130.0s | 3.1/5.1s | 63.6s | 1.04 | CHECKBOX |
| openai/gpt-5.6-luna | 539 | 99% | 0% | 1.2/4.5s | 1.2/2.9s | 4.5s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 539 | 96% | 0% | 1.4/7.1s | 1.4/3.1s | 7.1s | 0.56 | DEALER |
| openai/gpt-5.6-terra | 539 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.8s | 0.51 | DEALER |
| **pooled** | 5597 | 74% | 19% | 2.1/40.4s | 2.2/5.0s | 61.0s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 14.5423 USD.
