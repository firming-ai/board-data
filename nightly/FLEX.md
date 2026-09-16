# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 6 day(s) (2026-09-11 → 2026-09-16). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 29 | 72% | 10% | 4.5/83.0s | 4.0/4.7s | 65.7s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 29 | 97% | 3% | 2.0/10.3s | 2.0/2.2s | 22.3s | 0.55 | DEALER |
| gemini/gemini-3.5-flash-lite | 29 | 100% | 0% | 0.8/2.1s | 0.7/0.8s | 2.1s | 0.50 | DEALER |
| gemini/gemini-3.7-flash | 29 | 55% | 41% | 4.2/22.8s | 1.7/1.8s | 46.8s | 0.86 | CHECKBOX |
| openai/gpt-5.6-luna | 29 | 97% | 0% | 3.2/13.1s | 2.9/3.4s | 13.0s | 0.54 | DEALER |
| openai/gpt-5.6-sol | 29 | 72% | 0% | 3.5/9.5s | 3.2/3.9s | 9.0s | 0.81 | OPEN |
| openai/gpt-5.6-terra | 29 | 97% | 0% | 2.7/3.6s | 3.0/3.3s | 4.0s | 0.56 | DEALER |
| **pooled** | 203 | 84% | 8% | 2.8/13.4s | 2.3/4.3s | 24.2s | 0.72 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 0.4911 USD.
