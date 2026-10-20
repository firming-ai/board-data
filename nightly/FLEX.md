# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 40 day(s) (2026-09-11 → 2026-10-20). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 754 | 53% | 34% | 5.1/79.2s | 4.5/8.4s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 754 | 75% | 18% | 3.1/34.9s | 2.4/3.1s | 42.0s | 0.74 | OPEN |
| gemini/gemini-3.5-flash-lite | 754 | 91% | 3% | 1.0/12.8s | 1.1/1.5s | 14.7s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 754 | 38% | 51% | 6.8/104.4s | 2.7/4.9s | 62.5s | 0.98 | CHECKBOX |
| openai/gpt-5.6-luna | 754 | 39% | 0% | 1.2/4.4s | 1.2/3.1s | 4.5s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 754 | 37% | 0% | 1.4/8.6s | 1.4/3.5s | 8.6s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 754 | 39% | 0% | 1.1/2.9s | 1.2/3.0s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5278 | 53% | 15% | 2.3/40.9s | 2.2/5.0s | 55.8s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 16.4023 USD.
