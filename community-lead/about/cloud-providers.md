# Cloud providers

2i2c can deploy community hubs on several cloud platforms, giving communities flexibility in where their infrastructure runs.
In practice, cloud provider choices are also shaped by your [membership model](https://2i2c.org/membership), support expectations, and the operational complexity of your hub. See [2i2c's platform](https://2i2c.org/platform) for a service overview.

## Commercial cloud providers

We support several major international commercial cloud providers and can deploy a hub into most datacenters (or "regions") for each.

### Amazon Web Services (AWS)

[Amazon Web Services](https://aws.amazon.com/) is one of the largest and most widely-used cloud platforms globally, offering extensive infrastructure in regions worldwide.

### Google Cloud Platform (GCP)

[Google Cloud](https://cloud.google.com/) provides robust cloud infrastructure with strong integration with Google's ecosystem and data science tools.

### Microsoft Azure

[Microsoft Azure](https://azure.microsoft.com/en-us/) is Microsoft's cloud platform with broad enterprise adoption.

:::{note}
Azure deployments may incur an additional cost due to the extra complexity of deploying and managing hubs on this platform.
:::

## Public and governmental cloud providers

These cloud providers are managed by federal teams and resources. Access to them may be dependent on the community or specific grants or awards.

### JetStream2

[JetStream2](https://jetstream-cloud.org/) adds cloud-based, on-demand computing and data analysis resources to the national cyberinfrastructure. It is managed by the [Pervasive Technology Institute at Indiana University](https://pti.iu.edu/).

To see if your community is eligible for a JetStream2 hub, see [the JetStream2 getting started guide](https://docs.jetstream-cloud.org/getting-started/overview/).

For example, 2i2c deployed a [BinderHub](https://binderhub.readthedocs.io/) instance on JetStream2 for [Project Pythia](https://projectpythia.org/).

### NSF CloudBank

[CloudBank](https://www.cloudbank.org/) is an NSF-supported service that helps researchers and educators access commercial cloud resources.
2i2c runs hubs on CloudBank in collaboration with UC Berkeley, the University of Washington, and the San Diego Supercomputer Center (SDSC).

### National Research Platform

2i2c does not currently deploy hubs on the [National Research Platform](https://nationalresearchplatform.org/), though it is an item we are exploring on [our roadmap](https://2i2c.org/roadmap).
[Contact 2i2c support](../../support.md) if this is something you're interested in funding or supporting.

## On-premises deployments

2i2c does not currently operate any on-premises infrastructure, though our team has experience with on-premises deployments and are interested in learning about your use-case.
If you'd like to discuss an on-premises option, [contact 2i2c support](../../support.md).

## How to choose a cloud provider

The choice of cloud provider depends on several factors:

- **Data location requirements**: Some communities need data to remain in specific geographic regions for compliance or performance reasons.
- **Existing infrastructure**: Communities may want to deploy on the same provider where they already have data or resources.
- **Cost and funding**: Different providers have different pricing models, and some communities may have credits or grants for specific providers.
- **Access and eligibility**: Public cloud providers like JetStream2 may have specific eligibility requirements.

If you're unsure which provider is right for your community, contact 2i2c support to discuss your needs.
