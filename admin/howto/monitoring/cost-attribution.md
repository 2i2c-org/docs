# Cost attribution

:::{note}
Available for dedicated AWS clusters only. Other deployments on GCP will be supported in the future.
:::

## Accessing the cloud cost dashboard

Community Champions can view the Cloud Cost dashboard from their Grafana instance (please see [Grafana Dashboards](grafana-dashboards) for how to gain access).

From the main menu of Grafana, navigate to *Dashboards > Cloud cost dashboards > Cloud cost attribution* to view the dashboard.

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

"Cost account" refers to the associated AWS account's total costs, and "Cost attributable" refers to the costs that has successfully been attributed to 2i2c managed cloud infrastructure.

There are some costs associated with 2i2c managed cloud infrastructure that can't be attributed to it, but they are expected to be small. As an example, this panel is presenting data that incurred a small cost to ask for, and that cost is an example of what we fail to attribute and is only captured in the AWS account's cost.

If "Cost account" is significantly larger than "Cost attributable", it should be because of activity unrelated to 2i2c managed cloud infrastructure.

Note:

- All costs are [unblended costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
- All costs are pure usage costs, and doesn't consider credits etc.

### Daily costs per hub

:::{figure} images/cost-attribution-daily-per-hub.png
:alt: A line graph showing daily cloud costs per hub over a 1 month period.
:::

Costs can sometimes be attributed to a specific hub, and that can then be seen here. A typical 2i2c-managed deployment comprises of a staging hub and a production hub, although some other communities may have extra hubs such as a workshop hub.

"Cost shared" reflect all 2i2c cloud infrastructure attributable costs that aren't attributable to a specific hub.

For hub specific cost attribution, the underlying cloud infrastructure needs to setup to be hub specific. Currently compute, home storage, and object storage can be setup for specific hubs, but isn't unless explicitly requested.

Note:

- Hub refers to a deployment of a JupyterHub and related services within a Kubernetes namespace.
- All costs are [unblended costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
- All costs are pure usage costs, and doesn't consider credits etc.

### Total daily costs per component

:::{figure} images/cost-attribution-component.png
:alt: A line graph showing daily cloud costs per component over a 1 month period.
:::

Components are human friendly groupings of AWS services, defined as:

- backup: AWS Backup
- compute: EC2 – Other, Amazon Elastic Compute Cloud
- fixed: Amazon Elastic Container Service for Kubernetes
- home storage: Amazon Elastic File System
- networking: Amazon Elastic Load Balancing, Amazon Virtual Private Cloud
- object storage: Amazon Simple Storage Service

Note:

- All costs are [unblended costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
- All costs are pure usage costs, and doesn't consider credits etc.

### Daily costs per component per hub

:::{figure} images/cost-attribution-component-per-hub.png
:alt: A line graph showing daily cloud costs per component per hub over a 1 month period.
:::

The same as above but broken down for each specific hub.

## Sharing cost reports

The dashboard can be shared with other community members and stakeholders so they can understand usage and cost patterns. Community Champions can export data to a CSV file, generate a snapshot of the Grafana dashboard and share a public link, or [Progamatically accessing Prometheus data](prometheus-access) themselves.

### Generate a CSV file

1. Click on the three dots {material-regular}`more_vert`, in the top-right corner of the panel you wish to generate a CSV file for.
1. From the dropdown menu select *{octicon}`info` Inspect > Data*.
1. Click on the {bdg-primary}`Download CSV` button to download the data as a CSV file.

### Share a snapshot of the dashboard or panel

This function is available to Grafana admins only. A snapshot is a frozen view of data that can with others without the need to login with a Grafana account.

1. If you wish to share the *entire dashboard*, click on the {bdg-primary}`Share` button to the left of the time-range selector.
1. If you wish to share a *single panel*, click on the three dots {material-regular}`more_vert`, in the top-right corner of a panel. From the dropdown menu select *Share*.
1. From the pop-up *Share Panel* dialog, select the *Snapshot* tab and fill out the details.
1. Click the {bdg-primary}`Publish Snapshot` button to generate a public link that you can share with others.

:::{figure} images/cost-attribution-snapshot.png
:alt: Snapshot of the share panel dialog, with Snapshot name, Expire and Timeout fields.
:::
