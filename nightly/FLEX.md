# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 40 day(s) (2026-09-11 → 2026-10-20). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 745 | 54% | 33% | 5.1/74.0s | 4.5/8.3s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 745 | 75% | 18% | 3.1/34.7s | 2.4/3.1s | 41.7s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 745 | 91% | 3% | 1.0/11.8s | 1.1/1.5s | 13.3s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 745 | 38% | 51% | 6.7/102.0s | 2.6/4.9s | 62.4s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 745 | 38% | 0% | 1.2/4.4s | 1.2/3.1s | 4.5s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 745 | 36% | 0% | 1.5/8.6s | 1.4/3.5s | 8.6s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 745 | 39% | 0% | 1.1/2.9s | 1.2/3.0s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5215 | 53% | 15% | 2.3/40.2s | 2.2/5.0s | 54.0s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.2272 USD.
