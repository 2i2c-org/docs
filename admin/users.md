# Managing users and their sessions


(add-users)=
## Add / remove users

To add or remove users for your 2i2c Hub, go to the **Administrator Panel** and click on the `Add Users` button. This will allow you to add one-or-more users to the hub.

The types of usernames you add will depend on the kind of authentication you've requested for your hub (e.g., email addresses vs user names).

````{panels}
:container: full-width
:card: border-1
```{figure} ../images/add-users-button.png
The add users button in the Administrator Panel.
```
---
```{figure} ../images/add-users-form.png
Fill in usernames and optionally make them administrators. You can add multiple users at once by putting a username on each line.
```
````

(access-server)=
## Take control of a user's server

If you'd like to debug a user's server, you may take control over their session by clicking the **access server** button. This will show you the latest file that they were working on. This is particularly useful for helping them debug a problem with their session.

```{figure} ../images/access-server.png
Clicking "access server" will allow you to control the user's session.
```

```{warning}
When you control a user's server, all of your actions will be run *as if the user ran it themselves*. This can be confusing for some users and is generally not best-practice. We recommend telling users when you are taking over their session, and using this feature mostly to understand what the user was trying to do, rather than to make major changes to their code or notebook outputs.
```

## User session duration

After 1h of *inactivity*, the user's session is culled. This stops all running
notebooks & terminals. They can start them back up again on login - their home
directories are preserved. Any packages they've temporarily installed with `!pip`
or `!conda` are also cleared, so they might have to install them again.

There is no total time limit on how long a user's session
can last.
