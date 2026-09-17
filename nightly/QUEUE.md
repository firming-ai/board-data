# Offpeak queue latency — summary

How long a batch tier actually takes to land, measured by submitting a couple
of tiny jobs and watching the clock. This spends real money at real venues and
is therefore **not** the Spread Board: that one marks open grid data and
spends nothing. Same separation, and the same reason, as `SETTLED.md`.

Every number below is a percentile over completed sessions — not a single
row. A session still running when a probe stopped watching is *open*: it
stays on the desk's worklist and is resolved from its stored handle once a
later run checks again, so it is excluded from these numbers until it has an
outcome. A session marked *expired* or *overran_window* is the venue missing
its own declared window — the failure mode this table exists to catch. A
session marked *censored* predates resolution: it was cancelled after a fixed
wait with no completion in sight, so its true turnaround is only known to be
at least that wait — it contributes to the attempt count below but not to any
percentile, since it has no elapsed time to report.

The rows this is built from are private, kept in the desk's own repository.
Private tail since 2026-08-28; days before that were imported from the
public series this table replaces.

Written by `tools/queue_summary.py`, never by hand.


## anthropic (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 1m45s | 19m46s | 24m20s | 24m50s |
| 30d | 25 | 2m03s | 5m01s | 23m06s | 24m50s |
| all-time | 25 | 2m03s | 5m01s | 23m06s | 24m50s |

Completed: 25/25. Expired: 0. Overran window: 0. Failed: 0.

## gemini (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 1m53s | 26m28s | 1h16m50s | 1h22m26s |
| 30d | 23 | 2m49s | 5m54s | 1h06m07s | 1h22m26s |
| all-time | 23 | 2m49s | 5m54s | 1h06m07s | 1h22m26s |

Completed: 23/23. Expired: 0. Overran window: 0. Failed: 0.

## mistral (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 40s | 1m03s | 1m03s | 1m03s |
| 30d | 22 | 1m03s | 14h25m43s | 20h01m02s | 20h17m15s |
| all-time | 22 | 1m03s | 14h25m43s | 20h01m02s | 20h17m15s |

Completed: 22/23. Expired: 0. Overran window: 0. Failed: 0.

## openai (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 2m50s | 2h23m02s | 6h41m07s | 7h09m48s |
| 30d | 23 | 2m35s | 25m03s | 5h50m28s | 7h09m48s |
| all-time | 23 | 2m35s | 25m03s | 5h50m28s | 7h09m48s |

Completed: 23/25. Expired: 0. Overran window: 0. Failed: 0.

## Days of continuous accrual

| venue | days |
|---|---|
| anthropic | 25 |
| gemini | 23 |
| mistral | 23 |
| openai | 25 |

