# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 42 day(s) (2026-09-11 → 2026-10-22). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 802 | 52% | 36% | 5.2/74.8s | 4.5/8.9s | 64.4s | 0.92 | CHECKBOX |
| gemini/gemini-3.5-flash | 802 | 76% | 17% | 3.1/34.8s | 2.4/3.1s | 41.8s | 0.73 | OPEN |
| gemini/gemini-3.5-flash-lite | 802 | 91% | 3% | 1.0/13.7s | 1.1/1.5s | 14.9s | 0.60 | DEALER |
| gemini/gemini-3.7-flash | 802 | 38% | 51% | 7.0/108.0s | 2.7/5.1s | 62.9s | 0.98 | CHECKBOX |
| openai/gpt-5.6-luna | 802 | 43% | 0% | 1.2/4.3s | 1.2/3.0s | 4.5s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 802 | 41% | 0% | 1.4/8.2s | 1.4/3.3s | 8.1s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 802 | 43% | 0% | 1.1/2.8s | 1.2/2.9s | 2.8s | 0.50 | CHECKBOX |
| **pooled** | 5614 | 55% | 15% | 2.3/40.2s | 2.2/5.0s | 52.8s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 17.2537 USD.
