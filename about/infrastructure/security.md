# Security and Abuse

The cloud infrastructure that we manage follows best-practices in deploying cloud applications in a secure manner.
This page describes a few ways in which we make our hubs more secure and prevent them from abuse.

## Secure out of the box

The [Zero to JupyterHub Helm Chart](https://zero-to-jupyterhub.readthedocs.io/en/latest/) is the community standard in deploying JupyterHub in the cloud, and is what 2i2c uses in all of its cloud hubs.
This project follows the principle of "secure by default", and has a number of configuration and design decisions that properly isolate user environments from one another, and prevent them from being able to access resources or data that is forbidden to them.

As members of the JupyterHub team, we are constantly looking for ways to improve [the security of Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/security.html), and use our experience running these hubs to further improve JupyterHub's security.


## Data privacy

2i2c will not collect user data for any purpose beyond what is required in order to run a JupyterHub.
Depending on the choices of your community the hub might contain identifiable information (e.g., e-mail addresses used as usernames for authentication), but this will remain within your hub's configuration and is not shared publicly.

Our {term}`Cloud Engineering Team` will have access to all of the information that is inside a hub (which it requires in order to debug problems and and assist with upgrades), however we will not retain any of this data or move it *outside* of the hub, and will not retain it once the hub is shut down (except in order to transfer data to you at your request).


## Cryptocurrency mining

Cryptocurrency mining abuse occurs when users take advantage of cloud CPU in order to make money by mining cryptocurrency.
It is a common problem with cloud-based services and platforms.

There are many different cryptocurrencies out there, but the most common by-far for abuse is [the Monero cryptocurrency](https://www.getmonero.org/) due to its anonymous nature.

We deploy an open-source tool called [`cryptnono`](https://github.com/yuvipanda/cryptnono) to each of the clusters we manage.
This tool monitors any process that runs on the 2i2c hubs, and automatically kills any that are associated with Monero.

## Usage monitoring

We deploy [Grafana Dashboards](https://grafana.com/grafana/dashboards/) along with a [Prometheus Server](https://prometheus.io/) to continuously monitor the usage across all of our hubs.
This provides visual dashboards that allow us to identify abnormal behavior on a hub (such as a single user using unusual amounts of RAM, using a lot of CPU, or making unusual networking requests).
