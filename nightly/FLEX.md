# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 19 day(s) (2026-09-11 → 2026-09-29). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 251 | 66% | 28% | 4.5/59.3s | 4.3/4.9s | 63.9s | 0.83 | OPEN |
| gemini/gemini-3.5-flash | 251 | 69% | 27% | 8.4/52.9s | 2.3/2.5s | 58.8s | 0.81 | OPEN |
| gemini/gemini-3.5-flash-lite | 251 | 94% | 4% | 0.9/21.9s | 1.0/1.2s | 28.8s | 0.64 | DEALER |
| gemini/gemini-3.7-flash | 251 | 35% | 63% | 4.7/29.0s | 2.1/2.9s | 36.5s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 251 | 24% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 251 | 18% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.59 | CHECKBOX |
| openai/gpt-5.6-terra | 251 | 24% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1757 | 47% | 17% | 3.4/31.5s | 2.3/4.6s | 42.8s | 0.74 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 5.8937 USD.
