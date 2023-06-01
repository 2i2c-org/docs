# User authentication and access

## Authentication vs. Authorization

- **Authentication** allows your users to prove who their are.
- **Authorization** gives users certain permissions depending on their identity (such as "access to your hub", or "administrative privileges").

(admin/configuration/authentication)=
### Authentication

Users can prove who they are by logging in via an *authentication provider*. Currently, the following providers are supported:

1. *Google*. This includes public `@gmail.com` accounts, as well as [Google Workspace](https://workspace.google.com/) accounts set up for your workspace or university. If you use the GMail interface to access your work / university email, it can be used here.

2. [*GitHub*](https://github.com/). Extremely popular community of people creating, publishing and collaborating on code. Accounts are free, and many people already have them especially since the target community for most hubs are people who also write some kind of code. We can setup GitHub authentication so you can either manage a list of specific GitHub handles in the [JupyterHub admin panel](admin/management/admin-panel), or so that members of a specific GitHub organisation or team are automatically authorised to use the hub.

3. `<a different provider>`. We may be able to support other authentication providers, depending on your specific needs and the provider's complexity. Please reach out to us if none of those above work for your use-case.

We will ask you what provider you want when we set up the hub. We can change the provider after the fact, but only if absolutely necessary.

### Authorization

Not everyone who can authenticate is granted access to the hub - that would mean
everyone with a `@gmail.com` account can log in if you use Google as your
authentication provider! Instead, we support multiple ways for hub admins to
specify which users are *authorized* to be on the hub.

Authorizing regular users
: Currently, there are only three supported methods for authorizing regular users:

  1. [Manually add users](../howto/manage-users.md) via the admin panel in JupyterHub
  2. (Google only) Allow all users who are logged in via a particular domain - so
     you can allow access to anyone who is part of your organization or
     educational institution.
  3. (GitHub only) Allow all users who are members of a specific organisation or
     team. This approach gives you fine-grained control over who has access to the
     hub inline with your access policies on GitHub

```{tip}
If your hub has a range of different machine sizes or environments to choose from,
we can also configure which users can see which options based on their GitHub team
membership! For example, a team like `@MyCoolOrg/all-users` might be able to see
Small and Medium sized machines, but the `@MyCoolOrg/advanced-users` team can additionally
have access to the Large and GPU machines. You can manage these teams within GitHub.

Speak to a Hub Engineer about enabling this feature for your hub.
```

Authorizing admin users
: Admin users are authorized [in a hub's YAML config](https://github.com/2i2c-org/infrastructure/blob/c1d06be1eed2d748a4d39e4cba76436cffe89fb2/config/hubs/2i2c.cluster.yaml#L50-L55), with support from 2i2c staff.

% TODO: Link to SRE docs on how to do this once we have it

(admin/management/admin-panel)=
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


### Remove users from a hub

You can revoke a user's access to the JupyterHub by removing them from the allowed users list, using the admin panel.

1. Find the name of the user in your admin panel. If they have a running server,
   click the {guilabel}`Stop server` button to stop their running server.
2. Click the {guilabel}`Delete user` button for this user. Confirm the deletion in
   the dialog box that pops up.

After this, the user would not be able to log in. However, their files will not be deleted -
if you add them later, their files will still be present.

### Finding usernames

Access is granted or revoked based on `usernames`, and these depend on the kind
of [authentication provider](admin/configuration/authentication) your hub is
using. In general, it matches whatever the visible 'username' in your
authentication provider is. The table below lists the available providers, and
how to determine their username.


| Provider | Username |
|-|-|
| Google | Email address |
| GitHub | GitHub user name |


% TODO: Document how to remove users

## Debug user authentication issues

If users are running into strange errors when they log in (for example CILogon error pages that say "Looks like something went wrong!"), ask them to try these steps in debugging:

1. Try logging in with an `incognito` window. This will help determine if their issue is due to some cookie / cache that is stored on their machine.
2. Ask them to clear their cookies / cache for all CILogon websites. For example, [here are the Google Chrome instructions to clear cookies](https://support.google.com/chrome/answer/95647?hl=en&co=GENIE.Platform%3DDesktop).
3. If using `CILogon`, double-check that they've signed in with the correct account, and [ask them to switch accounts if needed](https://infrastructure.2i2c.org/en/latest/howto/configure/auth-management.html#switch-identity-providers-or-user-accounts).
