# Grafana dashboards

:::{note}
Grafana dashboards are only available to communities on **dedicated** AWS clusters (and excludes CloudBank-managed accounts). If a community is on a shared cluster and would like to discuss transitioning, please contact [partnerships@2i2c.org](mailto:partnerships@2i2c.org).
:::

To find the URL to the Grafana dashboard for your community, use the [List of Running Hubs](https://infrastructure.2i2c.org/reference/hubs/) table.

Note that monitoring data is retained for up to 3 years on 2i2c hubs.

## Getting a Grafana account

During the hub deployment process, 2i2c engineering will send authorized Hub Champions an email with an invitation link to Grafana to create an account. **This invite link expires after seven days;** and is unique to the recipient's email address. If a new invite link is required please contact [support](support:email).

:::{figure} images/grafana-invite.png
:alt: Screenshot of a form containing fields for email, name, username and password.
The Grafana website after clicking the invite link.
:::

This Grafana account is *separate* from the account used to log into JupyterHub. This new account has administrative privileges and will allow Hub Champions to invite other members of their community to access Grafana with admin or viewer roles.

:::{note}
See these [instructions](https://infrastructure.2i2c.org/sre-guide/support/grafana-account) for how to invite others to join Grafana.
:::
