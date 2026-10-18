# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 38 day(s) (2026-09-11 → 2026-10-18). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 696 | 56% | 30% | 5.0/69.8s | 4.5/8.2s | 64.4s | 0.89 | CHECKBOX |
| gemini/gemini-3.5-flash | 696 | 73% | 19% | 3.2/36.1s | 2.4/3.1s | 43.4s | 0.75 | OPEN |
| gemini/gemini-3.5-flash-lite | 696 | 90% | 3% | 1.0/12.2s | 1.1/1.5s | 13.7s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 696 | 36% | 53% | 6.2/88.1s | 2.6/4.8s | 61.8s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 696 | 34% | 0% | 1.3/4.6s | 1.2/3.1s | 5.1s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 696 | 31% | 0% | 1.5/9.3s | 1.4/3.5s | 9.3s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 696 | 34% | 0% | 1.1/2.9s | 1.2/3.1s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 4872 | 51% | 15% | 2.5/39.6s | 2.3/5.0s | 51.0s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.3092 USD.
