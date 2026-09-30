# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 20 day(s) (2026-09-11 → 2026-09-30). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 266 | 67% | 27% | 4.6/59.5s | 4.3/5.1s | 64.0s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 266 | 70% | 26% | 8.7/52.4s | 2.3/2.5s | 55.4s | 0.81 | OPEN |
| gemini/gemini-3.5-flash-lite | 266 | 94% | 3% | 0.9/20.8s | 1.0/1.2s | 26.2s | 0.64 | DEALER |
| gemini/gemini-3.7-flash | 266 | 34% | 64% | 4.7/30.6s | 2.1/3.1s | 37.1s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 266 | 23% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 266 | 17% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.58 | CHECKBOX |
| openai/gpt-5.6-terra | 266 | 23% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1862 | 47% | 17% | 3.5/35.9s | 2.3/4.6s | 43.9s | 0.74 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 6.2689 USD.
