# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 26 day(s) (2026-09-11 → 2026-10-06). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 419 | 68% | 26% | 4.7/60.8s | 4.4/5.3s | 64.1s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 419 | 74% | 23% | 8.4/41.4s | 2.3/2.6s | 48.2s | 0.77 | OPEN |
| gemini/gemini-3.5-flash-lite | 419 | 96% | 2% | 0.9/14.2s | 1.0/1.3s | 16.5s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 419 | 34% | 64% | 4.7/35.5s | 2.3/4.1s | 37.0s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 419 | 14% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 419 | 11% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.55 | CHECKBOX |
| openai/gpt-5.6-terra | 419 | 15% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.50 | CHECKBOX |
| **pooled** | 2933 | 45% | 17% | 3.5/38.8s | 2.3/4.8s | 44.0s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 10.0908 USD.
