# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 34 day(s) (2026-09-11 → 2026-10-14). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 601 | 64% | 27% | 5.0/68.7s | 4.5/7.1s | 64.4s | 0.87 | CHECKBOX |
| gemini/gemini-3.5-flash | 601 | 75% | 21% | 3.5/37.7s | 2.3/3.0s | 47.0s | 0.76 | OPEN |
| gemini/gemini-3.5-flash-lite | 601 | 94% | 3% | 0.9/13.1s | 1.1/1.4s | 14.7s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 601 | 37% | 58% | 6.2/87.7s | 2.5/4.9s | 61.7s | 0.97 | CHECKBOX |
| openai/gpt-5.6-luna | 601 | 23% | 0% | 1.4/6.3s | 1.2/3.4s | 6.1s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 601 | 21% | 0% | 1.8/10.1s | 1.4/3.8s | 9.6s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 601 | 24% | 0% | 1.2/3.0s | 1.2/3.2s | 3.1s | 0.50 | CHECKBOX |
| **pooled** | 4207 | 49% | 16% | 2.8/42.5s | 2.3/5.0s | 55.8s | 0.73 | CHECKBOX |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 13.9954 USD.
