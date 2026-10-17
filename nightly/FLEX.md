# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 37 day(s) (2026-09-11 → 2026-10-17). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 681 | 58% | 29% | 5.0/68.0s | 4.5/8.0s | 64.4s | 0.89 | CHECKBOX |
| gemini/gemini-3.5-flash | 681 | 73% | 19% | 3.2/36.1s | 2.4/3.1s | 43.9s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 681 | 90% | 3% | 1.0/12.6s | 1.1/1.5s | 14.4s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 681 | 36% | 54% | 6.2/88.8s | 2.5/4.8s | 61.9s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 681 | 32% | 0% | 1.3/4.7s | 1.2/3.2s | 5.2s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 681 | 30% | 0% | 1.5/9.4s | 1.4/3.6s | 9.4s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 681 | 33% | 0% | 1.1/2.9s | 1.3/3.1s | 3.0s | 0.50 | CHECKBOX |
| **pooled** | 4767 | 50% | 15% | 2.5/40.1s | 2.3/5.0s | 51.9s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.0281 USD.
