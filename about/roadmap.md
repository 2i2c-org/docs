# Roadmap

{octicon}`clock` Updated **2021-09-16**

This roadmap describes our major development priorities for the Managed JupyterHub Service.
It is meant to give an idea of where we hope to focus our efforts in the next several months.
Planning for this roadmap roughly follows a quarterly process, and items may be updated or changed as we learn more about the most important things to work on.
Treat this roadmap as a reflection of interests, not as a concrete promise.

Below we describe major initiatives that are currently active in the Managed Hub Service.

## Hub infrastructure launch

The Managed Hubs Service relies heavily on infrastructure that centralizes the configuration and deployment of many JupyterHub instances.
Our first major project is to use [our Pilot JupyterHubs](https://pilot-hubs.2i2c.org/en/latest/reference/hubs.html) to drive development on this infrastructure stack.

:::{note}
We are also [using an issue](https://github.com/2i2c-org/pilot-hubs/issues/610) to track long-term infrastructure needs for this service across all cloud providers.
That is more comprehensive and bigger in scope than any one initiative.
:::

Our goal for this initiative is to have **basic infrastructure that automates the deployment of Kubernetes clusters and JupyterHubs**.

:::{admonition} Deliverables for this initiative
You can find deliverables for this initiative at [this project board](https://github.com/orgs/2i2c-org/projects/10)
:::

This initiative has the following major areas of work:

- **Automation** - Automation is a critical part of scaling a service and minimizing manual steps with human intervention. We need to automate deployment and configuration of critical tools to deploy JupyterHub on Kubernetes.
- **Reporting and Quality Assurance** - Hub Administrators and Engineers should be confident that hubs are battle-tested and should know quickly if things are not working as expected. We should build basic reporting mechanisms and testing infrastructure that reports back what is going on with our infrastructure, as well as basic processes to ensure the quality of our hub deployments.
- **Basic hub setups** - Hub Administrators will want a basic environment that is useful to them. We need to make reasonable choices in Hub Infrastructure and the use-cases it enables.
- **Basic customizability** - Hub Administrators will want to customize their infrastructure to a degree. We should build in basic customization and configuration that does not require intervention from a 2i2c Engineer.

## Hub service model

In addition to basic infrastructure, 2i2c also requires a service model that makes it possible for communities to use the infrastructure, and that ensures the reliability of the infrastructure.
These largely require organizational, administrative, and team practices to operate and improve the Hub Service.

Our goal for this initiative is to have **a working support and operations plan, a sales plan, team coordination practices, and administrative infrastructure to support this service.

:::{admonition} Deliverables for this initiative
You can find deliverables for this initiative at [this project board](https://github.com/orgs/2i2c-org/projects/15)
:::

This initiative has the following main areas of work:

- **Administration** - In order to run a service that charges customers, we'll need an administrative process and infrastructure to handle the financial, legal, etc aspects. 
- **Support and operations model** - The Hub Engineering team will need to coordinate Development and Operations of the hub service in partnership with those administering the service. This will require practices for coordination and prioritization.
- **Sales model** - In order to receive funding for running hubs for communities, we'll need a sales and pricing model that lets us sign contracts.
- **Documentation** - As this will be a public-facing service, it will be crucial that we build high-quality public-facing documentation that describes the service and infrastructure.
