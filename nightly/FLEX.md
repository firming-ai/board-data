# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 22 day(s) (2026-09-11 → 2026-10-02). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 323 | 67% | 27% | 4.7/59.4s | 4.3/5.1s | 64.1s | 0.84 | OPEN |
| gemini/gemini-3.5-flash | 323 | 72% | 24% | 8.7/49.5s | 2.3/2.6s | 52.8s | 0.79 | OPEN |
| gemini/gemini-3.5-flash-lite | 323 | 95% | 3% | 0.9/15.5s | 1.0/1.2s | 21.6s | 0.61 | DEALER |
| gemini/gemini-3.7-flash | 323 | 34% | 65% | 4.7/36.0s | 2.2/3.6s | 40.8s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 323 | 19% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 323 | 14% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.57 | CHECKBOX |
| openai/gpt-5.6-terra | 323 | 19% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 2261 | 46% | 17% | 3.5/36.2s | 2.3/4.7s | 43.8s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 7.6904 USD.
