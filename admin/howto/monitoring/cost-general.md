# General cloud costs

:::{note}
Available for dedicated AWS clusters only (and excluding CloudBank managed accounts). Other deployments on GCP will be supported in the future.
:::

## Accessing the cloud cost dashboard

Community Champions can view the cloud cost dashboards from their Grafana instance (please see [Grafana Dashboards](grafana-dashboards.md) for how to gain access).

From the main menu of Grafana, navigate to *Dashboards > Cloud cost dashboards > General cloud costs* to view the dashboard.

## Understanding the cloud cost dashboard

The dashboard is made of several panels:

- Daily costs
- Daily costs per hub
- Total daily costs per component
- Daily costs per component per hub.

### Daily costs

:::{figure} images/cost-attribution-daily.png
:alt: A line graph showing daily cloud costs over a 1 month period.
:::

*Cost account* refers to the associated AWS account's *total* costs, and *Cost attributable* refers to the costs that have been *attributed* to 2i2c managed cloud infrastructure.

There are some costs associated with 2i2c managed cloud infrastructure that can't be attributed. For example, the act of loading the Cloud Cost dashboard itself incurs a cost that isn't attributed to 2i2c managed cloud infrastructure but forms a small part of the total cost.

If *Cost account* is significantly larger than *Cost attributable*, then in principle this should be because of activity unrelated to 2i2c managed cloud infrastructure. Please contact [support](/support.md) if you have any questions about understanding your cloud costs.

:::{note}

- All costs are [unblended costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
- All costs are pure usage costs, and doesn't account for credits etc.
:::

### Daily costs per hub

:::{figure} images/cost-attribution-daily-per-hub.png
:alt: A line graph showing daily cloud costs per hub over a 1 month period.
:::

Costs can sometimes be attributed to a specific hub, and that can then be seen here. A typical 2i2c-managed deployment comprises of a staging hub and a production hub, although some other communities may have extra hubs such as a workshop hub.

*Cost support* reflects all 2i2c cloud infrastructure support costs that aren't attributable to a specific hub.

### Total daily costs per component

:::{figure} images/cost-attribution-component.png
:alt: A time series showing daily cloud costs per component over a 1 month period.
:::

Components are groupings of cloud-provided services, such as

- compute
- home storage
- object storage
- networking
- support

For specific definitions, see [https://github.com/2i2c-org/jupyterhub-cost-monitoring/blob/2a810989bb1c1685277d2574d3b76e673bc6e5ad/src/jupyterhub_cost_monitoring/const_cost_aws.py#L11](https://github.com/2i2c-org/jupyterhub-cost-monitoring/blob/2a810989bb1c1685277d2574d3b76e673bc6e5ad/src/jupyterhub_cost_monitoring/const_cost_aws.py#L11).

### Daily costs per component per hub

:::{figure} images/cost-attribution-component-per-hub.png
:alt: A time series showing daily cloud costs per component per hub over a 1 month period.
:::

This panel shows the same information as above, but broken down for each specific hub also.

## Sharing and reporting Grafana dashboards

See [Sharing and reporting Grafana dashboards](reporting.md) for how to share and generate reports from Grafana dashboards.
