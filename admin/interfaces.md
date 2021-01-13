# Administrator interfaces

## The Administrator Dashboard

The JupyterHub administrator dashboard allows you to control several aspects of your JupyterHub. It is available via most of the user interfaces on your hub, as well as at the following URL:

```
https://<your-hub>.pilot.2i2c.cloud/hub/admin
```

:::{note}
The administrator panel will only be available to user names you have explicitly requested to be administrators!
:::

```{figure} ../images/admin-panel.png
An example administrator's panel
```

From the administrator panel, you can see several columns and buttons:

`User`
: The username of each user in your 2i2c Hub (both logged-in and logged-out)

`Admin`
: Whether that user is an administrator

`Last Activity`
: The last time that the user's server logged any activity (e.g. opening a file, running code, or logging in).

`Running`
: Whether the user's server is currently running. You may also **start or stop a user's server** from this column.

`Shutdown Hub`
: Shutdown the hub for all users (it may be restarted as well).

`Edit User`
: Edit the username information or make a user an administrator.

`access server`
: Take over the user's session so that you may inspect what they are doing (this is helpful for debugging).

