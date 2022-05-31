# Shared Responsibility Model

Many things must be done to successfully run a hub for a community.
Some of them are content-focused, some are community-focused, others are infrastructure-focused.

2i2c's aim is to **share responsibility for each hub** with the communities we serve. We do this by defining the responsibilities that are a good fit for the skills and goals of each organization.
This "Shared Responsibility Model" is a useful way to understand what actions communities are still expected to perform under a service agreement with 2i2c.[^1]

[^1]: This is inspired by the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) from Amazon Web Services.

## Why follow this model

We use a Shared Responsibility model because we believe that it leads to the best service for the communities that we serve.
Our main goal is to ensure that each hub service is maximally impactful for the community it serves, and that it achieves this impact in the most efficient way possible.[^ironies-automation]

[^ironies-automation]: Even when collaborating with engineering expertise in other organizations, we describe our service model in terms of areas of responsibility, rather than "tiers" of service that provide "burst capacity" or support only on an as-needed basis. This is because service "tiers" often leads to anti-patterns where support is needed from a person that is not empowered to be efforted in their duties (e.g., if they have been away from infrastructure for many months, and only after a series of escalations are needed to debug something). For more information on this, see [the Ironies of Automation](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf) as well as [this post](https://blog.acolyer.org/2020/01/08/ironies-of-automation/) and [this post](https://www.thinkautomation.com/automation-advice/the-ironies-of-automation-explored/) explaining its relevance to technology and service delivery.

To do that, we want to do two things:

- Assign responsibilities that are well-suited to the skills and the interests of each group. This will boost the impact of each party.
- Choose the operational model that is most well-matched to whomever is carrying out a responsibility. This will boost the efficiency of each party.

Our challenge is to figure out which responsibiltiies should lie with the community, and which should lie with the 2i2c team, to strike this balance of impact and efficiency.

We also follow this model because it helps us ensure that the community has the [Right to Replicate](https://2i2c.org/right-to-replicate) their infrastructure.
We think of our community hubs as being a collaboration between 2i2c and the communities that use it, and this framing helps us be explicit about where we fit into the picture.
By defining the roles and responsibilities that we take on via our services, this provides a natural place for other communities to take on some responsibility if they have the capacity to do so.

## Example responsibilities

Below are a few responsibilities that are involved in running a community hub, they are roughly ordered from "least to most technical".
In [2i2c's service model](overview.md), our responsibility generally begins around number 7.
However, for some communities we may take on more or less responsibility and adjust our costs accordingly depending on their needs.

::::{grid}

:::{grid-item}
:columns: 2

**Less technical**

```{div} mt-auto
**More technical**
```

:::

:::{grid-item}
:columns: 10

1. Advocating for the DataHub's usage to the Berkeley community.
2. Guiding, teaching, and sharing skills on the DataHub with others
3. Providing requests and feedback for changes to the DataHub infrastructure
4. Providing user support for questions related to their use-case
5. Performing straightforward environment changes
6. Doing basic administrative tasks on the hub (adding users, joining user sessions, etc)
7. Identifying when there is an outage, and escalating to the proper team to resolve them.
8. Performing more complex environment changes
9. Overseeing changes to the Kubernetes configuration of the hub
10. Adding or removing hubs and doing the corresponding clean-up
11. Performing development of the open source tools in JupyterHub/Jupyter/related tools
12. Performing upgrades and improvements to the hub's cloud infrastructure
13. Responding to and resolving incidents related to Kubernetes and cloud infrastructure

:::

::::
