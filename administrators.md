# Administrator Guide

## Your hub's environment

### The default environment

By default your 2i2c Hub has several packages installed for Python and R. The environment for all pilot hubs is defined [in this folder](https://github.com/2i2c-org/low-touch-hubs/tree/master/image). It is a bit technical, but gives an idea of the kinds of libraries that are installed by default. In particular:

- For Python: [see this `environment.yml` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/image/environment.yml) for common Python packages
- For R: [see this `install.R` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/image/install.R)

### Customize the hub's environment

Currently, the best way to customize your hub's environment is to [open an issue in this repository](https://github.com/2i2c-org/pilot/issues/new?labels=enhancement&template=tech-request.md) and ask for the new package to be installed. We are working on ways to let individual hubs customize their environment on their own, and will update these docs when that happens!

### Installing packages from *within* a Jupyter session

Note that you may install packages from within a running JupyterHub session (e.g. by running `pip install mypackage` from the terminal). However, these packages will be removed the next time that you start a JupyterHub session.

## Choose the interface

There are a three main interfaces available on the 2i2c Hubs. You may choose from each of these by altering the URL of your session. For example, here is the general structure of a URL for your personal 2i2c Hub session:

```
https://<your-hub>.pilot.2i2c.cloud/user/<your-username>/<your-interface>
```

You can replace the contents of `<your-interface>` to be one of the following:

- **JupyterLab**: `/lab`
- **Jupyter Notebook**: `/tree`
- **RStudio**: `/rstudio`

Note that your 2i2c Hub administrator can also configure the **default** interface that users see. In addition, you can configure the interface that **nbgitpuller links** point to, see [](include-content) for information about nbgitpuller links.

## The Administrator Dashboard

The JupyterHub administrator dashboard allows you to control several aspects of your JupyterHub. It is available via most of the user interfaces on your hub, as well as at the following URL:

```
https://<your-hub>.pilot.2i2c.cloud/hub/admin
```

:::{note}
The administrator panel will only be available to user names you have explicitly requested to be administrators!
:::

```{figure} images/admin-panel.png
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

## Add / remove users

To add or remove users for your 2i2c Hub, go to the **Administrator Panel** and click on the `Add Users` button. This will allow you to add one-or-more users to the hub.

The types of usernames you add will depend on the kind of authentication you've requested for your hub (e.g., email addresses vs user names).

````{panels}
:container: full-width
:card: border-1
```{figure} images/add-users-button.png
The add users button.
```
---
```{figure} images/add-users-form.png
Fill in usernames and optionally make them administrators.
```
````

(access-server)=
## Take control of a user's server

If you'd like to debug a user's server, you may take control over their session by clicking the **access server** button. This will show you the latest file that they were working on. This is particularly useful for helping them debug a problem with their session.

```{figure} images/access-server.png
Clicking "access server" will allow you to control the user's session.
```
