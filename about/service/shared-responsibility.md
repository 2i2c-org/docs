# Shared Responsibility Model

Many things must be done to successfully run a hub for a community.
Some of them are content-focused, some are community-focused, others are infrastructure-focused.

2i2c **shares responsibility for each hub** with the communities we serve. We do this by defining the responsibilities that are a good fit for the skills and goals of each organization.
This "Shared Responsibility Model" is a useful way to understand what actions communities are still expected to perform under a service agreement with 2i2c.[^1]

[^1]: This is inspired by the **Shared Responsibility Model** that is often used to describe cloud services. For example, see [the AWS Shared Responsibility model for compliance](https://aws.amazon.com/compliance/shared-responsibility-model/) and for [Best Practices](https://aws.amazon.com/blogs/industries/applying-the-aws-shared-responsibility-model-to-your-gxp-solution/), the [GxP whitepaper from Google Cloud](https://cloud.google.com/security/compliance/cloud-gxp-whitepaper), and the [Azure Shared Responsibility Model](https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).

```{figure} https://drive.google.com/uc?export=download&id=1SIhHrzPXSFBZ0yyVpxHm0WYs63k0SBRQ
:width: 80%

An overview of some categories of shared responsibility between the {term}`Cloud Engineering Team` and the {term}`Community Leadership Team`.
```

```{figure} https://drive.google.com/uc?export=download&id=1S6Y9TQcXXLkrGrhgXQc7kLzq7dxcuw9a
:width: 80%

An overview of some categories of shared responsibility between the {term}`Community Support Team` and the {term}`Community Leadership Team`.
```

:::{seealso}
[](../strategy/service-objectives.md) has information about our goals for uptime, reliability, and responsiveness in running this service.
:::

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
In [2i2c's service model](index.md), our responsibility generally begins around number 7.
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

1. **Use** the interactive computing sessions to accomplish the goals of the community.
2. **Advocate and onboard** new users to the hub to grow its user community.
3. **General user support** for generic questions about interactive computing.
4. **Provide user access** via the JupterHub admin panel to create new usernames and administrative users.
5. **Develop domain-specific software** that is relevant to your community members for their specific use-cases.
6. **Define the basic environment** via a Binder-style repository.
7. **Manage data** that is accessed by users.
8. **Guide 2i2c** with requests and feedback for changes to infrastructure
9. **Escalate to 2i2c** when something is wrong.
10. **Complex environment changes** that require more expertise in packaging and environment design.
11. **Develop software for interactive computing** to improve the underlying infrastructure that provides user sessions (e.g., JupyterHub, JupyterLab, etc).
12. **Support open source communities** so that the service infrastructure has a solid and reliable foundation of tools on which it runs, and so that the communities that produce those tools are healthy.
13. **Communicate with cloud provider** for issues related to infrastructure (e.g., requesting resource limit increases).
14. **Manage Kubernetes configuration** to perform updates to a hub or cluster (e.g., changing RAM available).
15. **Deploy and configure hubs** including configuration, guidance for setting up environment, some connections to cloud resources, etc.
16. **Monitor for incidents** to identify usability problems before they affect users.
17. **Develop software for cloud infrastructure** to improve the performance, features, and robustness of Kubernetes and other cloud infrastructure.
18. **Configure Kubernetes** upgrades and improvements for cloud infrastructure.
19. **Respond to incidents** when a more complex or cloud-related change is needed.
20. **Operate a Kubernetes cluster** that is configured to manage one or more JupyterHubs.

:::

::::
