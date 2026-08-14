# Apply compute quotas

This opt-in feature allows hub admins to cap the amount of compute resource a user can access over a given time period.

## Compute quotas

Suppose you are running a workshop and would like to cap usage to a `4GiB RAM` server for each user per day.
With compute quotas you can apply a usage cap of `4GiB x 24 hours` = `96 GiB-hours` over a rolling 1 day window for every member of a particular [JupyterHub group](https://jupyterhub-usage-quotas.readthedocs.io/en/latest/howto/user-group-management/).

Alternatively, can also apply a blanket compute usage policy to all users irrespective of JupyterHub group memberships.

For more details on compute policy configuration, see the [`jupyterhub-usage-quotas` documentation](https://jupyterhub-usage-quotas.readthedocs.io/en/latest/explanation/technical/#policy-configuration).

:::{tip} Opt-in
If you would like to apply a compute usage policy for your hub, then please get in touch with our [support desk](https://docs.2i2c.org/support/).
:::

## Usage dashboards

To accompany this feature, there is a [user-facing dashboard](../../user/usage-quota-dashboard.md) available to end-users to keep track of usage.
The home storage component is enabled by default, which shows the "used versus available" disk usage in a user's home directory.
The compute component is enabled if a compute quota policy is applied to the hub.

## Learn more

- [`jupyterhub-usage-quotas` documentation](https://jupyterhub-usage-quotas.readthedocs.io/en/latest)
- [`jupyterhub-usage-quotas` GitHub repository](https://github.com/2i2c-org/jupyterhub-usage-quotas)
