# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 23 day(s) (2026-09-11 → 2026-10-03). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 337 | 68% | 26% | 4.6/59.1s | 4.3/5.2s | 64.0s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 337 | 73% | 24% | 8.5/48.4s | 2.3/2.6s | 53.1s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 337 | 96% | 3% | 0.9/14.8s | 1.0/1.2s | 20.6s | 0.61 | DEALER |
| gemini/gemini-3.7-flash | 337 | 34% | 64% | 4.9/33.5s | 2.3/3.9s | 40.3s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 337 | 18% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 337 | 14% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.57 | CHECKBOX |
| openai/gpt-5.6-terra | 337 | 18% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 2359 | 46% | 17% | 3.5/34.9s | 2.3/4.7s | 43.3s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 8.0407 USD.
