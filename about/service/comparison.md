# Comparison to similar services

We believe that the research and education community is best-served by open, community-driven infrastructure and services.
However, there are many things to consider when choosing services to support and use.
This section describes a few major categories to think about as well as the major kinds of services available to you - we'll discuss each in the sections below as well.
They are roughly ordered from "most similar" to "least similar" to 2i2c.

For some excellent comprehensive guides, we also recommend reading these two resources:

- [The Principles of Open Scholarly Infrastructure](https://openscholarlyinfrastructure.org/) describes how infrastructure and services can align themselves with the mission and values of the scholarly community. We recommend that you use services that align closely with these principles.
- [The Values and Principles Framework and Assessment Checklist](https://commonplace.knowledgefutures.org/pub/5se1i1qy/release/4) is an assessment checklist to help those in the scholarly community choose services that are aligned with the mission and values of the scholarly community.

## 2i2c's qualifications

```{epigraph}
2i2c is a mission-driven non-profit with expertise in cloud infrastructure, Jupyter, open science and scholarship, and open development practices.
```

2i2c provides a **managed, customized JupyterHub service** that is tailored for research and education communities.
We manage entirely non-proprietary, open-source tools that ensure user communities have the [Right to Replicate](http://2i2c.org/right-to-replicate) this infrastructure with or without 2i2c.
As a part of this service, 2i2c also makes **upstream contributions to open-source communities** as a part of continuously operating and improving this infrastructure.

This page describes why we believe that 2i2c and its service model is uniquely suited for the research and education communities.

:::{tip}
The content on this page can be re-used as a part of "uniqueness and sole source justification" forms when completing contracting for communities.
:::

### Expertise in managed cloud infrastructure in research and education

Our team has developed and managed cloud infrastructure for over 5 years - first at our previous institutions and now as a part of 2i2c.
We follow modern practices for Site Reliability Engineering with cloud infrastructure like Kubernetes and JupyterHub.
This makes 2i2c uniquely capable of managing scalable and reliable cloud infrastructure for interactive computing.

Here are a few of the major projects our team members have been involved in over the past few years.

- [The Pangeo project](https://pangeo.io/) - A community platform for Big Data geoscience connecting researchers across the world to large-scale computing and data infrastructure.
- [The UC Berkeley DataHubs](https://docs.datahub.berkeley.edu/) - A collection of university-wide JupyterHubs for education serving many thousands of students.
- [The Binder Project](https://docs.mybinder.org/) - a large public cloud service for reproducible computing environments using JupyterHub, serving nearly 150,000 sessions each week.
- [The Syzygy Project](https://syzygy.ca/) - A network of federated JupyterHubs for more than 15 Canadian Universities running on national infrastructure.
- [The Jupyter Book](https://jupyterbook.org) and [MyST Markdown](https://myst.jupyterbook.org/) projects - A collection of tools and standards for improving scientific and technical communication and authoring with interactive computing.

### Expertise in open source workflows and Jupyter

2i2c's team is comprised of several "[Distinguished Contributors](https://jupyter.org/about)" in the Jupyter ecosystem, which is a crucial technical component of this service.
We are [core team members of JupyterHub and Binder](https://jupyterhub-team-compass.readthedocs.io/en/latest/team/index.html), and make regular contributions across the Jupyter ecosystem.
Moreover, our team has many years of experience with all aspects of the Jupyter stack and we are comfortable interacting with open source communities everywhere.
This makes 2i2c uniquely capable of both utilizing and improving this technology through upstream contributions.

### Expertise with research and education workflows

2i2c has years of experience managing cloud resources specifically for research and education communities.
We have led and contributed to projects like [the Binder Project](https://docs.mybinder.org/), [the Pangeo Project](https://pangeo.io/), [the Syzygy Project](https://syzygy.ca/), [the UC Berkeley DataHubs](https://docs.datahub.berkeley.edu/en/latest/), and [the Jupyter Book project](https://jupyterbook.org) to serve thousands of users in the research and education community.
As a non-profit, we have defined our mission in order to serve research and education sector, and our team and governing body is made up of individuals from this community.
We strive to build an understanding of their needs, to represent their interests in the Jupyter and open source ecosystem, and to collaborate with them in our operations and development.
2i2c is uniquely positioned to serve as a collaborator for research and education via these efforts.

### A transparent, collaborative non-profit

2i2c is a mission-driven non-profit organization that has a commitment to doing its work openly, transparently, and inclusively.
Our mission is to provide researchers and educators with the infrastructure they need to do their work, and to support open source communities that underlie this infrastructure.
2i2c is governed by a {doc}`Steering Council <tc:organization/role/steering-council>` made of members from the research and education community.
2i2c manages all of our work in public spaces, including [all of our infrastructure](http://github.com/2i2c-org/infrastructure) as well as [all of our organizational strategy and practices](http://team-compass.2i2c.org/).


## Major factors to consider

There are a few major categories to consider, and we'll provide a brief description of each below.

::::{grid} 1 1 2 2
:gutter: 3
:class-row: full-width

:::{grid-item-card}
:class-header: bg-light

Usage cost
^^^

How much does the infrastructure itself cost to use (either in monthly fees or in cloud costs)?

**Why it matters**: The amount of cloud cost you incur is heavily dependent on how you optimize and configure your infrastructure. The same group of users can use orders of magnitude more in cloud costs if the proper safeguards and put on their infrastructure.
:::

:::{grid-item-card}
:class-header: bg-light

Person cost
^^^

How much time does it take to maintain and manage the service, and how much does that time cost?

**Why it matters**: The more time you must spend configuring, debugging, improving, and supporting infrastructure, the less time you have for focusing on your other goals. Cloud infrastructure can be a significant time-sink if you are not already skilled in running it.
:::

:::{grid-item-card}
:class-header: bg-light

Right to replicate
^^^

Does the infrastructure run in a way that you could replicate the end-service nearly identically on your own?

**Why it matters**: Using infrastructure that is community-owned and portable prevents you from becoming too-dependent on a single vendor or service. Vendor lock-in is very common in the scholarly community, and eventually creates major problems in cost and usability.
:::

:::{grid-item-card}
:class-header: bg-light

User portability
^^^

Could the user port their workflows to a different service or local setup with minimal disruption?

**Why it matters**: Users are continuously moving between communities in their training and in doing their work. Using tools, interfaces, and workflows that are community standards ensures that they will have minimal friction in using your infratsructure, and in taking their skills elsewhere.

:::

:::{grid-item-card}
:class-header: bg-light

OSS Support
^^^

Does this service reliably drive resources and support to open source communities that underlie the service?

**Why it matters**: Open source communities are in desperate need of financial and personnel support to keep their infrastructure healthy and dynamic. Organizations that commit to re-investing significant resources into open source communities ensure that the tools we all rely on are well-supported and thriving.

:::

:::{grid-item-card}
:class-header: bg-light

Scalable
^^^

How complex is it to scale this option to many users, high-performance infrastructure, or big data?

**Why it matters**: Scaling up (e.g., one user with 10x more RAM) or scaling out (e.g., 10 users becoming 1000 users) both come with significant increases in cloud complexity. If a service is not designed with scalability from the start, it will be difficult to scale your infrastructure if needed.

:::

:::{grid-item-card}
:class-header: bg-light

Customizable
^^^

How much control do you have over the experience that your users have? Can you control the environment, interface, etc?

**Why it matters**: While much of our infrastructure can be re-used across workflows and use-cases, most communities still require customization that is unique to their needs. For example, installing custom packages, modifying interfaces, or adding extensions. Customizability allow you to take more ownership over your infrastructure and the workflows it enables.

:::

:::{grid-item-card}
:class-header: bg-light

Resilient
^^^

Is this option vulnerable to bottlenecks in individual skills and capacity, or is it fault-tolerant and sustained by a group?

**Why it matters**: Cloud infrastructure is dynamic and requires constant upkeep and care from experts. If there is insufficient maintenance capacity, or the infrastructure is not designed properly, then small problems can balloon into large issues that impact your users.

:::

:::{grid-item-card}
:class-header: bg-light

Openness
^^^

How easy is it to use this infrastructure to facilitate collaboration and access for community members within and between institutions.

**Why it matters**: Many communities exist across institutional boundaries (for example, a cross-university collaboration). However, many services put up barriers to access that allows them to track your information, pay for service, or prevent certain kinds of people from getting in. This may have a negative impact on your community's ability to collaborate and grow.

:::

:::{grid-item-card}
:class-header: bg-light

Cutting edge
^^^

How closely does this infrastructure track the latest developments in data science, interactive computing, and cloud technology?

**Why it matters**: The world of data science and open source tools is constantly improving and evolving. The same is true for cloud infrastructure. Keeping up to date with these developments is a lot of work, but results in a much better experience for your community's users.
:::
::::

## Overview of services

Below is a short table summarizing the kinds of services discussed below, and how they (roughly) perform for each of the factors discussed above.
It makes some simplifications and assumptions, and is meant to be a quick and "glanceable" way to compare options.

::::{grid} 3
:margin: 1

:::{grid-item}
✅ = yes / easy
:::
:::{grid-item}
🟧 = sometimes / depends
:::
:::{grid-item}
❌ = rarely / difficult
:::
::::

:::{list-table}
:widths: 15 10 10 5 5 5 5 5 5 5 5
:class: align-middle full-width
:stub-columns: 1
:header-rows: 1

- - Service
  - Usage cost
  - Person Cost
  - Right to Replicate
  - User portability
  - OSS Support
  - Scalable
  - Customizable
  - Resilient
  - Accessible
  - Updates
- - [2i2c](compare:2i2c)
  - 💲💲
  - 💲
  - ✅
  - ✅
  - ✅
  - ✅
  - ✅
  - ✅
  - ✅
  - ✅
- - [Internal Staffing](compare:internal)
  - 💲💲
  - 💲💲💲💲
  - 🟧
  - ✅
  - 🟧
  - ❌
  - ✅
  - ❌
  - ✅
  - 🟧
- - [National infrastructure](compare:public-infra)
  - 💲
  - 💲💲
  - 🟧
  - ✅
  - 🟧
  - 🟧
  - 🟧
  - 🟧
  - ❌
  - ❌
- - [Consultancy](compare:consulting)
  - 💲💲
  - 💲💲💲
  - 🟧
  - ✅
  - 🟧
  - ❌
  - ✅
  - 🟧
  - ✅
  - ✅
- - [SaaS Products](compare:saas)
  - 💲💲💲
  - 💲
  - ❌
  - ❌
  - 🟧
  - ✅
  - ❌
  - ✅
  - ❌
  - 🟧
:::

In addition, jump to a quick explanation of each type of service below:

:::{contents} Jump to service description
:depth: 1
:local:
:::

(compare:2i2c)=
### 2i2c's managed cloud service

As a non-profit, we choose our prices to move forward on a sustainable path to achieve our mission according to our {doc}`fundraising strategy <tc:finance/fundraising>`.
Our service entails developing and managing entirely open-source, vendor-agnostic, and community-driven infrastructure that is customized for research and education.

We curate and integrate this infrastructure, customize it for use-cases in research and education, and contribute back to the open source communities that underlie the tools we use.
We use shared configuration and deployment infrastructure so that we can achieve economies of scale in serving many communities, but with an entirely open-source stack that can be customized for their unique needs.

Usage Cost
:  2i2c passes cloud costs directly to the communities that we serve, and takes care to minimize this cost as much as possible.
  Because 2i2c's team has many years of experience running cloud infrastructure, we perform many optimizations that minimize the cloud expenses that you incur.
  Moreover, because we can run infrastructure that communities control as well, it is possible to use 2i2c hubs with cloud credits at your institution.

Person Cost
: 2i2c reduces its personnel costs by standardizing the configuration and deployment infrastructure across hubs for many communities. We aim to be significantly cheaper than hiring an in-house person or team to run infrastructure, but are slightly more expensive than a "fully-hosted Software as a Service" platform.

Right to Replicate
: All of 2i2c's infrastructure is entirely open-source and community-driven.
  We design our service with [the Right to Replicate](https://2i2c.org/right-to-replicate/) in mind from start to finish.

User portability
: 2i2c's managed hubs are designed to run on community standards in tools and workflows. We believe that the user's experience should mirror the best-practice in the open source community, and have as little 2i2c-specific workflows as possible.

OSS Support
: As a mission-driven organization, 2i2c has an obligation to support open source communities that it utilizes in its infrastructure. We design our workflow to do most of our improvements by making upstream contributions in open source projects.

Scalable
: 2i2c's infrastructure runs on JupyterHub, which can be scaled from 10s to 1000s of users. Moreover, we have experience running JupyterHub for high-performance data workflows via projects like Pangeo.

Customizable
: 2i2c's JupyterHubs give communities control over the user environments, interfaces, and general user workflows on our hubs. We aim for them to be as customizable as possible using technology in the Jupyter ecosystem.

Resilient
: 2i2c's JupyterHubs have a team of cloud experts operating, developing, and improving the infrastructure behind each hub. We also have a team with years of experience in research and education workflows to design these services in a sustainable and reliable manner.

Accessible
: 2i2c's JupyterHubs are run in partnership with the communities that use them, and commercial cloud infrastructure has very little restrictions on who can use it.
  Your infrastructure can be as open and accessible as you wish it to be.

Updates
: 2i2c's team follows the latest developments in Jupyter and cloud infrastructure, and continuously incorporates them into our managed hubs.

(compare:internal)=
### Internal staffing

The most common way for organizations to achieve similar services is to staff their own internal teams.
2i2c encourages this, as it is aligned with our commitment to open source, vendor-agnostic tools, and the [Right to Replicate your infrastructure](https://2i2c.org/right-to-replicate).

If your organization has significant pre-existing expertise in open source, Jupyter, and cloud infrastructure, then it may be more cost effective for you to run your own JupyterHub services.
If you need to build this expertise internally, it is likely much more cost-effective to partner with 2i2c.

Cloud Cost
:  Potentially optimal. Cloud costs depend heavily on the amount of optimization done to keep costs down. If you have an exceptional dev-ops team on-hand, then you may be able to reduce cloud costs, or use cloud credits, in a similar manner as 2i2c's services.
  Generally speaking, costs will be slightly higher without expertise in these areas.

Person Cost
: Very expensive. Hiring and retaining modern cloud engineers is difficult and costly.
  In 2022, [the median compensation of a Site Reliability Engineer](https://www.levels.fyi/t/software-engineer/title/site-reliability-engineer) is roughly `$180,000` a year, excluding indirect costs, training costs, recruiting costs, etc.
  Moreover, the efficiency of this role will depend heavily on the expertise of the person doing this work.

Right to Replicate
: Having an internal team run your infrastructure means that you are "already" replicating your own infrastructure, so this is not a concern.

User portability
: Having an internal team run your infrastructure means that you can design the user-workflows to be as portable as you wish.

OSS Support
: Depends on the organization.
  In practice, very few devops teams spend significant time contributing back to open source communities.

Scalable
: Depends on the experience of your internal team member, they may be able to scale your infrastructure to suit your community's needs.
  However, this requires a deeper understanding of the Jupyter and Dask ecosystem and how it interacts with cloud infrastructure.

Customizable
: Depends on the experience of your internal team member. They may be able to scale your infrastructure to suit your community's needs, though this requires a deeper understanding of the Jupyter ecosystem and how it interacts with cloud infrastructure.

Resilient
: Centralizing your organization’s cloud engineering on a single person creates risk associated with having a single point of failure.
  If a team of people is available, this is better, but comes with a significant increase in personnel costs.

Accessible
: With your own engineer, your infrastructure can be as accessible as you wish to be.

Updates
: 2i2c's team follows the latest developments in Jupyter and cloud infrastructure, and continuously incorporates them into our managed hubs.

:::{note}
2i2c primarily aims to be a more cost-effective alternative to this model of service delivery.
We constantly adjust our own prices and team compensation to be responsive to the ecosystem of Cloud and Site Reliability Engineering, and we'll update this information as the field evolves.
:::

(compare:public-infra)=
### Large-scale public infrastructure

Depending on the state or country that you live in, you may be able to access large-scale shared infrastructure that is run by government agencies.
For example, the [XSEDE](https://www.xsede.org/) program in the United States provides shared infrastructure that you can access with an application.

Often you will need to adapt your workflow to the infrastructure setup, rather than the other way around.
However, if you can find large-scale public infrastructure that accomplishes what you want, it may be a good option!

Cloud Cost
:  Your cloud costs will likely be quite low, as this infrastructure tends to be subsidized be government funds.
  However, it is also common for these services to charge cloud infrastructure directly to grants, in which case it is likely no different from managing your own cloud services or using 2i2c.

Person Cost
: Large-scale infrastructure efforts often come with significant complexity in bureaucratic process and steps that must be followed before you can get access.
  This complexity may come with significant personnel costs in interfacing with this centralized service, and building your own workflows around it.

Right to Replicate
: This depends heavily on the type of infrastructure you are using. Most public infrastructure is better than SaaS providers at using technology that is re-usable and community-driven, though the cloud infrastructure itself is often not designed with replication and community-ownership in mind.

User portability
: Most large-scale public infrastructure does not deviate much from the open source standards that others use.

OSS Support
: Highly-dependent on the organization.
  In practice, very few devops teams spend significant time contributing back to open source communities.

Scalable
: Depending on the experience of your internal team member, they may be able to scale your infrastructure to suit your community's needs.
  However, this requires a deeper understanding of the Jupyter and Dask ecosystem and how it interacts with cloud infrastructure.

Customizable
: Depending on the experience of your internal team member, they may be able to scale your infrastructure to suit your community's needs.
  However, this requires a deeper understanding of the Jupyter ecosystem and how it interacts with cloud infrastructure.

Resilient
: Centralizing your organization’s cloud engineering on a single person creates risk associated with having a single point of failure.
  If a team of people is available, this is better, but comes with a significant increase in personnel costs.

Accessible
: Using large-scale infrastructure like this often requires an application or vetting process before access can be provided, and is often restricted to only users that are within the same institution or country as the hub.

Updates
: There are more complex processes, bureaucracy, and constraints that manage the maintenance of large-scale infrastructure, and this means it tends to evolve and improve more slowly.

(compare:consulting)=
### Consulting companies

Many companies specialize in technical consulting that is flexible and tailored to an organization's needs.
They can build bespoke infrastructure using an open source stack that is similar to the one that 2i2c offers.
We also encourage this, as we believe in having a diverse ecosystem of vendors that can offer a similar vendor-neutral stack, as this may also encourage the [Right to Replicate your infrastructure](https://2i2c.org/right-to-replicate).
Examples of companies that do software consultancy in this space are [Anaconda](https://www.anaconda.com/), [KitWare](https://www.kitware.com/), [QuanSight](https://www.quansight.com/), and [QuantStack](https://quantstack.net/).

Usage cost
: Non-existent, assuming you are paying by the developer hour, rather than by the user.

Cloud Cost
: Dependent on the consultancy. If the consulting group has strong expertise in cloud infrastructure, jupyter infrastructure, and data workflows, then they may be able to optimize your cloud costs well. However this tends to come with higher hourly rates.

Person Cost
: These companies generally bill by the hour for their work, and have rates that vary between `$150/hr` and `$400/hr`.
It is difficult to assess the total number of hours needed to develop and operate a hub like the ones in this service, as it depends on the expertise of the organization.
If we assume 10 hours a month, this comes to between $1500 and $4000 a month.
A more conservative estimate for a team that does not specialize in JupyterHub and Kubernetes infrastructure might be 30 hours a month, or between $4,500 and $12,000 a month.

Right to Replicate
: You can generally direct these companies to deploy infrastructure in whatever manner you wish, and so may request that they provide infrastructure that gives you the right to replicate it.

User portability
: As long as you request that they only deploy standard infastructure and workflows for you, this is not a concern (though, it may cost extra if the company also offers their own company-specific service).

OSS Support
: Depends on the consultancy. Some organizations do a good job of providing upstream contributions to open source communities, and we recommend asking what kind of open source contribution process each follows.

Scalable
: Depends on the consultancy, and their expertise in cloud infrastructure.

Customizable
: Depends on the consultancy, and their expertise in cloud infrastructure.

Resilient
: Because consultancies generally charge by the hour, you can request more people to run the infrastructure in order to boost its resilience. However this generally comes with a significantly increased cost.

Accessible
: Depends on the consultancy, and their expertise in cloud infrastructure.

Updates
: Depends on the consultancy, and their expertise in cloud infrastructure.

(compare:saas)=
### Software as a Service Products

There are many companies offering services and platforms via a subscription fee.
The experience from a user's perspective may be similar and they may offer some open source tools as part of their services.
Examples of these products are [CoCalc](https://cocalc.com/), [Deepnote](https://deepnote.com/), [engageLively](https://engagelively.com/), [Colaboratory (Google)](https://colab.research.google.com/), [ObserveableHQ](https://observablehq.com/), [rstudio.cloud](https://rstudio.cloud/), [Sagemaker (AWS)](https://aws.amazon.com/sagemaker/), and [Saturn Cloud](https://saturncloud.io/).

Usage cost
: Generally charge betwee $7 and $50 per user, per month, depending on the complexity of the resources needed and the service. Many SaaS offerings include enterprise services as well, but their prices are generally not advertised publicly and are often significantly more expensive.

Cloud cost
: Cloud costs are generally wrapped up in usage-costs, though you will generally start paying extra costs if your usage reaches a certain limit.
  SaaS providers often bundle the cost of cloud in with a flat monthly price, and convert unused compute into extra revenue.

Person Cost
: Depends on the complexity of the service's interface and user experience, but generally this is significantly less-complex than running your own infrastructure (at the cost of openness, customizability, and the right to replicate).

Right to Replicate
: These platforms generally run on proprietary infrastructure or platforms, and do not give users the [Right to Replicate](https://2i2c.org/right-to-replicate) their infrastructure on their own.

User portability
: Most SaaS platforms use proprietary and service-specific interfaces and infrastructure. This means that users tend to learn service-specific skills and their workflows are not as portable to other services and tools.

OSS Support
: These platforms generally do not commit significant amounts of their resources to supporting collaborative open source communities. However, many of these services run on open source platforms that are controlled by the company offering the service.

Scalable
: Dependent on the platform, and whether scalability is built into their core offering. Often, scalable data workflows will come with a significant increase in usage cost.

Customizable
: Dependent on the platform, but generally more constrained than running on community-driven infrastructure, as SaaS providers tend to have more opinionated and proprietary interfaces and workflows.

Resilient
: Most SaaS providers are highly resilient, as they have teams of engineers managing a single shared service.

Accessible
: Not accessible. Most SaaS providers require each user to create their own account, or pay on their own, in order to have access.

Updates
: Dependent on the platform. Most SaaS providers do a reasonable job of staying up to date with modern data and cloud workflows, though they tend to include new features in the form of custom or proprietary workflows.
