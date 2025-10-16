# User authentication and access

## Authentication vs. Authorization

- **Authentication** allows your users to prove who their are.
- **Authorization** gives users certain permissions depending on their identity (such as "access to your hub", or "administrative privileges").

(admin/configuration/authentication)=
## Authentication providers

Users can prove who they are by logging in via an *authentication provider*. Currently, the following providers are supported:

### [CILogon](https://www.cilogon.org/)

An extremely popular provider for various institutional logins, Google accounts (including @gmail.com accounts), Microsoft accounts, etc. This is our **primary** authentication provider.
It can support allowing users from multiple institutions to login as well, which is very helpful.
2i2c can manage CILogon using the JupyterHub CILogonOAuthenticator.

Some key terms about CILogon authentication worth mentioning:

`Identity Provider`
: The authentication service available through the CILogon connection.

  When a user logs in via CILogon, they are first presented with a list of various institutions and organizations that they may choose from (`Australia National University`, `UC Berkeley`, etc.).

  The available identity providers are members of [InCommon](https://www.incommon.org/federation/), a federation of universities and other organizations that provide single sign-on access to various resources.

  ```{note}
  Check if a community's login provider is available on CILogon, by going to https://cilogon.org/idplist and filter after its name.
  ```

`User account`
: Within an institution, each user is expected to have their own user account (e.g. `myname@berkeley.edu`). This is the account that is used to give somebody an ID on their JupyterHub. This is entered on an Identity Provider's login screen.

### [GitHub](https://github.com/)
Extremely popular community of people creating, publishing and collaborating on code. Accounts are free, and many people already have them especially since the target community for most hubs are people who also write some kind of code. We can setup GitHub authentication so you can either manage a list of specific GitHub handles in the [JupyterHub admin panel](admin/management/admin-panel), or so that members of a specific GitHub organisation or team are automatically authorised to use the hub.

### `<a different provider>`
We may be able to support other authentication providers, depending on your specific needs and the provider's complexity. However, this should be used as a last resort and will come with an increase in management cost, to offset the extra engineering complexity. Please reach out to us if none of those above work for your use-case.

We will ask you what provider you want when we set up the hub. We can change the provider after the fact, but only if absolutely necessary.

## Add a new user (Authorization)

Not everyone who can authenticate is granted access to the hub - that would mean
everyone with a `@gmail.com` account can log in if you use Google as your
authentication provider! Instead, we support multiple ways for hub admins to
specify which users are *authorized* to be on the hub.

Authorizing regular users
: Currently, there are only three supported methods for authorizing regular users:

  1. {ref}`Manually add users<admin/management/admin-panel>` via the admin panel in JupyterHub
  2. (CILogon only) Allow all users who are logged in via a particular domain - so
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
### Manually manage users from the administrator panel

The **Administrator Panel** can be used to maintain the list of users
who are authorized to use your hub. You can access this panel by clicking
the 'Admin' button in the top bar in your hub control panel.
Alternatively, you can go to this URL in your browser:
`https://<your-hub-url>/hub/admin`

#### To add users

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

#### Remove users from a hub

You can revoke a user's access to the JupyterHub by removing them from the allowed users list, using the admin panel.

1. Find the name of the user in your admin panel. If they have a running server,
   click the {guilabel}`Stop server` button to stop their running server.
2. Click the {guilabel}`Delete user` button for this user. Confirm the deletion in
   the dialog box that pops up.

After this, the user would not be able to log in. However, their files will not be deleted -
if you add them later, their files will still be present.

### GitHub Organizations and Teams

Hub admins can control access to their hub by adding users to their GitHub Organization and Team. Hub admins require *Owner* permissions for their GitHub Organization in order to {ref}`invite non-members<manage-users:github-org>` to it (team maintainers or regular members do not have the power to invite non-members to GitHub Organizations). Inviting a user to the organization does not automatically grant the user access to a hub. A member of a GitHub Organization must be added to a {ref}`GitHub Team<manage-users:github-team>` associated with the hub in order to log into the hub with their GitHub credentials.

#### First time setup

When we setup authentication to use [GitHub orgs or teams](auth:github-orgs), we create an OAuth app in the 2i2c org and ask hub admins to install this app upon first login to the hub.

```{seealso}
See our [Infrastructure Guide](https://infrastructure.2i2c.org/hub-deployment-guide/configure-auth/github-orgs/#how-to-setup-github-auth) on how 2i2c sets up GitHub OAuth apps.
```

You will be presented with a list of all the GitHub orgs related to your account.
Some will already be authorised and have a green tick next to them, others where you are a member will have a "Request" button next to them.
Orgs where you are an admin will have a "Grant" button next to them. Click the "Grant" button next to the _target_ org associated with your hub before clicking the green "Authorize" button.

For example, see the below screenshot where we wish to grant the `nasa-cryo-staging` OAuth app access to the `binderhub-test-org` org.

```{figure} /images/granting-org-access-to-oauth-app.jpg
How to grant org access to an OAuth app on GitHub
```

```{warning}
If this is not done correctly, all users will report a `403 Forbidden` error when they try to login. If this happens, please contact [support](/support.md) and we can revoke all user tokens of the auth app to restart the process.
```

The OAuth app will now have the correct permissions to read the org info and hence users should be able to successfully log into their hub.

(manage-users:github-org)=
#### Manage your GitHub Organization

##### Invite a non-member to the organization

:::{figure} ../../images/manage-users-github.png
:name: gh-org-people
:width: 100%
:alt: Screenshot showing a list of members of the 2i2c-community-showcase GitHub Organization.

Screenshot showing a list of [2i2c-community-showcase](https://github.com/orgs/2i2c-community-showcase/people) GitHub Organization members. The *People* tab menu is located at the top; the green *Invite member* button is located in the top right; the *Failed invitations* tab is located in the left sidebar and the *Member settings* ![member settings button](../../images/manage-users-github-settings.png) icon is located next to each member account.

:::

1. Navigate to the GitHub Organization page at `https://github.com/<organization_name>`
1. Invite a non-member to the organization by clicking the green *Invite member* button and searching by username, full name or email address.
1. The invited user will receive an email and GitHub notification inviting them to join the GitHub Organization.

   :::{warning}
   Invitations to join a GitHub Organization will expire after 7 days, after which you can cancel and then retry the invitation by clicking the *Failed invitations* tab in the left sidebar.
  
   :::

1. Once the user has accepted, they will become visible in the list of Organization members in the *People* menu tab.

##### Remove a member from the organization

Members can be removed from the organization by going to the *People* menu tab.

1. Click the ![member settings button](../../images/manage-users-github-settings.png) icon next to the member account you wish to remove.

1. Select the *Remove from organization...* option.

1. Confirm removal by clicking the *Remove members* button.

1. The user will receive an automatic email from GitHub notifying them that they have been removed from the organization.

(manage-users:github-team)=
#### Manage your GitHub Team

A GitHub Team is defined and specially linked to a hub's configuration when it is initially deployed. This special GitHub Team should be known to hub administrators. If not, please contact your community representative who deployed the hub or open a 2i2c {doc}`support ticket<../../support>`.

##### Add a member to the team

Add members to the GitHub Team associated with the hub so that users can log into the hub with their GitHub credentials.

1. From the GitHub Organization page `https://github.com/<organization_name>`, click on the *Teams* menu tab.
1. Click on the GitHub Team that authorizes access to the hub see a list of members.

  :::{figure} ../../images/manage-users-github-team.png
  :width: 100%
  :alt: Screenshot showing a list of members of the access-2i2c-showcase GitHub Team.
  
  Screenshot showing a list of [access-2i2c-showcase](https://github.com/orgs/2i2c-community-showcase/teams/access-2i2c-showcase) GitHub Team members.
  
  :::

1. Invite an existing member of the organization to join the team by clicking the green *Add a member* button and searching by username, full name or email address.
  
1. The account will instantly appear in the list of team members and the user does not need to accept an invitation to join. The user may choose to leave the team by clicking the *Leave team* button on the same page.

1. The user has authorization to log into the hub using their GitHub credentials 🎉

##### Remove a member from the team

Hub admins can remove user access to a hub by removing their account from the GitHub Team.

  :::{figure}  ../../images/manage-users-github-team-remove.png
  :width: 100%
  :alt: Screenshot showing how to remove a member from the access-2i2c-showcase GitHub Team.
  
  Screenshot showing how to remove a member from the [access-2i2c-showcase](https://github.com/orgs/2i2c-community-showcase/teams/access-2i2c-showcase) GitHub Team.
  
  :::

1. From the GitHub Team page `https://github.com/orgs/<organization_name>/teams/<team_name>`, check the box next to the member account you wish to remove (in this case, `jmunroe-testuser` in the screenshot above).
1. Click the tab at the top of the list labelled *1 member selected*.
1. Select *Remove from team* from the dropdown menu.
1. Confirm your choice in the pop up by clicking *Remove members*.
1. The account will instantly disappear in the list of team members and the user will not be notified.

## Finding usernames

Usernames are assigned depending on the kind
of [authentication provider](admin/configuration/authentication) your hub is
using. In general, it matches whatever the visible 'username' in your
authentication provider is. The table below lists the available providers, and
how to determine their username.


| Provider | Username |
|-|-|
| CILogon | Email address |
| GitHub | GitHub user name |

% TODO: Document how to remove users

## Debug user authentication issues

### CILogon

If users are running into strange errors when they log in (for example CILogon error pages that say "Looks like something went wrong!"), ask them to try these steps in debugging:

1. Try logging in with an `incognito` window. This will help determine if their issue is due to some cookie / cache that is stored on their machine.
2. Ask them to clear their cookies / cache for all CILogon websites. For example, [here are the Google Chrome instructions to clear cookies](https://support.google.com/chrome/answer/95647?hl=en&co=GENIE.Platform%3DDesktop).
3. If using `CILogon`, double-check that they've signed in with the correct account, and [ask them to switch accounts if needed](https://infrastructure.2i2c.org/howto/troubleshoot/cilogon-user-accounts/).
