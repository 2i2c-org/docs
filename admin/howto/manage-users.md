# Manage access to the hub

The **Administrator Panel** can be used to maintain the list of users
who are authorized to use your hub. You can access this panel by clicking
the 'Admin' button in the top bar in your hub control panel.
Alternatively, you can go to this URL in your browser:
`https://<your-hub-url>/hub/admin`

## To add users

1. Click the {guilabel}`Add Users` button. The {guilabel}`Add Users` dialog box will pop up.
2. Add one or more users, and hit the {guilabel}`Add Users` button to authorize all the users you just added.


````{panels}
:container: full-width
:card: border-1
```{figure} ../../images/add-users-button.png
The {guilabel}`Add Users` button in the Administrator Panel.
```
---
```{figure} ../../images/add-users-form.png
Fill in usernames and optionally make them administrators. You can add multiple users at once by putting a username on each line.
```
````

## Finding usernames

Access is granted or revoked based on `usernames`, and these depend on the kind
of (authentication provider)[admin/configuration/authentication] your hub is
using. In general, it matches whatever the visible 'username' in your
authentication provider is. The table below lists the available providers, and
how to determine their username.


| Provider | Username |
|-|-|
| Google | Email address |
| GitHub | GitHub user name |
| ORCID | ORCID id |


% TODO: Document how to remove users
