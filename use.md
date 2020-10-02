# Customize a hub

This page contains information about using and customizing your 2i2c Hubs.

(include-content)=
## Include content in your hub

To include content in your hub (e.g., scripts, notebooks, etc) we recommend using [`nbgitpuller`](https://jupyterhub.github.io/nbgitpuller).

You can use `nbgitpuller` to generate a link to a public repository, or a file in that repository. When a user clicks that link, then a copy of the link's target will be automatically placed in the user's home directory, and they will be directed to that content in the JupyterHub (if they are logged in).

- **Generate an nbgitpuller link** by going to [`nbgitpuller.link`](http://nbgitpuller.link/). You'll be asked to provide some information about the content you wish to share, and can copy the link when you are done.
  - Use `https://<your-hub>.pilot.2i2c.cloud` as your JupyterHub address
  - Fill in the GitHub repository where your content exists (along with an optional file path or branch name)
  - The link will be in the field just above your form.

- **Share this link with your users**. Anybody can click an `nbgitpuller` link. If they have an account on the hub to which it points, then they'll get a copy of the content that you've linked to.

## Customize the hub's environment

Currently, the best way to customize your hub's environment is to [open an issue in this repository](https://github.com/2i2c-org/pilot/issues/new) and ask for the new package to be installed. We are working on ways to let individual hubs customize their environment on their own, and will update these docs when that happens!

The environment for all pilot hubs is defined [in this folder](https://github.com/2i2c-org/low-touch-hubs/tree/master/image). It is a bit technical, but gives an idea of the kinds of libraries that are installed by default. In particular:

- For Python: [see this `environment.yml` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/image/environment.yml) for common Python packages
- For R: [see this `install.R` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/image/install.R)

### Installing packages from *within* a Jupyter session

Note that you may install packages from within a running JupyterHub session (e.g. by running `pip install mypackage` from the terminal). However, these packages will be removed the next time that you start a JupyterHub session.

## Write public books that connect to a 2i2c Hub

You can create public content that is designed to have connections with your 2i2c Hub. For example, you can create lectures from Jupyter Notebooks, and allow students to grab their own copy of the notebook to interact with on the 2i2c Hub.

To connect your public content with a 2i2c Hub, we recommend using [Jupyter Book](https://jupyterbook.org). This is an open-source project that allows you to share collections of notebooks and markdown files as an online website and book. Check out the [Jupyter Book getting started guide](https://jupyterbook.org/start/overview.html) for more information about Jupyter Book.

You can tell Jupyter Book to place links *directly to your 2i2c Hub* on each page that is served from a notebook. To do so, follow the [launch buttons for JupyterHubs instructions](https://jupyterbook.org/interactive/launchbuttons.html#jupyterhub-buttons-for-your-pages). Make sure that you configure your `jupyterhub_url` to point to the URL of your 2i2c Hub (e.g., `https://<your-hub>.pilot.2i2c.cloud`).

## Storage on the hub

Currently there is **no persistent storage** on the hub. However, we are working to get this implemented soon (hopefully in the next week or two). In the meantime, you should use this hub for demonstrating its functionality and sharing quick sessions with others, but not for long-term work.

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

### Add / remove users

To add or remove users for your 2i2c Hub, go to the **Administrator Panel** and click on the `Add Users` button. This will allow you to add one-or-more users to the hub.

The types of usernames you add will depend on the kind of authentication you've requested for your hub (e.g., email addresses vs user names).

(access-server)=
### Take control of a user's server

If you'd like to debug a user's server, you may take control over their session by clicking the **access server** button. This will show you the latest file that they were working on. This is particularly useful for helping them debug a problem with their session.
