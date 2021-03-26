# Provision a paid cloud provider account for 2i2c

For 2i2c to build & manage your JupyterHub, it needs *full* access to a
cloud provider account on [Google Cloud Platform](https://cloudn.google.com),
[Amazon Web Services][https://aws.amazon.com], or [Azure](https://azure.microsoft.com).
This page will provide guidance on how to do that.

## Google Cloud Platform

Currently, Google Cloud Platform (GCP) is 2i2c's preferred cloud provider. 2i2c
access can be set up in a couple different ways.

### Full billing account access

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
   5. Enter the following user emails under 'New members': `yuvipanda@2i2c.org`,
      `choldgraf@2i2c.org`. These are two of the folks at 2i2c who will
      help manage your project.
   6. Click 'Save'. This sends 2i2c staff an invitation to your billing account.
   
   Let 2i2c staff know once you've completed this process, and they should be
   able to get going!
   
### Project-level access

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
   
4. Enter the following user emails under 'New members': `yuvipanda@2i2c.org`,
    `choldgraf@2i2c.org`. These are two of the folks at 2i2c who will
    help manage your project.

5. Click 'Save'. This sends 2i2c staff an invitation to your billing account.

Let 2i2c staff know once you've completed this process, and they should be
able to get going!
