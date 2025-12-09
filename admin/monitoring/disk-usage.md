(monitoring:disk-usage)=
# Filesystem and disk dashboards

You can monitor home directory disk usage for users on your hub to identify large directories and manage storage resources.

:::{seealso}
See [](./grafana-dashboards.md) for setting up Grafana on your hub.
:::

## Navigate to the Home Directory Usage Dashboard

To access the disk usage dashboard:

1. Navigate to your hub's [Grafana dashboard](grafana-dashboards.md)
2. Go to {kbd}`Dashboards` → {kbd}`JupyterHub Default Dashboards` → {kbd}`Home Directory Usage Dashboard`

:::{figure} images/home-directory-usage-dashboard.png
:alt: Screenshot of the Home Directory Usage Dashboard showing a table of directories with their sizes and usage percentages
The Home Directory Usage Dashboard displays disk usage for user home directories.
:::

Note that some entries will be for _users_ while others will be _shared by all users_. Above, we've blurred out the users and included the hub-wide directory.

## Resources

For more information about user storage quotas and filesystem structure, see the [user documentation on filesystem and storage](../../user/data/filesystem.md).
