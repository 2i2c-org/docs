# Usage Quotas Dashboard

:::{figure} images/grafana-usage-quotas.png
:alt: Screenshot of a Usage Quotas Grafana dashboard
The "Usage Quotas" Grafana dashboard.
:::

This dashboard consists of the following panels:

- *Cumulative compute usage over the last `$window` days* is a time series of the cumulative compute usage over the last `$window` days
- *Compute usage policies* is a table of compute usage quota limits individually applied to policy group members
- *Monitoring - Denied server launch* shows the number of server launches denied due to users exceeding compute quota limits
- *Monitoring - Fail opens* shows when a user server is allowed to launch when the usage quota system is unavailable

with dropdowns to filter data by:

- `$hub` to filter by hub name, e.g. `staging`, `prod`, etc.
- `$user` to filter by user name
- `$window` to filter by the rolling window over which a compute policy is applied.