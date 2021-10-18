# User authentication and access


## Authentication vs. Authorization

**Authentication** allows your users to prove who their are.
**Authorization** gives users certain permissions depending on their identity (such as "access to your hub", or "administrative privileges").

(admin/configuration/authentication)=
### Authentication

Users can prove who they are by logging in via an *authentication provider*. Currently, the following providers are supported:

1. *Google*. This includes public `@gmail.com` accounts, as well as [Google Workspace](https://workspace.google.com/) accounts set up for your workspace or university. If you use the GMail interface to access your work / university email, it can be used here.

2. [*GitHub*](https://github.com/). Extremely popular community of people creating, publishing and collaborating on code. Accounts are free, and many people already have them especially since the target community for most hubs are people who also write some kind of code.

3. Username / Password via [auth0](https://auth0.com/docs/connections/database).
   A traditional username / password interface where users can sign up. There are currently [limited
   options](https://github.com/2i2c-org/infrastructure/issues/421) for limiting who
   can sign up, so this should be only used in limited circumstances.

4. `<a different provider>`. We may be able to support other authentication providers, depending on your specific needs and the provider's complexity. Please reach out to us if none of these 3 work for your use-case.

We will ask you what provider you want when we set up the hub. We can change the provider after the fact, but only if absolutely necessary.

### Authorization

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
: Admin users are authorized [in a hub's YAML config](https://github.com/2i2c-org/infrastructure/blob/c1d06be1eed2d748a4d39e4cba76436cffe89fb2/config/hubs/2i2c.cluster.yaml#L50-L55), with support from 2i2c staff.

% TODO: Link to SRE docs on how to do this once we have it

## Manage users from the administrator panel

The **Administrator Panel** can be used to maintain the list of users
who are authorized to use your hub. You can access this panel by clicking
the 'Admin' button in the top bar in your hub control panel.
Alternatively, you can go to this URL in your browser:
`https://<your-hub-url>/hub/admin`

### To add users

1. Click the {guilabel}`Add Users` button. The {guilabel}`Add Users` dialog box will pop up.
2. Add one or more users, and hit the {guilabel}`Add Users` button to authorize all the users you just added.

`````{grid}
:class-container: full-width
:padding: 0 0 0 5

````{grid-item-card} 
:class-item: border-1
```{figure} ../../images/add-users-button.png
The {guilabel}`Add Users` button in the Administrator Panel.
```
````

````{grid-item-card} 
:class-item: border-1

```{figure} ../../images/add-users-form.png
Fill in usernames and optionally make them administrators. You can add multiple users at once by putting a username on each line.
```

````
`````


### Finding usernames

Access is granted or revoked based on `usernames`, and these depend on the kind
of (authentication provider)[admin/configuration/authentication] your hub is
using. In general, it matches whatever the visible 'username' in your
authentication provider is. The table below lists the available providers, and
how to determine their username.


| Provider | Username |
|-|-|
| Google | Email address |
| GitHub | GitHub user name |


% TODO: Document how to remove users
