# 2i2c Hub infrastructure

This page contains information about the infrastructure that is provided by the 2i2c Hubs pilot.

## Infrastructure overview of a 2i2c Hub

Here's a small overview that gives and idea for the major parts of a 2i2c Hub. We'll describe the individual pieces a bit more below.

```{image} https://2i2c.org/media/2i2c-hub-overview.png
:height: 300px
```

## What technology makes up each hub?

🚀 core infrastructure
: Underneath each 2i2c Hub is a [JupyterHub](https://jupyter.org/hub). These provide interactive computing sessions for each of your users, and connect to the other infrastructure in the cloud. We use [`auth0`](https://auth0.com/) for authenticating users, which can connect to a number of other authentication protocols (such as OAuth2).

💻 interfaces
: Each 2i2c Hub has two main interactive interfaces: Jupyter interfaces (Notebook and Lab), and RStudio. Each of them is accessible from your session via `/tree`, `/lab`, and `/rstudio` endpoints in your URL.

🌄 environment
: Your 2i2c Hub has an environment that has been created for your particular use-case. It exists as a Docker image that your JupyterHub loads when a user starts a new session. These images can either be built with the tool [repo2docker](https://repo2docker.readthedocs.io/), or pulled directly from a Docker registry. The environment also comes pre-loaded with some tools that are helpful for working with JupyterHub, such as [nbgitpuller](https://jupyterhub.github.io/nbgitpuller). See [](environment/custom) for more information.

🤖 hardware
: 2i2c Hubs can run on most major cloud providers - the primary thing that is needed is a working Kubernetes deployment. By default, 2i2c runs its hubs on Google Cloud, but if communities wish to use a different provider, this can be accomplished as well. This also means that the hardware underlying the Kubernetes deployment is configurable.

📦 data
: The data that is used by your 2i2c Hub is provided by you! 2i2c Hubs can connect with a variety of public data sources. We recommend using standard data structures or specifications via libraries like [Intake](https://intake.readthedocs.io/en/latest/). Note that 2i2c does not host this data itself, but can build connections between 2i2c hubs and these data sources.

(hub-types)=
## Types of 2i2c Hubs

There are several flavors of 2i2c Hubs with configuration designed for specific use-cases. They provide a starting point, and can be further customized for a specific community using standard JupyterHub configuration. Here's a short description of each.

(hub-types:pangeo)=
### Pangeo Hubs

The [Pangeo Project](https://pangeo.io) is a community platform for Big Data geoscience.
This platform is one of the cutting-edge workflows in cloud-native data science with large datasets, and drives development of a number of open source tools in this space.

The 2i2c Pangeo Hubs are intended to allow other teams, organizations, and communities to access the same infrastructure and stack that Pangeo uses. Here are a few important points about the 2i2c Pangeo Hubs:

The **user environment**: Runs the [`pangeo-notebook` Docker image](https://pangeo-data.github.io/pangeo-stacks/images.html#pangeo-pangeo-notebook). This includes packages such as `xarray`, `zarr`, `intake`, and `dask`, along with the PyData stack. In addition, **scalable computing** is provided via [`dask`](https://dask.org) and [`dask-gateway`](https://gateway.dask.org/), which allows you to quickly scale computing resources as needed.

You can find the JupyterHub configuration for 2i2c Pangeo Hubs [at this repository](https://github.com/2i2c-org/pilot-hubs/tree/master/hub-templates/daskhub).

(hub-types:education)=
### Education Hubs

The 2i2c Educational Hubs provide standard data science environments and infrastructure that is meant for teaching data science. They are inspired by 2i2c's experience with the [DataHubs at UC Berkeley](https://docs.datahub.berkeley.edu/en/latest/).

The Education Hubs come pre-configured with several interfaces and extensions pre-installed to help students learn on the hub.
For example, [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller/index.html) allows instructors to create "interactive links" that let students quickly grab a copy of a file (e.g., a notebook) and use it in their own Jupyter session.
These can be used in conjunction with tools like [Jupyter Book](https://jupyterbook.org) to build connections between your course's content and your online learning environment.

You can find the JupyterHub configuration for 2i2c Education Hubs [at this repository](https://github.com/2i2c-org/pilot-hubs/tree/master/hub-templates/base-hub).

(hub-types:ephemeral)=
### Ephemeral Hubs

Ephemeral Hubs are designed to quickly provide online computing sessions on a short-term basis (for example, as a part of a bootcamp demonstration). They are inspired by 2i2c's experience running online services like [`mybinder.org`](https://mybinder.org).

Ephemeral Hubs contain the same environment as educational hubs, however they **do not require authentication**, and **do not persist user files**. They're designed for quick interactions with minimal infrastructure complexity and cost.

You can find the JupyterHub configuration for 2i2c Education Hubs [at this repository](
https://github.com/2i2c-org/pilot-hubs/tree/master/hub-templates/ephemeral-hub).


## How are hubs configured and deployed?

All of the configuration and deployment scripts for the 2i2c Hubs can be found at [the `pilot-hubs/` repository](https://github.com/2i2c-org/pilot-hubs). This repository contains both the deployment code as well as documentation that explains how it works. It should be treated as "for advanced users only", and is provided for transparency and as a guide for the community to follow if they wish to manage their own infrastructure similar to 2i2c Hubs.

To learn about how the `pilot-hubs/` repository works, we recommend checking out the [`pilot-hubs` documentation](ph:index).


(note-on-urls)=
## Where are hubs accessed?

By default all 2i2c Hubs get their own URL with the following form:

```
<hub-name>.<community-name>.2i2c.cloud
```

Each 2i2c Hub has **hub name** (denoted by `<hub-name>`) and a **community name** (denoted by `<community-name>`). Communities are collections of hubs around a particular community or collaboration. Each community infrastructure may be run by different teams. For more information, see [](people-behind-hubs).

It is also possible to provide your own URL that points to a 2i2c Hub.

% TODO: add back in once #54 is merged
% ## How could I deploy my own 2i2c Hub?
%
% Check out [](../admin/migrate.md) for information about migrating off of a 2i2c Hub, including deploying your own hub.
