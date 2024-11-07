# Monitoring the hub with Grafana

:::{note}
Grafana dashboards are only available to communities on **dedicated** clusters. If a community is on a shared cluster and would like to discuss transitioning, please contact [partnerships@2i2c.org](mailto:partnerships@2i2c.org).
:::

To discover the URL to the Grafana dashboard, use the [List of Running Hubs](https://infrastructure.2i2c.org/reference/hubs/) table. This table also shows which cluster each hub is running on.

## Getting a Grafana account

During the hub deployment process, 2i2c engineering will send the Hub Champions an email with an invitation link to Grafana to allow them to create an account. **This invite link only lasts for seven days;** and is unique to the recipient's email address. If a new invite link is required please contact [support](support:email) to request a new invite link.

:::{figure} ../../images/grafana-invite.png
:alt: Grafana website after clicking invitation link
The Grafana website after clicking invitation link.
:::

This Grafana account is separate from the account used to log into JupyterHub. This new account has administrative privileges and will allow Hub Champions to invite others to have access to Grafana as admins or viewers for the community. See the [instructions](https://infrastructure.2i2c.org/sre-guide/support/grafana-account) for how to invite others to join Grafana.

## Using Grafana for your JupyterHub

:::{figure} ../../images/grafana-dashboard.png
:alt: Screenshot of JupyterHub Grafana dashboard
The "Activity" Grafana dashboard.
:::

There is documentation available about what each dashboard or panel represents in the upstream [JupyterHub Grafana](https://jupyterhub-grafana.readthedocs.io/en/latest/) project. You can also hover over the {octicon}`info` icon in the top-right corner of each panel for more information.

## Making changes to Grafana dashboards

Changes to the `JupyterHub dashboard` directory will not persist. If changes are required, we encourage you to contribute to the upstream [jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project.

Hub Champions are welcome to create their own custom dashboards and panel in a separate directory, but the configuration will not be backed up.
