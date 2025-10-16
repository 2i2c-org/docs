# Security foundations

2i2c hubs are built on industry-standard security practices and are designed to be secure by default.

## Zero to JupyterHub

All 2i2c cloud infrastructure is deployed using the [Zero to JupyterHub Helm Chart](https://z2jh.jupyter.org/) (Z2JH), which is the community standard for deploying JupyterHub in Kubernetes. This project is maintained by the Jupyter community and follows the principle of "secure by default."

Here are a few security features and design decisions that ensure security in Z2JH:

- Properly isolate user environments from one another
- Prevent users from accessing resources or data that is forbidden to them
- Follow cloud security best practices

As members of the JupyterHub team, 2i2c is constantly working to improve [the security of Zero to JupyterHub](https://z2jh.jupyter.org/en/stable/administrator/security.html), and we use our experience running these hubs to identify and address security concerns.

## User isolation

Each user's server runs in an isolated environment that prevents them from:

- Accessing other users' files or data
- Interfering with other users' computational processes
- Accessing system resources beyond what they've been allocated
- Escalating their privileges on the hub

## Abuse prevention and monitoring

2i2c deploys monitoring and prevention tools to protect hubs from abuse.

### Cryptocurrency mining prevention

Cryptocurrency mining abuse occurs when users take advantage of cloud CPU to make money by mining cryptocurrency. It is a common problem with cloud-based services and platforms.

We deploy an open-source tool called [`cryptnono`](https://github.com/yuvipanda/cryptnono) to each of the clusters we manage. This tool monitors any process that runs on 2i2c hubs and automatically kills any associated with cryptocurrency mining (particularly *Monero*, the most common cryptocurrency for abuse due to its anonymous nature).

This protection runs automatically on all hubs.

### Monitoring for abnormal behavior

We deploy [Grafana Dashboards](https://grafana.com/grafana/dashboards/) along with a [Prometheus Server](https://prometheus.io/) to continuously monitor usage across all hubs.

This provides visual dashboards that allow us to identify abnormal behavior on a hub, such as:

- A single user using unusual amounts of RAM
- Excessive CPU usage patterns
- Unusual networking requests
- Unexpected cost patterns

See [](../monitoring/index.md) for more information about monitoring tools available to hub administrators.

## Additional security configuration

Beyond these baseline protections, hub administrators can configure additional security features:

- **Network access controls**: See [](internet-access.md) for controlling what external resources users can access
- **Secrets management**: See [](managing-secrets.md) for securely managing sensitive information

## Reporting security concerns

If you discover a security issue with your hub or 2i2c infrastructure, please report it by [opening a support ticket](../../support.md).
