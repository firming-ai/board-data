# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 39 day(s) (2026-09-11 → 2026-10-19). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 723 | 54% | 32% | 5.0/71.2s | 4.5/8.3s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 723 | 74% | 19% | 3.1/35.3s | 2.4/3.1s | 42.4s | 0.75 | OPEN |
| gemini/gemini-3.5-flash-lite | 723 | 90% | 3% | 1.0/11.8s | 1.1/1.5s | 13.3s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 723 | 38% | 52% | 6.2/88.0s | 2.6/4.8s | 61.9s | 0.96 | CHECKBOX |
| openai/gpt-5.6-luna | 723 | 36% | 0% | 1.2/4.5s | 1.2/3.1s | 4.6s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 723 | 34% | 0% | 1.5/8.7s | 1.4/3.5s | 8.7s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 723 | 37% | 0% | 1.1/2.9s | 1.2/3.0s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5061 | 52% | 15% | 2.4/39.5s | 2.3/5.0s | 52.3s | 0.73 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 15.8127 USD.
