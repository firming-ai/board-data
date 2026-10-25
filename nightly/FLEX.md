# Flex lanes — the dealer back-test

Daily flex probes across 7 lanes, 45 day(s) (2026-09-11 → 2026-10-25). Rescue fires at 60s. Percentiles and counts only; rows stay private.

| lane | attempts | fill@60s | shed | flex p50/p95 | ctrl p50/p95 | ladder p95 | blended | verdict |
| :-- | --: | --: | --: | --: | --: | --: | --: | :-- |
| gemini/gemini-3.1-pro-preview | 874 | 52% | 36% | 5.2/79.3s | 4.5/9.1s | 64.4s | 0.91 | CHECKBOX |
| gemini/gemini-3.5-flash | 874 | 78% | 16% | 3.0/33.6s | 2.5/3.1s | 39.6s | 0.72 | OPEN |
| gemini/gemini-3.5-flash-lite | 874 | 91% | 3% | 1.0/13.2s | 1.1/1.5s | 14.7s | 0.59 | DEALER |
| gemini/gemini-3.7-flash | 874 | 36% | 50% | 8.3/115.6s | 2.9/5.1s | 63.3s | 1.01 | CHECKBOX |
| openai/gpt-5.6-luna | 418 | 99% | 0% | 1.2/4.2s | 1.2/2.9s | 4.3s | 0.52 | DEALER |
| openai/gpt-5.6-sol | 418 | 95% | 0% | 1.5/8.0s | 1.3/3.2s | 8.0s | 0.57 | DEALER |
| openai/gpt-5.6-terra | 418 | 100% | 0% | 1.1/2.7s | 1.2/2.7s | 2.7s | 0.51 | DEALER |
| **pooled** | 4750 | 73% | 19% | 2.2/41.0s | 2.2/5.0s | 58.8s | 0.79 | OPEN |

Verdict rule (pre-committed): DEALER when fill@60s ≥ 80%, blended ≤ 0.70 and ladder p95 ≤ 2× budget; CHECKBOX when fill@60s < 50% or blended ≥ 0.85; OPEN otherwise. Spend to date 12.3849 USD.
