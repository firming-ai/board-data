# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 17 day(s) (2026-09-11 → 2026-09-27). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 202 | 64% | 30% | 4.5/60.2s | 4.3/5.1s | 63.9s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 202 | 73% | 24% | 7.3/50.6s | 2.3/2.5s | 52.9s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 202 | 96% | 2% | 0.8/25.7s | 0.9/1.2s | 26.4s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 202 | 37% | 62% | 4.3/19.4s | 2.0/2.8s | 29.4s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 202 | 30% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 202 | 23% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.60 | CHECKBOX |
| openai/gpt-5.6-terra | 202 | 30% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1414 | 50% | 17% | 3.2/28.7s | 2.2/4.6s | 36.2s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 4.6408 USD.
