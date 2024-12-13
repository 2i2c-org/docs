```{team} Service Team
```
# Shared responsibility model

2i2c **shares responsibility for each hub** with the communities we serve.[^similar-models]
This aligns with our mission of promoting collaborative and open workflows in research and education.
It also leads to a more effective, more sustainable, and more transparent service[^ironies-automation], and ensures that the community has the [Right to Replicate](https://2i2c.org/right-to-replicate) their infrastructure. Here's how it works:

1. Define the major responsibilities needed to run a hub service with a community, and categorize them broadly by skillset.
2. Assign responsibilities that are well-suited to the skills and the interests of each group.
3. Choose an operational and cost model for the group so that each actor is empowered to carry out their responsibilities.

Below is a high-level summary of the major areas of responsibility in this service and how they work together.

% This figure is not stored with the repository, it is downloaded at build time
% Diagram here: https://drive.google.com/uc?export=download&id=16r5xE7SguunLfMh5LhSynSUfjb7IXs_n
```{figure} /images/shared_responsibility_diagram.png
:figwidth: 80%
An overview of the major teams that collaborate around the cloud service in order to serve a community of users.
```

Below we describe these areas in more detail, and define the roles that 2i2c and our partner communities take on in the service.

:::{contents}
:local:
:depth: 1
:::

## Site Reliability Engineering

**Key goal**: Ensure that the cloud infrastructure is reliable, robust, and scalable.

### Responsibilities

% NOTE: Goal is to have max 5 responsibilities per category, to avoid overwhelming people.
1. **Monitor infrastructure for errors**. Continuously monitor cloud infrastructure to identify usability problems before they affect users.
2. **Respond to incidents**. When incidents are identified or reported, carry out an incident response process to diagnose and resolve the incident.
3. **Deploy and configure the cloud environment**. Make the necessary service connections and technical changes to set up the community's environment (e.g., authenetication, connecting with a database or defining RAM per user, etc).
4. **Enhance and develop cloud infrastructure**. Continuously develop and deploy software improvements with the goal of boosting service reliability and scalability.
5. **Operate a Kubernetes cluster**. This is the cloud platform that manages all of a community's infrastructure, and may be shared between many communities.

```{role} Site Reliability Engineer
```

```{admonition} Role: Site Reliability Engineer
A team of engineers with expertise in cloud infrastructure and open source tools that we use as part of our services. This group of people oversees the cloud infrastructure that a community uses. They perform new development and upgrades, make changes per the request of {team}`Community Representatives`, and coordinate with the {team}`Community Support Team` during incidents and outages.
This is roughly equivalent to a [Site Reliability Engineering Team](https://en.wikipedia.org/wiki/Site_reliability_engineering).

See [our Infrastructure documentation](https://infrastructure.2i2c.org/en/latest/) for more information.

**Usually filled by 2i2c team members.** Though we are experimenting with ways to involve community members in our cloud operations.
```

### Responsibility breakdown

Usually, 2i2c assumes responsibility for all of the above, though we are experimenting with ways to involve community members in our cloud operations.

## Service applications support

**Key goal**: Ensure that communities have the skills and understanding needed to use the cloud infrastructure to have an impact.

### Responsibilities]

1. **Create documentation and training material**. Write and improve content that helps users learn cloud-native workflows and use the infrastructure effectively.
2. **Provide support to community leaders**. Follow our service {ref}`support prcoess<tc:support:process>` for community leaders.
3. **Assist with user environment creation**. Provide domain expertise about how to configure and set up the proper environment using [Binder-style repositories](/admin/howto/environment/index.md).
4. **Create and manage data in the cloud**. If your communities requires access to a cloud-native dataset, format it properly and put it in a place that the hub can connect to.
5. **Run workshops and training**. Training workshops are geared towards community leaders, with the goal of helping them share knowledge with others in their community.

```{role} Community Guide
```
```{admonition} Role: Community Guide

An expert practitioner with familiarity in user workflows as well as the technical use-cases that 2i2c's cloud services enable.
Acts as a bridge between the communities we work with and our {role}`Site Reliability Engineer`s. Facilitates information transfer, signal-boosts community needs and requests, and guides communities in utilizing the infrastructure more effectively.

See the {ref}`Support Team Documentation <tc:support:process>` for more information.

**Usually filled by 2i2c team members.** Though communities with "Power Users" or those with exceptional engineering and computational skills may serve in this role as well.
```

### Responsibility breakdown

Generally shared between 2i2c and the community partners it works with.
We focus our efforts on general use-case training for community leaders, as well as documentation.
However, our base service model does not allow us to spend extensive time managing complex environments or cloud-native datasets on behalf of communities.

## Community leadership and management

**Key goal**: Ensure that a hub's community has the structure, support, and leadership to make the most of the hub.

### Responsibilities

A team of leaders *within the community that we work with* who act as {team}`Community Representatives` on behalf of their community. This team coordinates more closely with our {team}`Community Support Team`, facilitates the transfer of knowledge between 2i2c teams and communities of users, and helps manage the structure and dynamics of these communities. They also define the strategic mission and goals of each user community, and help us define the definition of "success" for the hub service.

1. **Define success for the hub's community**. Community leaders understand the goals of a community's users, and define whether the hub is meeting their needs.
2. **Oversee user access policy**. Decide who has access to the hub, and what permissions they have. Generally done via the JupterHub admin panel.
3. **Manage and cultivate a community around the hub.** Define the community events, processes, structure, and communication channels that are best for a hub's community.
4. **Represent community in decisions and feedback**. Serve as a point of contact for {role}`Site Reliability Engineer`s, make requests for changes to the hub, and surface incidents or problems if they arise.
5. **Make financial decisions about the hub**. Have decision authority for changes that have a financial impact on the infrastructure, and serve as a point of contact for billing matters.

```{role} Hub Administrator
```
```{admonition} Role: Hub Administrator

Trusted community members that perform common administrative operations on a hub that do not require intervention from a Hub Engineer.
{team}`Community Representatives` are the first Hub Administrators, and they may add new Hub Administrators via the JupyterHub interface.
They are able to add users, start/stop servers, and generally have more control over operations on the hub.

**Filled by a community member**.
```

```{role} Community Representative
```
```{admonition} Role: Community Representative

Acts as the primary point of contact for a community, and ensures that the interests of the {team}`Hub Community` are represented in the infrastructure, and that the hub serves their needs.

They have the authority to speak on behalf of the community, and make decisions about the infrastructure that the community uses.

**Filled by one or two community leaders**.
```

### Responsibility breakdown

Community management and leadership is generally the responsibility of the community.

## Software engineering

**Key goal**: Improve and maintain open source tools to support community workflows.

### Responsibilities

1. **Develop domain-specific software** that is relevant to your community members for their specific use-cases.
2. **Develop software for interactive computing** to improve the underlying infrastructure that provides user sessions (e.g., JupyterHub, JupyterLab, etc).
3. **Support open source communities** so that the service infrastructure has a solid and reliable foundation of tools on which it runs, and so that the communities that produce those tools are healthy.

**There are no formal roles for this area**. 2i2c does not currently have the capacity for dedicated software development, though it hopes to grow this capacity in the future.

### Responsibility breakdown

Software development is performed by community members or their partners.

[^ironies-automation]: Even when collaborating with engineering expertise in other organizations, we describe our service model in terms of areas of responsibility, rather than "tiers" of service that provide "burst capacity" or support only on an as-needed basis. This is because service "tiers" often leads to anti-patterns where support is needed from a person that is not empowered to be efforted in their duties (e.g., if they have been away from infrastructure for many months, and only after a series of escalations are needed to debug something). For more information on this, see [the Ironies of Automation](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf) as well as [this post](https://blog.acolyer.org/2020/01/08/ironies-of-automation/) and [this post](https://www.thinkautomation.com/automation-advice/the-ironies-of-automation-explored/) explaining its relevance to technology and service delivery.

[^similar-models]: This is inspired by the **Shared Responsibility Model** that is often used to describe cloud services. For example, see [the AWS Shared Responsibility model for compliance](https://aws.amazon.com/compliance/shared-responsibility-model/) and for [Best Practices](https://aws.amazon.com/blogs/industries/applying-the-aws-shared-responsibility-model-to-your-gxp-solution/), the [GxP whitepaper from Google Cloud](https://cloud.google.com/security/compliance/cloud-gxp-whitepaper), and the [Azure Shared Responsibility Model](https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).
