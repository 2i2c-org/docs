# Overview of hub features

2i2c builds and operates **distributions of JupyterHubs** that are tailored for particular use-cases.
These services share many of the same infrastructure components, but have customizations and optimizations that are more domain- or community-specific.

```{figure} https://drive.google.com/uc?export=download&id=1vL8ekAtUQ4TEik4-oWIn36VAOITdlmpR
:width: 80%

A high-level technical overview of an Interactive Computing Service collaboratively run by 2i2c and a community of practice. Each hub is a JupyterHub Distribution with a collection of community-led open source projects that are customized for a particular use-case.
```


Here is a brief overview of the major features that are present in each.

```{csv-table}
:header-rows: 1
:widths: auto
:file: ../../build_assets/feature-matrix.csv
```

<script>
    headers = document.querySelectorAll(".feature-header");
    headers.forEach((header) => {
        td = header.parentElement
        td.setAttribute("colspan", "100")
        td.classList.add("feature-header")
        tr = td.parentElement
        tr.querySelectorAll("td:not(.feature-header)").forEach((td) => {
            td.remove()
        })
    })
</script>
<style>
    td.feature-header {
        font-weight: 500;
        background-color: #f8f9fa;
    }
</style>


## JupyterHub in the cloud

At the core of a community service is one or more [JupyterHubs](https://jupyter.org/hub) that provide an access point for interactive computing and cloud infrastructure for your community members.

You may access your community JupyterHub at a URL with the following form (though you may choose a custom URL if you wish):

```
<hub-name>.<community-name>.2i2c.cloud
```

JupyterHub provides interactive computing sessions for each of your users, and connect to the other infrastructure in the cloud.
Our JupyterHubs can run on Google Cloud, Amazon AWS, or Microsoft Azure.

## Authentication

We use [CILogon](https://www.cilogon.org/) for authenticating users, which can connect to a number of other authentication protocols (such as OAuth2). We also
directly support connecting to GitHub, for working with Teams and Organization
based Authentication.

## User interfaces

Each 2i2c JupyterHub has two main interactive interfaces: Jupyter interfaces (Notebook and Lab), and RStudio. Each of them is accessible from your session via `/tree`, `/lab`, and `/rstudio` endpoints in your URL.

## Custom user environments

Your 2i2c JupyterHub has an environment that has been created for your particular use-case. It exists as a Docker image that your JupyterHub loads when a user starts a new session. These images can either be built with the tool [repo2docker](https://repo2docker.readthedocs.io/), or pulled directly from a Docker registry. The environment also comes pre-loaded with some tools that are helpful for working with JupyterHub, such as [nbgitpuller](https://jupyterhub.github.io/nbgitpuller). See [](environment/custom) for more information.

## Transparent infrastructure and operations

All of the configuration and deployment scripts for the 2i2c JupyterHub can be found at [the `infrastructure/` repository](https://github.com/2i2c-org/infrastructure). This repository contains both the deployment code as well as documentation that explains how it works. It should be treated as "for advanced users only", and is provided for transparency and as a guide for the community to follow if they wish to manage their own infrastructure similar to 2i2c JupyterHub.

To learn about how the `infrastructure/` repository works, we recommend checking out the [`infrastructure` documentation](inv:infra#index).

See the next sections for more information about each hub distribution.

## Secure out of the box

The cloud infrastructure that we manage follows best-practices in deploying cloud applications in a secure manner.
The [Zero to JupyterHub Helm Chart](https://zero-to-jupyterhub.readthedocs.io/en/latest/) is the community standard in deploying JupyterHub in the cloud, and is what 2i2c uses in all of its cloud hubs.
This project follows the principle of "secure by default", and has a number of configuration and design decisions that properly isolate user environments from one another, and prevent them from being able to access resources or data that is forbidden to them.

As members of the JupyterHub team, we are constantly looking for ways to improve [the security of Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/security.html), and use our experience running these hubs to further improve JupyterHub's security.

### Data privacy

2i2c will not collect user data for any purpose beyond what is required in order to run a JupyterHub.
Depending on the choices of your community the hub might contain identifiable information (e.g., e-mail addresses used as usernames for authentication), but this will remain within your hub's configuration and is not shared publicly.

Our {role}`Site Reliability Engineer`s will have access to all of the information that is inside a hub (which it requires in order to debug problems and and assist with upgrades), however we will not retain any of this data or move it *outside* of the hub, and will not retain it once the hub is shut down (except in order to transfer data to you at your request).

## Monitored for abuse and unexpected costs

We deploy [Grafana Dashboards](https://grafana.com/grafana/dashboards/) along with a [Prometheus Server](https://prometheus.io/) to continuously monitor the usage across all of our hubs.
This provides visual dashboards that allow us to identify abnormal behavior on a hub (such as a single user using unusual amounts of RAM, using a lot of CPU, or making unusual networking requests).

### Cryptocurrency mining

Cryptocurrency mining abuse occurs when users take advantage of cloud CPU in order to make money by mining cryptocurrency.
It is a common problem with cloud-based services and platforms.

There are many different cryptocurrencies out there, but the most common by-far for abuse is [the Monero cryptocurrency](https://www.getmonero.org/) due to its anonymous nature.

We deploy an open-source tool called [`cryptnono`](https://github.com/yuvipanda/cryptnono) to each of the clusters we manage.
This tool monitors any process that runs on the 2i2c hubs, and automatically kills any that are associated with Monero.
