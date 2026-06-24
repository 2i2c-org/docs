# Control access to Dask Gateway

Starting with [Dask Gateway](https://gateway.dask.org/) version [v2026.3.0](https://gateway.dask.org/changelog.html#v2026-3-0), hub admins can control which hub users or groups have access to Dask-Gateway, via [JupyterHub scopes](https://jupyterhub.readthedocs.io/en/stable/rbac/scopes.html). This is possible because JupyterHub is used to authenticate requests between users and the dask-gateway-server.

2i2c is deploying this version alongside the hubs, so all communities we serve that are using Dask-Gateway, now have access to this feature.

## Pre-requisites

Before requesting this feature:

1. Go to the [JupyterHub admin panel](admin/management/admin-panel) and create or retrieve the relevant groups that should have access to Dask-Gateway.
1. Add users to these groups if the groups were newly created in the step above.

## How to request this feature

To request this feature, please reach out to [2i2c support](https://docs.2i2c.org/support/) and provide the following information:

1. The name of the hub you want this feature enabled on
2. The list of users or groups that should have access to Dask-Gateway

The 2i2c team will then enable this feature for you and confirm once it is ready.
