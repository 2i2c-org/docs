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

## Using Grafana for your JupyterHub

:::{figure} images/grafana-dashboard.png
:alt: Screenshot of JupyterHub Grafana dashboard
The "Activity" Grafana dashboard.
:::

The `JupyterHub Default Dashboards` folder shows dashboard deployed from the upstream [https://github.com/jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project.

1. **Cluster Information**

  Contains panels with different cluster usage statistics about things like:
    - nodes
    - memory
    - cpu
    - running users per hub in cluster

1. **Global Usage Dashboard**

  This dashboard contains information about the weekly active users we get on each of the clusters we manage.

1. **JupyterHub Dashboard**

   This is the place to find information about the hub usage stats and hub diagnostics, like
   - number of active users
   - user CPU usage distribution
   - user memory usage distribution
   - server start times
   - hub response latency

  There is also a Panel section about `Anomalous user pods` where pods with high CPU usage or high memory usage are tracked.

1. **NFS and Support Information**

  This provides info about the NFS usage and monitors things like CPU, memory, disk and network usage of the Prometheus instance.

1. **Usage Dashboard**

  This has information about the number of users using the cluster over various periods of time.

1. **Usage Report**

  This provides a report about the memory requests, grouped by username, for notebook nodes and dask-gateway nodes. It also provides a graph that monitors GPU requests per user pod.

## Making changes to Grafana dashboards

If you make any changes to the pre-configured dashboards in the *JupyterHub Default Dashboards* and *Cloud Cost Dashboards* folders, then they will not be saved.

We encourage you to create new dashboards outside of these folders (however the configurations will not be backed up), or even contribute to:

- the upstream [https://github.com/jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project for *JupyterHub Default Dashboards*
- the [https://github.com/2i2c-org/jupyterhub-cost-monitoring](https://github.com/2i2c-org/jupyterhub-cost-monitoring) project for *Cloud Cost Dashboards*

## Resources

Grafana is a powerful open source data visualization tool with many features. For more information on how to use Grafana, refer to the [Grafana documentation](https://grafana.com/docs/grafana/latest/).
