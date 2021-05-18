# User authentication & authorization

**Authentication** allows your users to prove who their are.
**Authorization** gives users certain permissions depending on their identity (such as "access to your hub", or "administrative privileges").

(admin/configuration/authentication)=
## Authentication

Users can prove who they are by logging in via an *authentication provider*. Currently, the following providers are supported:

1. *Google*. This includes public `@gmail.com` accounts, as well as [Google Workspace](https://workspace.google.com/) accounts set up for your workspace or university. If you use the GMail interface to access your work / university email, it can be used here.

2. [*GitHub*](https://github.com/). Extremely popular community of people creating, publishing and collaborating on code. Accounts are free, and many people already have them especially since the target community for most hubs are people who also write some kind of code.

3. [*ORCID*](https://orcid.org/). Everyone who has published a paper has one of these, and anyone else can easily sign up. Almost exclusively used by researchers.

4. Username / Password via [auth0](https://auth0.com/docs/connections/database).
   A traditional username / password interface where users can sign up. There are currently [limited
   options](https://github.com/2i2c-org/pilot-hubs/issues/421) for limiting who
   can sign up, so this should be only used in limited circumstances.

5. `<a different provider>`. We may be able to support other authentication providers, depending on your specific needs and the provider's complexity. Please reach out to us if none of these 3 work.

We will ask you what provider you want when we set up the hub. We can change the provider after the fact, but only if absolutely necessary.

## Authorization

Not everyone who can authenticate is granted access to the hub - that would mean
everyone with a `@gmail.com` account can log in if you use Google as your
authentication provider! Instead, we support multiple ways for hub admins to
specify which users are *authorized* to be on the hub.

Authorizing regular users
: Currently, there are only two supported methods for authorizing regular users:

  1. [Manually add users](../howto/manage-users.md) via the admin panel in JupyterHub
  2. (Google only) Allow all users who are logged in via a particular domain - so
     you can allow access to anyone who is part of your organization or
     educational institution.

Authorizing admin users
: Admin users are authorized [in a hub's YAML config](https://github.com/2i2c-org/pilot-hubs/blob/master/hubs.yaml), with support from 2i2c staff.

% TODO: Link to SRE docs on how to do this once we have it
