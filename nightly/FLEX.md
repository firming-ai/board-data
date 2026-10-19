# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 39 day(s) (2026-09-11 → 2026-10-19). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 731 | 54% | 33% | 5.1/71.6s | 4.5/8.3s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 731 | 75% | 18% | 3.1/35.0s | 2.4/3.1s | 42.1s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 731 | 90% | 3% | 1.0/12.0s | 1.1/1.5s | 13.4s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 731 | 38% | 52% | 6.4/89.2s | 2.6/4.9s | 62.1s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 731 | 37% | 0% | 1.2/4.5s | 1.2/3.1s | 4.6s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 731 | 35% | 0% | 1.5/8.7s | 1.4/3.5s | 8.7s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 731 | 37% | 0% | 1.1/2.9s | 1.2/3.0s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5117 | 52% | 15% | 2.4/39.5s | 2.3/5.0s | 52.4s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.9658 USD.
