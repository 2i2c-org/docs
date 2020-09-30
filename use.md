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

## Write public books that connect to a 2i2c Hub

You can create public content that is designed to have connections with your 2i2c Hub. For example, you can create lectures from Jupyter Notebooks, and allow students to grab their own copy of the notebook to interact with on the 2i2c Hub.

To connect your public content with a 2i2c Hub, we recommend using [Jupyter Book](https://jupyterbook.org). This is an open-source project that allows you to share collections of notebooks and markdown files as an online website and book. Check out the [Jupyter Book getting started guide](https://jupyterbook.org/start/overview.html) for more information about Jupyter Book.

You can tell Jupyter Book to place links *directly to your 2i2c Hub* on each page that is served from a notebook. To do so, follow the [launch buttons for JupyterHubs instructions](https://jupyterbook.org/interactive/launchbuttons.html#jupyterhub-buttons-for-your-pages). Make sure that you configure your `jupyterhub_url` to point to the URL of your 2i2c Hub (e.g., `https://<your-hub>.pilot.2i2c.cloud`).

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
