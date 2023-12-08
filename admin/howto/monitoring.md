# Monitoring the hub with Grafana

*Note: Grafana dashboards are only available to communities on **dedicated** clusters.  If a community is on a shared cluster and would like to discuss transitioning, please contact partnerships@2i2c.org.

To discover the URL to you Grafana dashboard, use the [List of Running Hubs](https://infrastructure.2i2c.org/reference/hubs/) table. This table also shows which cluster each hub is running on. 

## Getting a Grafana account

During the hub deployment process, 2i2c engineering will send the hub champions an email with an invitation link to Grafana to allow them to create an account. This invite link only lasts for seven days; if a new invite link is required please email support@2i2c.org to request a new invite link.

This Grafana account is separate from the account used to log in to your JupyterHub. This new account has administrative priviledges and will allow hub champions to invite others to have access to Grafana as appropropriate for your community.

## Using Grafana for your JupyterHub

There is currently limited documentation available about what each dashboard or panel represents but this is an [upstream work in progress](https://jupyterhub-grafana.readthedocs.io/en/latest/).

## Making changes to Grafana dashboards

Changes to the `JupyterHub dashboard` directory will not persist. If changes are required, please contribute to the upstream [jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project.

Hub champions are welcome to create their own custom dashboards and panel in a separate directory.