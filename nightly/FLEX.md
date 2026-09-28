# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 18 day(s) (2026-09-11 → 2026-09-28). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 220 | 66% | 28% | 4.5/59.3s | 4.3/5.0s | 63.7s | 0.82 | OPEN |
| gemini/gemini-3.5-flash | 220 | 70% | 26% | 8.3/52.1s | 2.3/2.6s | 54.1s | 0.79 | OPEN |
| gemini/gemini-3.5-flash-lite | 220 | 94% | 3% | 0.8/24.7s | 1.0/1.2s | 31.4s | 0.65 | DEALER |
| gemini/gemini-3.7-flash | 220 | 37% | 61% | 4.5/24.2s | 2.0/2.9s | 29.8s | 0.95 | CHECKBOX |
| openai/gpt-5.6-luna | 220 | 27% | 0% | 2.8/13.4s | 2.6/4.2s | 13.3s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 220 | 21% | 0% | 3.2/9.1s | 3.0/3.9s | 8.2s | 0.60 | CHECKBOX |
| openai/gpt-5.6-terra | 220 | 28% | 0% | 2.4/3.2s | 2.6/3.3s | 3.8s | 0.51 | CHECKBOX |
| **pooled** | 1540 | 49% | 17% | 3.3/29.3s | 2.3/4.6s | 40.1s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 5.0965 USD.
