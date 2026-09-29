# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 19 day(s) (2026-09-11 → 2026-09-29). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 242 | 67% | 28% | 4.5/59.4s | 4.3/4.9s | 63.9s | 0.82 | OPEN |
| gemini/gemini-3.5-flash | 242 | 69% | 27% | 8.4/50.6s | 2.3/2.5s | 54.0s | 0.80 | OPEN |
| gemini/gemini-3.5-flash-lite | 242 | 94% | 4% | 0.8/22.9s | 1.0/1.2s | 31.0s | 0.65 | DEALER |
| gemini/gemini-3.7-flash | 242 | 36% | 62% | 4.7/26.8s | 2.1/3.0s | 29.6s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 242 | 25% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 242 | 19% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.59 | CHECKBOX |
| openai/gpt-5.6-terra | 242 | 25% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1694 | 48% | 17% | 3.4/29.7s | 2.3/4.6s | 39.5s | 0.74 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 5.6566 USD.
