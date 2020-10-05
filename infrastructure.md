# 2i2c Hub infrastructure

This page contains information about the infrastructure that is provided by the 2i2c Hubs pilot.

:::{note}
This content is meant for those familiar with cloud infrastructure and tools for deploying things like a 2i2c Hub. It is meant for reference and for guidance to others who wish to run their own infrastructure, but isn't necessary to use or customize your own 2i2c Hub.
:::

## What technology makes up each hub?


🚀 core infrastructure
: Underneath each 2i2c Hub is a [JupyterHub](https://jupyter.org/hub). These provide interactive computing sessions for each of your users, and connect to the other infrastructure in the cloud. We use [`auth0`](https://auth0.com/) for authenticating users, which can connect to a number of other authentication protocols (such as OAuth2).

💻 interfaces
: Each 2i2c Hub has two main interactive interfaces: Jupyter interfaces (Notebook and Lab), and RStudio. Each of them is accessible from your session via `/tree`, `/lab`, and `/rstudio` endpoints in your URL.

🌄 environment
: Your 2i2c Hub has an environment that has been created for your particular use-case. It exists as a Docker image that your JupyterHub loads when a user starts a new session. These images can either be built with the tool [repo2docker](https://repo2docker.readthedocs.io/), or pulled directly from a Docker registry. The environment also comes pre-loaded with some tools that are helpful for working with JupyterHub, such as [nbgitpuller](https://jupyterhub.github.io/nbgitpuller).

🤖 hardware
: All of the 2i2c Hubs in this pilot run on Google Cloud, using Kubernetes along with Terraform to orchestrate the cloud infrastructure underlying the hub.

📦 data
: The data that is used by your 2i2c Hub is provided by you! 2i2c Hubs can connect with a variety of public data sources. We recommend using standard data structures or specifications via libraries like [Intake](https://intake.readthedocs.io/en/latest/).

## Where are 2i2c Hubs configured?

All of the configuration and deployment scripts for the 2i2c Hubs can be found at [this GitHub repository][low-touch-hubs]. This repository contains both the deployment code as well as documentation that explains how it works. It should be treated as "for advanced users only", and is provided for transparency and as a guide for the community to follow if they wish to manage their own infrastructure similar to 2i2c Hubs.

## How could I deploy my own 2i2c Hub?

The 2i2c Hubs are all deployed according to best-practices as documented in the following guides:

- For smaller hubs with 5-50 users: [The Littlest JupyterHub Documentation](https://tljh.jupyter.org)
- For larger hubs with 5-100+ users: [The JupyterHub for Kubernetes Documentation](https://z2jh.jupyter.org)

In addition, we recommend checking out [this GitHub repository][low-touch-hubs], which contains the configuration and deployment scripts for all of the hubs offered under this pilot.

[low-touch-hubs]: https://github.com/2i2c-org/low-touch-hubs

## A list of current hubs

```{include} hubs-table.txt
```
