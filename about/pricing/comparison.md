# Comparison to similar services

This page is a guide to 2i2c's services, our pricing, and how this compares with similar kinds of offerings.

:::{tip}
The content on this page can be re-used as a part of "price reasonableness and comparisons" forms when completing contracting for communities.

In each section below, we'll list a few similar companies and services that can be compared with 2i2c.
Their presence and ordering do not constitute an "endorsement" and are not exhaustive - we are merely trying to be transparent and helpful about the other organizations in this space.
:::

There are a few major categories to consider, and we'll provide a brief description of each below.

- **Cloud cost**: How much does the infrastructure itself cost?
- **Person cost**: How much time does it take to maintain, and how much does that time cost?
- **Right to replicate**: Does the infrastructure run in a way that you could replicate the end-service nearly identically on your own?
- **OSS Support**: Does this service reliably drive resources and support to open source communities that underlie the service?
- **Scalable**: How complex is it to scale this option to many users, high-performance infrastructure, or big data?
- **Customizable**: How much control do you have over the experience that your users have? Can you control the environment, interface, etc?
- **Resilient**: Is this option vulnerable to bottlenecks in individual skills and capacity, or is it fault-tolerant and sustained by a group?

Below is a short table summarizing the information below along a few major dimensions.
It makes some simplifications and assumptions, and is meant to be a quick and "glanceable" way to compare the options below:

::::{grid} 3
:margin: 1

:::{grid-item}
✅ = yes / easy
:::
:::{grid-item}
🟧 = sometimes / possible
:::
:::{grid-item}
❌ = rarely / difficult
:::
::::

:::{list-table}
:widths: 15 10 10 5 5 5 5 5
:class: align-middle
:stub-columns: 1
:header-rows: 1

- - Service
  - Cloud Cost
  - Person Cost
  - Right to Replicate
  - OSS Support
  - Scalable
  - Customizable
  - Resilient
- - [2i2c](compare:2i2c)
  - 💲💲
  - 💲💲
  - ✅
  - ✅
  - ✅
  - ✅
  - ✅
- - [Internal Staffing](compare:internal)
  - 💲💲💲
  - 💲💲💲💲
  - 🟧
  - 🟧
  - ❌
  - ✅
  - ❌
- - [National infrastructure](compare:public-infra)
  - 💲💲
  - 💲💲💲
  - 🟧
  - 🟧
  - 🟧
  - 🟧
  - 🟧
- - [Consultancy](compare:consulting)
  - 💲💲
  - 💲💲💲
  - 🟧
  - 🟧
  - ❌
  - ✅
  - 🟧
- - [SaaS Products](compare:saas)
  - 💲💲💲
  - 💲
  - ❌
  - 🟧
  - ✅
  - ❌
  - ✅
:::

(compare:2i2c)=
## How to think about 2i2c's service and pricing

As a non-profit, we choose our prices to move forward on a sustainable path to achieve our mission according to [our cost model](costs:human) as well as [our growth model](strategy:growth).
Our service entails developing and managing entirely open-source, vendor-agnostic, and community-driven infrastructure that is customized for research and education.

Our aim with 2i2c's service model is to strike a balance between **scalability** and **flexibility**, with the constraints that we operate **transparently** and **collaboratively** with our communities, by runing **open-source** and **community-driven** infrastructure.

We curate and integrate this infrastructure, customize it for use-cases in research and education, and contribute back to the open source communities that underlie the tools we use.
We use shared configuration and deployment infrastructure so that we can achieve economies of scale in serving many communities, but with an entirely open-source stack that can be customized for their unique needs.

We do not know of any other organizations that offer managed cloud services in this way.
However, below are a few similar kinds of service and product models.
They are roughly ordered from "most similar" to "least similar" to 2i2c.

(compare:internal)=
## Internal staffing

