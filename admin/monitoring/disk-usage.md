(monitoring:disk-usage)=
# Filesystem and disk dashboards

## Total storage space

Each hub has one disk that stores _all_ persistent user data: home directories and directories for [sharing data between users](#data:sharing-files).
This disk starts small and grows as needed.

When the disk has less than 10% of its space left, 2i2c's team gets an alert and increases its size.
We may also contact you, in case you want to ask your users to clean up some space.[^1]

[^1]: A bigger disk costs more, and shrinking it later is hard.
  Shrinking means creating a new, smaller disk, moving the data over, and then deleting the old one.
  So we try to grow the disk only when we need to.

## Usage quotas

All of our hubs have a **default value of 10GB storage quota per-user**, although this may vary depending on the hub.
Also, the `shared`, and `shared-public` directories also **abide the same default 10GB storage quota**.

```{note}
If you intend to store more than this in these folders, please contact 2i2c support.
```

But keep in mind that the `/home/jovyan` space is intended only for notebooks and code and is **not** an appropriate place to store datasets, as it can get really expensive (and slow) when used that way.

:::{seealso}
- For storing small datasets, take a look at [](#data:sharing-files).
- For temporarily storing large datasets, take a look at the [/tmp directory](#filesystem:tmp).
- For storing data in cloud object storage, see the section [Cloud Object Storage](../../user/data/object-storage/index.md).
:::

(admin:tmp-dedicated)=
## Dedicated `/tmp` disks

By default, each user's [`/tmp` directory](#filesystem:tmp) shares a disk with other users on the same machine (usually around `20-30GB` per user).
If some of your users need more temporary space, you can offer them a [dedicated `/tmp` disk](#filesystem:tmp-dedicated) that they pick when they start their server.

Consider this when a few users run workflows that download or generate large intermediate files.
Giving those users a dedicated disk is much cheaper than giving every user a bigger machine or a bigger shared disk, because the dedicated disk only costs money while the user's server is running.

You can offer dedicated disks to all users, or only to some user groups.
For example:

- [uw-escience offers a 500GB disk to everyone](https://github.com/2i2c-org/infrastructure/blob/3278bfdb5258c806feeac5a7c7eb4e6ea8fc9f2c/config/clusters/uw-escience/common.values.yaml#L97-L131).
- [MAAP staging offers a 500GB disk only to users in its larger-machine groups](https://github.com/2i2c-org/infrastructure/blob/3278bfdb5258c806feeac5a7c7eb4e6ea8fc9f2c/config/clusters/maap/staging.values.yaml#L87-L126).

To set this up, [contact support](#support) with the disk size you want and which groups should see it.

:::{note} Only available on AWS
Currently this is only available on clusters and hubs running on AWS.
If you'd like this functionality on a non-AWS hub, reach out to use and we can explore how to enable it in another cloud provider.
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
