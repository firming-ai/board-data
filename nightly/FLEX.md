# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 63 day(s) (2026-09-11 → 2026-11-12). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 1307 | 54% | 34% | 5.3/89.4s | 4.4/8.4s | 64.4s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 1307 | 83% | 13% | 3.1/32.7s | 2.7/3.3s | 35.5s | 0.69 | DEALER |
| gemini/gemini-3.5-flash-lite | 1307 | 94% | 2% | 1.1/13.7s | 1.2/1.6s | 14.6s | 0.57 | DEALER |
| gemini/gemini-3.7-flash | 1307 | 27% | 52% | 12.8/141.0s | 3.3/5.2s | 63.8s | 1.09 | CHECKBOX |
| openai/gpt-5.6-luna | 851 | 99% | 0% | 1.2/5.5s | 1.2/2.5s | 5.6s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 851 | 96% | 0% | 1.4/5.4s | 1.4/3.0s | 6.0s | 0.55 | DEALER |
| openai/gpt-5.6-terra | 851 | 100% | 0% | 1.1/2.5s | 1.2/2.1s | 2.5s | 0.51 | DEALER |
| **pooled** | 7781 | 75% | 17% | 1.9/40.4s | 2.0/5.0s | 62.5s | 0.80 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 20.0224 USD.
