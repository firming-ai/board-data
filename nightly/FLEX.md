# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 36 day(s) (2026-09-11 → 2026-10-16). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 658 | 59% | 28% | 5.0/68.2s | 4.5/7.3s | 64.4s | 0.88 | CHECKBOX |
| gemini/gemini-3.5-flash | 658 | 72% | 20% | 3.3/37.0s | 2.3/3.0s | 46.8s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 658 | 89% | 3% | 0.9/12.7s | 1.1/1.5s | 14.6s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 658 | 35% | 55% | 6.5/86.3s | 2.5/4.9s | 61.6s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 658 | 30% | 0% | 1.3/4.8s | 1.2/3.3s | 5.4s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 658 | 28% | 0% | 1.6/9.7s | 1.4/3.6s | 9.7s | 0.55 | CHECKBOX |
| openai/gpt-5.6-terra | 658 | 31% | 0% | 1.1/3.0s | 1.3/3.1s | 3.0s | 0.50 | CHECKBOX |
| **pooled** | 4606 | 49% | 15% | 2.6/41.0s | 2.3/5.0s | 50.9s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 14.6207 USD.
