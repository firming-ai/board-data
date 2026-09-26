# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 16 day(s) (2026-09-11 → 2026-09-26). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 168 | 60% | 35% | 4.6/33.3s | 4.3/5.2s | 63.9s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 168 | 74% | 23% | 6.4/48.2s | 2.3/2.5s | 59.8s | 0.78 | OPEN |
| gemini/gemini-3.5-flash-lite | 168 | 95% | 3% | 0.8/31.0s | 0.9/1.1s | 33.0s | 0.62 | DEALER |
| gemini/gemini-3.7-flash | 168 | 34% | 64% | 4.7/22.7s | 2.0/2.9s | 32.1s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 168 | 36% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.52 | CHECKBOX |
| openai/gpt-5.6-sol | 168 | 27% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.62 | CHECKBOX |
| openai/gpt-5.6-terra | 168 | 36% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1176 | 52% | 18% | 3.0/25.4s | 2.2/4.6s | 35.0s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 3.7829 USD.
