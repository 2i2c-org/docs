# Cloud costs per user

![Grafana dashboard with multiple panels showing stacked bar charts of user cloud costs over time.](https://raw.githubusercontent.com/2i2c-org/jupyterhub-cost-monitoring/refs/heads/main/images/dashboard.png)

## Navigate to the *Cloud costs per user* dashboard

From the Grafana homepage, navigate to *Home > Dashboards > Cloud cost dashboards* and then click on *Cloud costs per user*.

This will load the dashboard, which may take a few moments to populate with data.

## Understand the dashboard layout

The dashboard is organized into several panels, each providing insights into different aspects of user cloud costs:

- **Top 5 Users**: a quick at a glance view of the top 5 users by total cost over the selected time range.
- **Total by Hub**: a breakdown of total costs by hub, allowing you to see which hubs are incurring the most expenses.
- **Total by Component**: a breakdown of total costs by component (such as compute, home storage, etc.), helping you identify which resources are driving costs.
- **Hub**: individual panels for each hub, showing daily costs by users within that hub. User costs summed over all hubs is shown by default. Try toggling the variable `hub` at the top of the dashboard to see splits by individual hubs.
- **Component**: individual panels showing daily costs by users for compute and home storage. You can also toggle the variable `component` at the top of the dashboard to show or hide panels.

## Interact with the dashboard

You can interact with the dashboard in several ways:

- **Time Range**: use the time range selector in the top right corner to adjust the period for which data is displayed. The last 30 days are shown by default. The timezone is always UTC, since daily cost data prepared by cloud providers is typically settled at 00:00 UTC.
- **Variables**: use the dropdowns at the top of the dashboard to filter data by hub or component.
- **Legend**: click on user names in the legend to isolate or hide specific users in the graphs. You can select multiple users by holding down the `Shift` key while clicking, and double-click to reset the selection.
- **Tooltips**: hover over data points in the graphs to see detailed information, including exact cost values and timestamps of each user.

:::{tip}
Some interactions may re-trigger additional queries to fetch data, so there may be a slight delay while the graph is updated.
:::

## Export data

You can export the data from any panel by clicking on the panel menu in the top right corner, then selecting *Inspect > Data*. From there, you can view the raw data and export it in various formats, such as CSV or JSON.

## Resources

Grafana is a powerful open source data visualization tool with many features. For more information on how to use Grafana, refer to the [Grafana documentation](https://grafana.com/docs/grafana/latest/).

## Feedback and support

If you have any feedback or suggestions on what works well or how you would like to improve the dashboard design, [let us know](https://github.com/2i2c-org/jupyterhub-cost-monitoring/issues/new)!
