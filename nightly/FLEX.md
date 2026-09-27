# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 17 day(s) (2026-09-11 → 2026-09-27). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 193 | 64% | 30% | 4.6/59.4s | 4.3/5.1s | 63.8s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 193 | 73% | 24% | 7.3/40.8s | 2.3/2.5s | 53.6s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 193 | 95% | 3% | 0.8/26.1s | 0.9/1.2s | 28.4s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 193 | 35% | 63% | 4.5/19.8s | 2.0/2.8s | 30.5s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 193 | 31% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 193 | 24% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.61 | CHECKBOX |
| openai/gpt-5.6-terra | 193 | 32% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1351 | 51% | 17% | 3.1/26.6s | 2.2/4.6s | 34.5s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 4.4156 USD.
