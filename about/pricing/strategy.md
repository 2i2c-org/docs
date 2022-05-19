# Pricing strategy and rationale

This page describes the rationale and strategy behind our pricing.

We invite comments and feedback about the attractiveness and sustainability of these services, and expect to update this model with feedback from the community as we learn more.

```{list-table}
:widths: auto
:stub-columns: 1

- - Last Updated
  - 2022-05-06
- - Next checkpoint
  - 2022-08
```

## Guiding principles of our prices

The following principles guide our decision-making around pricing our services.
We believe that following these principles allows us to deliver the best services for our communities in a way that aligns with our mission and values.
Our prices should:

- Sustain and grow 2i2c's services and allow it to thrive as an organization.
- Support the extra cost associated with open source contributions.
- Reflect a holistic understanding of open source support, not just code.
- Be competitive with other "Data Science environment as a service" offerings (see below for how we consider ourselves relative to similar offerings).
- Be sustainable for the communities we serve, with mechanisms to accommodate institutions with fewer resources.


## Pricing structure

Currently, we base our pricing on two major items:

### Flat monthly fees

We charge a flat monthly fee to cover [our personnel costs](costs/people.md).
We estimate the number of hubs an engineer can run, and use this to estimate our costs per hub after adding in project management and administration costs.

Most hubs take extra effort during the _set up_ phase, and relatively less effort to maintain over time (depending on how many change requests a community makes).
As such we suspect that this pricing structure does not cover our costs in the first month or two, but regains those costs in subsequent months.

In the future we may try to perform a more nuanced mapping of costs onto effort from our team, but for now we wish to keep things simple and predictable while we learn more.

### Pass-through cloud costs

In addition to our monthly hub fees, we pass cloud costs [directly to the communities we serve](costs/cloud.md), without taking any percentage markup.
We do this for two reasons:

1. In our eyes, we are running infrastructure _on behalf of each community_, and wish to act as if a member of that community were running the infrastructure themselves. We are simply being compensated for our time and expertise.
2. Adding a percentage markup on cloud costs may create perverse incentives for us to avoid optimizing down a community's cloud costs.

For these reasons, we are currently [passing through cloud costs directly to communities](costs/cloud.md).

## Base fees for three service types

These are based on major use-cases in the communities we have served.

- **Educational communities** need basic hubs that are reliable, secure, and that serve a community of users. They tend to charge course fees and can recoup some costs this way. Assume 22 educational hubs per engineer.
- **Research communities** need a bit more power and complexity, and potentially access to more cloud infrastructure and data. They tend to have grant funding for fixed periods of time that is enough to cover an internal FTE. Assume 13 research hubs per engineer.
- **Partnerships** happen with more advanced / well-resourced communities that want more bespoke infrastructure and new development, and we want a service option that allows for this flexibility. It takes significant extra effort to define and carry out these more complex relationships, and we should only engage in them if they cover a larger percentage of our costs. We'll use a lower-bound of 20% FTE per engineer for these engagements (ie, at-most 5 partnership-level engagements per engineer), though we suspect most will require more FTE time than this.

Below is a table which summarizes these major points

% Generated with https://www.tablesgenerator.com/markdown_tables

| Type of service | Annual cost / engineer | N hubs max / engineer | Avg Annual Cost per service | Avg Monthly Cost per service |
|:---------------:|:----------------------:|:---------------------:|:---------------------------:|:----------------------------:|
|    Education    |       $250,000.00      |           22          |          $12,000.00         |           $1,000.00          |
|     Research    |       $250,000.00      |           14          |          $18,000.00         |           $1,500.00          |
|   Partnership   |       $250,000.00      |           5           |          >=$50,000.00        |           $4,166.67          |

### Markup for running on dedicated clusters

In general we want our fees to scale with the amount of complexity that we have to manage. If we run JupyterHubs on community-specific cloud infrastructure, we have more responsibility and moving parts to keep track of. For example, we’ll need to manage credentials for cloud accounts, set up infrastructure that connects with those accounts, and manage a dedicated kubernetes cluster for the community. We’ll also need to provide billing reports per-cluster for cloud costs. All of this is extra complexity we must deal with, and so a 50% markup is a conservative estimate to cover this labor.

## What we are missing

We know that there are some communities that will not be well-served by the options described above. Our goal during the alpha is to build sustainability in order to meet these communities in the future. If the model described above doesn’t fit your needs well (e.g., wrong kind of service, too expensive, etc) please provide feedback, as this can help us evolve the service over time.

Below are a few things that we know we are missing:

- **Under-resourced communities**. For many communities, $12,000 a year is too much cost to justify. Our mission requires that we serve these communities as well, not just the ones with larger budgets. This proposal is a step towards sustainability, with the goal of developing new models that can serve under-resourced organizations as well. A few ideas to explore are sponsorship models, tiered pricing models that adjust price based on a community’s budget size, and reducing our internal costs (and thus the fees for our services).
- **Lightweight hubs**. For many individuals or communities, these offerings might involve more complexity than what they need. We’d like to offer a much more scalable and lightweight hub service that people could quickly spin up. We hope to prototype and experiment with ideas after the initial roll-out of the alpha service.
- **Communities that need multiple hubs**. For organizations with many sub-communities and complexity, a single hub is likely not enough to meet their needs. These communities may be better-served by their own dedicated federation of hubs, with a different pricing / growth model than the offerings described here. For now we’ll treat these as partnership opportunities, but may wish to standardize this in a service offering in the future.
- **Significant differences in community size**. Our pricing model assumes that most communities have a relatively similar degree of complexity and size between them. However, when communities grow to a certain size (say, two orders of magnitude), it generates additional work in supporting users and hub operations. We hope to better-understand the costs associated with serving these larger communities, and identify ways to recover them via our pricing.
- **Cloud payments as a service**. In some cases we manage the billing infrastructure and payments for communities (as opposed to them paying cloud providers directly). We do not currently charge explicitly for performing this service. In this case we take on extra work and complexity in tracking and paying cloud bills. We should estimate how much work and risk/liability is entailed in this, and work with our fiscal sponsor to understand how to cover these costs.
- **Liability for cloud payments**. For communities where we manage their cloud billing, we hold some liability because we’ll need to pay the cloud provider for their usage before they pay us. We should work with our fiscal sponsor to understand our risk here (for example, what if a community charges $50,000 in cloud costs and then refuses to pay their invoice). We should also explore potential ways to mitigate this risk (for example, pre-billing communities for *estimated* cloud usage to create a buffer, or asking for a deposit.
