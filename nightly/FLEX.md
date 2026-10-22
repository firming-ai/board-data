# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 42 day(s) (2026-09-11 → 2026-10-22). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 793 | 52% | 35% | 5.2/75.5s | 4.5/8.6s | 64.5s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 793 | 76% | 17% | 3.1/35.0s | 2.4/3.1s | 42.0s | 0.73 | OPEN |
| gemini/gemini-3.5-flash-lite | 793 | 91% | 3% | 1.0/13.2s | 1.1/1.5s | 14.8s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 793 | 38% | 51% | 7.0/108.0s | 2.7/5.1s | 62.9s | 0.98 | CHECKBOX |
| openai/gpt-5.6-luna | 793 | 42% | 0% | 1.2/4.3s | 1.2/3.0s | 4.4s | 0.51 | CHECKBOX |
| openai/gpt-5.6-sol | 793 | 40% | 0% | 1.4/8.3s | 1.4/3.4s | 8.3s | 0.54 | CHECKBOX |
| openai/gpt-5.6-terra | 793 | 42% | 0% | 1.1/2.8s | 1.2/2.9s | 2.9s | 0.50 | CHECKBOX |
| **pooled** | 5551 | 54% | 15% | 2.3/40.3s | 2.2/5.0s | 52.8s | 0.74 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 17.0871 USD.
