# Launch a dask-gateway cluster

This guide shows you how to launch a dask gateway cluster for parallel and distributed computing.

:::{contents}
:depth: 2
:local:
:::

## What is Dask Gateway?

Dask Gateway allows users to launch clusters for scaling computations without requiring direct access to the underlying backend of the 2i2c hub (e.g. Kubernetes). Configuration, such as cluster resourcing, authentication and security settings, is managed by 2i2c engineering to ease deployment and provide a consistent user experience across the hub.

:::{warning}
Avoid large, long-running, idle clusters, which consume cloud computing resources and costs. Only use a cluster when you need it and shutdown when not in use.
:::

## Usage

This section roughly follows the [Dask Gateway Docs – Usage](https://gateway.dask.org/usage.html), however, the guide outlined here is specific to a 2i2c dask hub.

### Connect to a dask-gateway server

Create a gateway client to communicate with the dask-gateway server.

```python
from dask_gateway import Gateway
gateway = Gateway()
```

<!-- ## Which image should I use?

Defaults to using the Pangeo image https://infrastructure.2i2c.org/topic/infrastructure/hub-helm-charts/#hub-helm-charts

## FAQs

https://infrastructure.2i2c.org/howto/troubleshoot/logs/common-errors/#dask-issues -->