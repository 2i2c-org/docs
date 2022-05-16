# Service Level Objectives

This page describes the **Service Level Objectives** (SLOs) of 2i2c's infrastructure services[^slos].
These are our goals in running infrastructure for the communities that we serve.
They indicate what our users can expect when using the infrastructure we support.
They will evolve over time as we get feedback and learn how to best deliver impact via our services.

:::{note}
2i2c does not currently have a **Service Level Agreement** (SLAs), and the SLOs here are not legally-binding.
We aim to create SLAs once we learn more about our capacity to fulfill them sustainably.[^zenodo]
:::


(objectives:stability)=
## Availability and uptime

The infrastructure that 2i2c runs should be available to its communities 24/7, and with minimal human intervention needed to maintain this level of performance.
We invest in continous development to improve the resiliency and efficiency of the infrastructure that we run, following best-practices in service design and engineering in the cloud.

- Communities should feel comfortable relying on 2i2c's services for critical educational and research needs.
- There should not be prolonged periods of service disruption for any community.
- We will invest in monitoring and reporting infrastructure to detect outages quickly and before they impact end-users.
- When outages do occur, we will prioritize these over other work that our team is doing.

:::{admonition} To be refined...
It is a known anti-pattern to define an ambiguous SLO like "24/7".
Truly meeting such an objective is nearly impossible and extremely costly.
In the future, we plan to run an audit of our infrastructure and practices, and design quantifiable uptime targets for our SLOs.
:::


(objectives:intentional-downtime)=
### Intentional downtime

In some cases there may be intentional downtime for the infrastructure that we run.
For example, if we need to undergo major maintenance of infrastructure transitions.

- We will communicate with communities before any intentional downtime.
- We will aim for downtime windows that happen outside of heavy usage.
- We will communicate with communities when the expected downtime is over.

(objectives:reduced-capacity)=
### Reduced team capacity

There are some periods of time when we have **expected reduced capacity**.
These are periods of time when we are less strict about adhering to the service objectives on this page.
This ensures that our work practices are sustainable and fair for our team.

Here are periods of expected reduced capacity:

- Weekends
- The first and last weeks of the year.
- Periods of overlapping international holidays.

If this is disruptive to your community's activies, please reach out and we can discuss.
However, we encourage you to avoid planning mission-critical events or actions during periods of expected reduced capacity.

:::{admonition} A note on timezones
Remember that 2i2c's team is distributed globally, and our working time zone may be different from yours.
We aim to have team members in time zones that are working at the same time as the communities we serve, but there may occasionally be mis-matches in working hours.
:::

(objectives:support)=
## Support responsiveness

Support is one of the most important services that 2i2c provides, especially when there are problems or outages.
For this reason, we commit to developing a support process that is efficient in responding to issues that communities bring to us.
We define two types of support with 2i2c:

- **Change Requests** are general requests for changes or improvements to a community's hub. For example, updating the environment or improving an open source tool.
- **Incidents** are requests connected with significant degraded service for one or more communities. For example, a system-wide outage or inability of users to log-in.

Below are our objectives broken down by the type of support they relate to.

:::{seealso}
- See [](../support.md) for more information about contacting support.
- See [](tc:support:process) for our team's support process.
:::

### General support objectives

- We have a dedicated communications channel for support (see [](../support.md)).
- At least one team member is always tasked with monitoring this channel.
- Our support team is communicative, helpful, and [abides by our Code of Conduct](tc:code-of-conduct).

### Incident support objectives

Our goal is to be more rapid in responding, communicating, and resolving support requests during incidents.
Our ability to meet these objectives will depend on the times they are reported relative to the working hours of our support team.

- We will triage and respond to Incidents within 8 working hours.
- We will prioritize resolving Inicdents over any other Change requests.
- For major or complex outages, we will re-direct capacity on our engineering team to resolve them.

### Change Request support objectives

- We will triage support requests and respond to them within 24 working hours.
- We will prioritize resolving Change Requests by balancing them against our other development priorities as described in {doc}`our Support Team Process documentation <tc:projects/managed-hubs/support>`)

(objectives:cost)=
## Costs and cloud flexibility

Our communities rely on us to keep their cloud costs as low as possible.
They also rely on us to provide infrastructure that is dynamic and meets the needs of diverse communities.

There is an inherent tension between doing things quickly (which generally requires using extra resources to encourage speed) and cost efficiency (because you pay for those extra resources).
This is particularly relevant during sharp increases in hub usage.

- Communities should feel comfortable that moderate increases in usage will not result in instability.
- Communities should feel comfortable that this flexibility does not result in unexpected cloud costs.
- We should provide this flexibility in a way that is sustainable for our team.
- If infrastructure requires steady, but semi-random usage, we should prioritize cost efficiency.
- If infrastructure will have known spikes of activity, we may temporarily favor speed over cost by asking for extra resources from the cloud provider.
- If spikes in activity will come just after a holiday or weekend, we may make these changes a few days early to avoid working off-hours.

:::{seealso}
See [](pricing/index.md) for more information about costs.
:::


(objectives:updates)=
## Upgrades and maintenance

By continuously upgrading the cloud infrastructure and software environments that our hubs offer, we improve the experience of the communities that we serve by giving them new features, enhancements, and bug and security fixes.

We aim to continuously upgrade this infrastructure in a way that minimizes the risk of instability or outages.

- We will keep our hubs relatively up-to-date with the latest [JupyterHub](https://jupyterhub.readthedocs.io) and [Zero to JupyterHub](https://z2jh.jupyter.org) releases.
- We will ensure that our hub infrastructure is compatible with the latest software releases in the common open source ecosystems we provide.
- We will support open source communities in making regular updates and releases to their tools.

[^slos]: For more about the difference between Service Level Objectives, Agreements, and Indicators, see [the Google SRE handbook](https://sre.google/sre-book/service-level-objectives/).

[^zenodo]: This practice is inspired by [Zenodo's intentional lack of Service Level Agreements](https://about.zenodo.org/principles/).
