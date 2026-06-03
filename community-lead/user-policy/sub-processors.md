# Sub-processors

A **sub-processor** is a third-party service that processes data on behalf of 2i2c while we operate infrastructure for a community.
This page describes the sub-processors used in a typical hub deployment and the kinds of personal data each one handles.
The specifics differ per hub (e.g., the cloud region where data is stored, or any add-on services), so the list below is not exhaustive.
See [](#data-processor:find) below to determine the list for a particular hub.

:::{admonition} This is not a legal document
:class: warning
This document is provided to set expectations and understanding about 2i2c's cloud infrastructure service.
It is not legally binding.
:::

## Typical sub-processors

The services below are common touchpoints for user data (e.g., their identity, files they create, etc).

### Cloud or infrastructure provider

An infrastructure provider (like a cloud provider) hosts the core infrastructure that runs the hub. This includes **compute**, **storage**, and **logging**.
The cloud region is configured per hub and determines where this data is stored.
2i2c either manages its own cloud provider account, or uses one managed by the community.

Personal data processed by this sub-processor:

- User home directory contents (e.g., notebooks, data files created during use)
- The JupyterHub username / authentication database
- System and access logs

Here are a few common cloud providers we use and their sub-processors pages:

- **Amazon Web Services (AWS)**. [GDPR Center](https://aws.amazon.com/compliance/gdpr-center/), [sub-processors](https://aws.amazon.com/compliance/sub-processors/)
- **Google Cloud Platform (GCP)**. [GDPR resource center](https://cloud.google.com/privacy/gdpr), [sub-processors](https://cloud.google.com/terms/subprocessors)
- **Microsoft Azure**. [Data Protection Addendum](https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA), [service trust page](https://servicetrust.microsoft.com)

### Identity provider

The service used to authenticate users when they log in.
The hub _uses_ these providers to authenticate but does not store authentication credentials on them. The user or their home institution has a direct relationship with the identity provider.

Personal data processed by this sub-processor (exchanged at login only):

- Username
- Email address (depending on the provider)
- Membership in a designated organization (where applicable)

Here are a few common ones we use:

- **GitHub**. [Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- **CILogon**. operated by the [University of Illinois NCSA](https://www.cilogon.org/about)
- **Google**. [Privacy & Terms](https://policies.google.com/privacy)

**Note**: If a hub uses CILogon, the user's home institution is itself the identity provider and effectively the relevant sub-processor for that user's authentication data.

(data-processor:find)=
## How to find the data processors for a specific hub

The sub-processors used by a given hub are determined by its configuration in the [2i2c infrastructure repository](https://github.com/2i2c-org/infrastructure/).
This will usually involve digging through `.yaml` configuration to find the services that your hub uses.
If you need this information, please [open a support ticket](../../support.md).

## Related

- [](./privacy.md). what data 2i2c does and does not retain
- [](./acceptable-use.md). expectations for using 2i2c-managed infrastructure
