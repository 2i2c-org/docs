(monitoring:disk-usage)=
# Filesystem and disk dashboards

## Total storage space

Hubs have a disk that stores _all_ persistent user data (user home directories, but also other directories meant for [sharing data amongst users](#sharing-files)). This disk starts from a conservative small size and then later increases based on needs.

We have alerts that notify us when the hub has less than 10% of space remaining. At this point we'll increase the size of the disk to avoid any issues.
We might also be reaching out to you, in case you want to take action and instruct your users to cleanup some space.

However, bear in mind that increasing the size of a storage disk comes with cost implications and resizing it down later, is a complicated process that we want to avoid as much as possible.
This is because it requires the creation of a new, smaller disk, where existing data will be moved to, before the original big disk can be decommissioned. 

## Usage quotas

All of our hubs have a **default value of 10GB storage quota per-user**, although this may vary depending on the hub.
Also, the `shared`, and `shared-public` directories also **abide the same default 10GB storage quota**.

```{note}
If you intend to store more than this in these folders, please contact 2i2c support.
```

But keep in mind that the ``/home/jovyan`` space is intended only for notebooks and code and is **not** an appropriate place to store datasets, as it can get really expensive (and slow) when used that way.

:::{seealso}
- For storing small datasets, take a look at [](#sharing-files).
- For temporarily storing large datasets, take a look at the [/tmp directory](#filesystem:tmp).
- For storing data in cloud object storage, see the section [Cloud Object Storage](./object-storage/index.md).
:::

## Monitoring disk usage
You can monitor home directory disk usage for users on your hub to identify large directories and manage storage resources.

:::{seealso}
See [](./grafana-dashboards.md) for setting up Grafana on your hub.
:::

### Navigate to the Home Directory Usage Dashboard

To access the disk usage dashboard:

1. Navigate to your hub's [Grafana dashboard](grafana-dashboards.md)
2. Go to {gui}`Dashboards > JupyterHub Default Dashboards > Home Directory Usage Dashboard`

:::{figure} images/home-directory-usage-dashboard.png
:alt: Screenshot of the Home Directory Usage Dashboard showing a table of directories with their sizes and usage percentages
The Home Directory Usage Dashboard displays disk usage for user home directories.
:::

Note that some entries will be for _users_ while others will be _shared by all users_. Above, we've blurred out the users and included the hub-wide directory.

## Resources

For more information about user storage quotas and filesystem structure, see the [user documentation on filesystem and storage](../../user/data/filesystem.md).
