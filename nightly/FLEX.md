# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 33 day(s) (2026-09-11 → 2026-10-13). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 565 | 66% | 26% | 4.9/68.1s | 4.5/6.0s | 64.3s | 0.87 | CHECKBOX |
| gemini/gemini-3.5-flash | 565 | 77% | 21% | 3.4/38.3s | 2.3/2.9s | 46.2s | 0.75 | OPEN |
| gemini/gemini-3.5-flash-lite | 565 | 96% | 2% | 0.9/12.6s | 1.0/1.4s | 14.3s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 565 | 38% | 58% | 6.2/76.1s | 2.4/4.9s | 61.3s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 565 | 19% | 0% | 1.6/6.7s | 1.3/3.5s | 6.6s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 565 | 16% | 0% | 1.8/8.6s | 1.4/3.9s | 7.9s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 565 | 19% | 0% | 1.2/3.1s | 1.3/3.2s | 3.2s | 0.50 | CHECKBOX |
| **pooled** | 3955 | 47% | 15% | 2.9/42.8s | 2.3/5.0s | 53.8s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.4034 USD.
