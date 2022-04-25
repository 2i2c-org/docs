# Pricing strategy and rationale

This page describes the rationale and strategy behind our pricing.

We invite comments and feedback about the attractiveness and sustainability of these services, and expect to update this model with feedback from the community as we learn more.

## Guiding principles of our prices

The following principles guide our decision-making around pricing our services.
Our prices should:

- Sustain and grow 2i2c's services and allow it to thrive as an organization.
- Support the extra cost associated with open source contributions.
- Reflect a holistic understanding of open source support, not just code.
- Be competitive with other "Data Science environment as a service" offerings (see below for how we consider ourselves relative to similar offerings).
- Be sustainable for the communities we serve, with mechanisms to accommodate institutions with fewer resources.

## Base fees for three service types

These are based on major use-cases in the communities we have served.

- **Educational communities** need basic hubs that are reliable, secure, and that serve a community of users. They tend to charge course fees and can recoup some costs this way. Assume 22 educational hubs per engineer.
- **Research communities** need a bit more power and complexity, and potentially access to more cloud infrastructure and data. They tend to have grant funding for fixed periods of time that is enough to cover an internal FTE. Assume 13 research hubs per engineer.
- **Partnerships** happen with more advanced / well-resourced communities that want more bespoke infrastructure and new development, and we want a service option that allows for this flexibility. This pricing is bespoke, but we should assume around 5 partnerships per engineer for these engagements.

Below is a table which summarizes these major points

% Generated with https://www.tablesgenerator.com/markdown_tables

| Type of service | Annual cost / engineer | N hubs max / engineer | Avg Annual Cost per service | Avg Monthly Cost per service |
|:---------------:|:----------------------:|:---------------------:|:---------------------------:|:----------------------------:|
|    Education    |       $250,000.00      |           22          |          $12,000.00         |           $1,000.00          |
|     Research    |       $250,000.00      |           14          |          $18,000.00         |           $1,500.00          |
|   Partnership   |       $250,000.00      |           5           |          $50,000.00         |           $4,166.67          |

### Markup for running on dedicated clusters

In general we want our fees to scale with the amount of complexity that we have to manage. If we run JupyterHubs on community-specific cloud infrastructure, we have more responsibility and moving parts to keep track of. For example, we’ll need to manage credentials for their cloud accounts, set up infrastructure that connects with those accounts, and manage a dedicated kubernetes cluster for them. We’ll also need to provide billing reports per-cluster for cloud costs. All of this is extra complexity we must deal with, and so a 50% markup is a conservative estimate to cover this labor.

## What we are missing

We know that there are some communities that will not be well-served by the options described above. Our goal during the alpha is to build sustainability in order to meet these communities in the future. If the model described above doesn’t fit your needs well (e.g., wrong kind of service, too expensive, etc) please provide feedback, as this can help us evolve the service over time.

Below are a few things that we know we are missing:

- **Under-resourced communities**. For many communities, $12,000 a year is too much cost to justify. Our mission requires that we serve these communities as well, not just the ones with larger budgets. This proposal is a step towards sustainability, with the goal of developing new models that can serve under-resourced organizations as well. A few ideas to explore are sponsorship models, tiered pricing models that adjust price based on a community’s budget size, and reducing our internal costs (and thus the fees for our services).
- **Lightweight hubs**. For many individuals or communities, these offerings might involve more complexity than what they need. We’d like to offer a much more scalable and lightweight hub service that people could quickly spin up. We hope to prototype and experiment with ideas after the initial roll-out of the alpha service.
- **Communities that need multiple hubs**. For organizations with many sub-communities and complexity, a single hub is likely not enough to meet their needs. These communities may be better-served by their own dedicated federation of hubs, with a different pricing / growth model than the offerings described here. For now we’ll treat these as partnership opportunities, but may wish to standardize this in a service offering in the future.
- **Significant differences in community size**. Our pricing model assumes that most communities have a relatively similar degree of complexity and size between them. However, when communities grow to a certain size (say, two orders of magnitude), it generates additional work in supporting users and hub operations. We hope to better-understand the costs associated with serving these larger communities, and identify ways to recover them via our pricing.
- **Billing as a service**. In some cases we are managing the billing infrastructure and payments for communities. However, we do not currently charge explicitly for performing this service. We should estimate how much work and liability is entailed in this, and work with our fiscal sponsor to understand if and how much we should charge to cover these costs.
- **Liability for cloud billing**. For communities where we manage their cloud billing, we hold some liability because we’ll need to pay the cloud provider for their usage before they pay us. We should work with our fiscal sponsor to understand our risk here (for example, what if a community charges $50,000 in cloud costs and then refuses to pay their invoice). We should also explore potential ways to mitigate this risk (for example, pre-billing communities for *estimated* cloud usage to create a buffer, or asking for a deposit.
