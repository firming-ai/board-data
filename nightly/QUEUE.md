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
| 30d | 26 | 2m00s | 4m59s | 23m02s | 24m50s |
| all-time | 26 | 2m00s | 4m59s | 23m02s | 24m50s |

Completed: 26/26. Expired: 0. Overran window: 0. Failed: 0.

## gemini (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 1m46s | 26m28s | 1h16m50s | 1h22m26s |
| 30d | 24 | 2m39s | 5m48s | 1h05m23s | 1h22m26s |
| all-time | 24 | 2m39s | 5m48s | 1h05m23s | 1h22m26s |

Completed: 24/24. Expired: 0. Overran window: 0. Failed: 0.

## mistral (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 40s | 1m02s | 1m03s | 1m03s |
| 30d | 23 | 1m02s | 14h01m10s | 20h00m16s | 20h17m15s |
| all-time | 23 | 1m02s | 14h01m10s | 20h00m16s | 20h17m15s |

Completed: 23/24. Expired: 0. Overran window: 0. Failed: 0.

## openai (24h)

| range | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 7d | 8 | 2m26s | 8m24s | 18m58s | 20m08s |
| 30d | 24 | 2m35s | 24m27s | 5h46m51s | 7h09m48s |
| all-time | 24 | 2m35s | 24m27s | 5h46m51s | 7h09m48s |

Completed: 24/26. Expired: 0. Overran window: 0. Failed: 0.

## Days of continuous accrual

| venue | days |
|---|---|
| anthropic | 26 |
| gemini | 24 |
| mistral | 24 |
| openai | 26 |

