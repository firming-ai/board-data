# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 27 day(s) (2026-09-11 → 2026-10-07). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 434 | 67% | 26% | 4.8/63.7s | 4.4/5.4s | 64.1s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 434 | 73% | 25% | 8.5/41.2s | 2.3/2.7s | 48.4s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 434 | 96% | 2% | 0.9/13.5s | 1.0/1.3s | 15.3s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 434 | 35% | 64% | 4.9/33.9s | 2.3/4.0s | 37.8s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 434 | 14% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 434 | 11% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.55 | CHECKBOX |
| openai/gpt-5.6-terra | 434 | 14% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 3038 | 44% | 17% | 3.5/39.8s | 2.3/4.8s | 45.8s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 10.4867 USD.
