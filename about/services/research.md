(hub-types:scalable-research)=
# Scalable computing in the cloud

:::{admonition} TODO
This section is incomplete, it needs more information!
:::

```{image} https://drive.google.com/uc?export=download&id=1gWAIQVKcB-uxuJsBHqlDlRTq88oki1zn
```

The [Pangeo Project](https://pangeo.io) is a community platform for Big Data geoscience.
This platform is one of the cutting-edge workflows in cloud-native data science with large datasets, and drives development of a number of open source tools in this space.

The 2i2c Pangeo Hubs are intended to allow other teams, organizations, and communities to access the same infrastructure and stack that Pangeo uses. Here are a few important points about the 2i2c Pangeo Hubs:

The **user environment**: Runs the [`pangeo-notebook` Docker image](https://pangeo-data.github.io/pangeo-stacks/images.html#pangeo-pangeo-notebook). This includes packages such as `xarray`, `zarr`, `intake`, and `dask`, along with the PyData stack. In addition, **scalable computing** is provided via [`dask`](https://dask.org) and [`dask-gateway`](https://gateway.dask.org/), which allows you to quickly scale computing resources as needed.

You can find the JupyterHub configuration for 2i2c Pangeo Hubs [at this repository](https://github.com/2i2c-org/pilot-hubs/tree/master/hub-templates/daskhub).

## Inspiration for our scalable research hubs

## Basic hub configuration

**User Environment**

**Resources**

**Cloud infrastructure**


## What does a typical workflow look like?

## What open source tools are featured?

## Communities that use this hub

### Pangeo Hubs pilot

The Pangeo Hubs pilot is a collaboration with [the Pangeo Project](https://pangeo.io/), which is a distributed scientific community for big-data geoscience.
The Pangeo approach has become a leading approach in cloud-native geospatial analytics, and drives development across many parts of the PyData ecosystem.
This pilot is an attempt at deploying Pangeo-like hubs with scalable Dask clusters via Kubernetes.