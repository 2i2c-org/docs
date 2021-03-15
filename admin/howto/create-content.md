# Create content for your Hub

## Write public books that connect to a 2i2c Hub

You can create public content that is designed to connect with your
2i2c Hub. For example, you can create lectures from Jupyter Notebooks, and allow
students to grab their own copy of the notebook to interact with on the 2i2c
Hub.

To connect your public content with a 2i2c Hub, we recommend using [Jupyter
Book](https://jupyterbook.org). This is an open-source project that allows you
to share collections of notebooks and markdown files as an online website and
book. Check out the [Jupyter Book getting started
guide](jb:start/overview) for more information about
Jupyter Book.

You can tell Jupyter Book to place links *directly to your 2i2c Hub* on each
page that is served from a notebook. To do so, follow the [launch buttons for
JupyterHubs
instructions](https://jupyterbook.org/interactive/launchbuttons.html#jupyterhub-buttons-for-your-pages).
Make sure that you configure your `jupyterhub_url` to point to the URL of your
2i2c Hub (e.g., `https://<your-hub>.pilot.2i2c.cloud`).
This will use automatically [create nbgitpuller links](nbgitpuller.md)
for you.
