# Set up your cloud account

(cloud-account:models)=
## Who owns the cloud account

There are two ways to set up the cloud account behind your hub:

**You own the cloud account (recommended).**
You establish the billing relationship with your preferred cloud vendor and grant 2i2c the access it needs to build and operate your infrastructure.
You pay the vendor directly, so your cloud costs are always visible to you.

**2i2c owns the cloud account.**
We deploy your infrastructure into a 2i2c-owned cloud account and pass the cloud costs through to you on our invoice, with no markup.
This adds reporting and administrative overhead for both of us, so we recommend bringing your own account when possible.

If you bring your own account, 2i2c needs access to it.
The rest of this page describes how to grant that access.

:::{admonition} 2i2c is not a cloud reseller

2i2c doesn't have a reseller relationship with any cloud provider.
For example, it does not have negotiated discounted pricing with either vendor.

:::

## Grant 2i2c access to your account

To build and manage your JupyterHub, 2i2c needs *full* access to a
cloud provider account on [Google Cloud Platform](https://cloud.google.com),
[Amazon Web Services](https://aws.amazon.com), or [Azure](https://azure.microsoft.com).

The sections below show how to do this for a few major platforms.
For any of them, we're happy to step you through the process: [contact 2i2c support](../../support.md) if you need help.

### Google Cloud Platform

#### Full billing account access

A GCP [billing account](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
is attached to a source of funds (Credit Card, Institutional account with invoicing,
credits provided by Google, etc). Giving 2i2c full access to a billing account
lets us manage everything except the funding mechanism. You can track costs,
get invoices, and grant overall access by controlling the billing account.

1. [Create a billing account](https://cloud.google.com/billing/docs/how-to/manage-billing-account#create_a_new_billing_account)
   This should be fairly straightforward with a credit card.

2. Give 2i2c [billing administrator](https://cloud.google.com/billing/docs/how-to/billing-access)
   permissions. You can do this by:

   1. Going to 'Account Management' on the left menu inside your billing account
      page.
   2. Click 'Show Info Panel' on the right. This should show a right sidebar that
      has list of current people with access to this billing account.
   3. Click 'Add Member'. This opens another right sidebar that lets you add /
      remove billing administrators.
   4. Select 'Billing -> Billing account administrator' as the role.

      ```{note}
      If you want 2i2c to not see anything about your payment method, select
      the following roles instead: 'Billing -> Billing Accounts Costs Manager',
      'Billing -> Billing Accounts User'. The full administrator role is
      preferred.
      ```
   5. [Contact 2i2c support](../../support.md) to request the email addresses of the
      2i2c engineering staff who will manage your project.
   6. Add those email addresses under 'New members'.
   7. Click 'Save'. This sends 2i2c staff an invitation to your billing account.

   The 2i2c team will confirm once they've accepted the invitation and can proceed with setup.

#### Project-level access

In some circumstances, you might already have access to a [GCP Project](https://cloud.google.com/storage/docs/projects),
rather than to a billing account. This is most common if you have a bigger
institutional entity managing your cloud access. 2i2c can work with just this
level of access too - although we will not have access to cost reports without
extra access grants.

1. Go to the [IAM Page](https://console.cloud.google.com/iam-admin/iam) for your
   project. You can manage access to your project, as well as to specific resources,
   here.

2. Click 'Add' in the top toolbar. A right side panel should open up

3. Select 'Projects -> Owner' as the role. This gives 2i2c full rights to
   everything inside the project.

4. [Contact 2i2c support](../../support.md) to request the email addresses of the
   2i2c engineering staff who will manage your project.

5. Add those email addresses under 'New members'.

6. Click 'Save'. This sends 2i2c staff an invitation to your project.

The 2i2c team will confirm once they've accepted the invitation and can proceed with setup.

### Amazon Web Services

We haven't written 2i2c-specific instructions for AWS yet.
Start with the AWS documentation to [create an account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) and [grant IAM access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html), then [contact 2i2c support](../../support.md) for the access our engineers need.

### Microsoft Azure

We haven't written 2i2c-specific instructions for Azure yet.
Start with the Azure documentation to [create a subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription) and [assign roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal), then [contact 2i2c support](../../support.md) for the access our engineers need.

### JetStream2 and CloudBank

Public providers like [JetStream2](https://docs.jetstream-cloud.org/getting-started/overview/) and [CloudBank](https://www.cloudbank.org/) grant access through allocations and grants rather than a billing account you create yourself.
They also restrict access to certain kinds of users and communities, so you'll need to double-check if you fit within their target user first.
Their processes vary, so [contact 2i2c support](../../support.md) and we'll advise on the right setup if you think you might be a good fit.