The most common way for organizations to achieve similar services is to staff their own internal teams.
2i2c encourages this, as it is aligned with our commitment to open source, vendor-agnostic tools, and the [Right to Replicate your infrastructure](https://2i2c.org/right-to-replicate).

However, hiring and retaining modern cloud engineers is difficult and costly.
In 2022, [the median compensation of a Site Reliability Engineer](https://www.levels.fyi/Salaries/Software-Engineer/Site-Reliability/) is roughly `$180,000` a year, excluding indirect costs.

This under-estimates the true cost, as there are a few other risk factors associated with paying a single engineer to manage your cloud infrastructure:

- Attracting and hiring people for this very in-demand position requires a significant amount of time and energy.
- Centralizing your organization’s cloud engineering on a single person creates risk associated with having a single point of failure.
- The efficiency of this role will depend heavily on their previous expertise with cloud infrastructure and Jupyter, and their capacity to make improvements to the open source tooling will be difficult unless they have previous experience in this ecosystem.
- As a sole contributor, they will likely not be as responsive to outages, make improvements, or incorporate enhancement and security fixes as quickly as a distributed team of experts.

If your organization has significant pre-existing expertise in open source, Jupyter, and cloud infrastructure, then it may be more cost effective for you to run your own JupyterHub services.
If you need to build this expertise internally, it is likely much more cost-effective to partner with 2i2c.

:::{note}
2i2c primarily aims to be a more cost-effective alternative to this model of service delivery.
We constantly adjust our own prices and team compensation to be responsive to the ecosystem of Cloud and Site Reliability Engineering, and we'll update this information as the field evolves.
:::

(compare:public-infra)=
## Large-scale public infrastructure

Depending on the state or country that you live in, there may also be options available to get access to large-scale shared infrastructure that is run by government agencies.
For example, the [XSEDE](https://www.xsede.org/) program in the United States provides shared infrastructure that you can access with an application.

The biggest challenges to using these larger infrastructure services tend to be inflexibility and friction associated with gaining access, sharing access, and customizing to your needs. Large-scale infrastructure efforts often come with significant complexity in bureaucratic process and steps that must be followed before you can get access.
This is particularly difficult if you wish to collaborate across institutions, or want to easily provide access to newcomers.
Moreover, the infrastructure tends to evolve more slowly, and is less dynamic in user interactions, than modern cloud-based infrastructure.
Often you will need to adapt your workflow to the infrastructure setup, rather than the other way around.
However, if you can find large-scale public infrastructure that accomplishes what you want, it may be a good option!

(compare:consulting)=
## Consulting companies

Many companies specialize in technical consulting that is flexible and tailored to an organization's needs.
They can build bespoke infrastructure using an open source stack that is similar to the one that 2i2c offers.
We also encourage this, as we believe in having a diverse ecosystem of vendors that can offer a similar vendor-neutral stack, as this may also encourage the [Right to Replicate your infrastructure](https://2i2c.org/right-to-replicate).
Examples of companies that do software consultancy in this space are [Anaconda](https://www.anaconda.com/), [QuanSight](https://www.quansight.com/), and [QuantStack](https://quantstack.net/).

These companies generally bill by the hour for their work, and have rates that vary between `$150/hr` and `$400/hr`.
It is difficult to assess the total number of hours needed to develop and operate a hub like the ones in this service, as it depends on the expertise of the organization.
If we assume 10 hours a month, this comes to between $1500 and $4000 a month.
A more conservative estimate for a team that does not specialize in JupyterHub and Kubernetes infrastructure might be 30 hours a month, or between $4,500 and $12,000 a month.

(compare:saas)=
## Software as a Service Products

There are many companies offering services and platforms via a subscription fee.
These platforms generally run on proprietary infrastructure or platforms, and do not give users the [Right to Replicate](https://2i2c.org/right-to-replicate) their infrastructure on their own.
The experience from a user's perspective may be similar and they may offer some open source tools as part of their services.
Examples of these products are [CoCalc](https://cocalc.com/), [Deepnote](https://deepnote.com/), [engageLively](https://engagelively.com/), [Colaboratory (Google)](https://colab.research.google.com/), [Noteable](https://noteable.io/), [ObserveableHQ](https://observablehq.com/), [rstudio.cloud](https://rstudio.cloud/), [Sagemaker (AWS)](https://aws.amazon.com/sagemaker/), and [Saturn Cloud](https://saturncloud.io/).

These models are generally priced in one of two ways:

- **By the user**. Introductory levels of SaaS services tend to charge by the user, at a rate that scales with the complexity and power of the service being used. This might range between $12 and $100 per user per month for basic data science environments. It can be in the hundreds or thousands per user per month for particularly complex enterprise environments.
- **As a markup on cloud usage**. Another approach is to charge a percentage markup on cloud costs. For example, a 75% surcharge is added to each monthly cloud bill. This amount depends heavily on your total cloud bill, and is particularly affected if you run lots of scalable or long-running computations.

Enterprise-level contracts for these platforms can be significantly more expensive than this, but prices are generally not displayed publicly and vary by the organization.

## Bottom line

There is a large ecosystem of vendors and services available for interactive data science.
2i2c believes that interactive computing is emerging as the vital medium for communications in research and education communities. As a result, we suggest that universities and research communities should build atop non-proprietary tools and commit to services that are vendor-agnostic and respect your [Right to Replicate your infrastructure](https://2i2c.org/right-to-replicate).
You should think about the constraints and principles that you'd like your infrastructure to follow, and choose the right approach for your organization.
