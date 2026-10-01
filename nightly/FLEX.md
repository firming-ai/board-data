# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 21 day(s) (2026-09-11 → 2026-10-01). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 291 | 67% | 27% | 4.6/59.5s | 4.3/5.2s | 64.0s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 291 | 71% | 25% | 9.3/50.3s | 2.3/2.5s | 53.5s | 0.80 | OPEN |
| gemini/gemini-3.5-flash-lite | 291 | 95% | 3% | 0.9/19.4s | 1.0/1.2s | 24.7s | 0.63 | DEALER |
| gemini/gemini-3.7-flash | 291 | 33% | 65% | 4.7/29.9s | 2.2/3.2s | 33.7s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 291 | 21% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 291 | 16% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.58 | CHECKBOX |
| openai/gpt-5.6-terra | 291 | 21% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 2037 | 46% | 17% | 3.5/34.4s | 2.3/4.6s | 43.3s | 0.74 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 6.8844 USD.
