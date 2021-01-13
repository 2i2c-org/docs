

# Your hub's environment

## Where is your hub configured?

All of the infrastructure that 2i2c deploys uses standard open source tooling and configuration. This means that the configuration for your JupyterHub can be modified just as if you were deploying it yourself. The [`pilot-hubs` repository](https://github.com/2i2c-org/pilot-hubs) has information about the configuration for each hub that 2i2c supports. For example, [this configuration file](https://github.com/2i2c-org/pilot-hubs/blob/master/hubs.yaml) has configuration for a collection of hubs. Each entry (corresponding to one hub) has [a Zero to JupyterHub configuration](https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference.html). This can be modified to customize your hub's setup.

## The default user environment

The default environment for all pilot hubs is defined [in this folder](https://github.com/2i2c-org/low-touch-hubs/tree/master/images/user). It is a bit technical, but gives an idea of the kinds of libraries that are installed by default. 

In particular:

- For Python: [see this `environment.yml` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/images/user/environment.yml) for common Python packages
- For R: [see this `install.R` file](https://github.com/2i2c-org/low-touch-hubs/blob/master/images/user/install.R)

In addition, some [types of hubs](hub-types) have modifications (usually additions) to this software environment.

(environment/custom)=
## Customize your hub's environment

There are two ways that you can customize your hub's environment:

- **Temporarily `pip install` the packages you wish**. These will be installed **for your current session only**, and will be removed if your server stops and re-starts. As such, we recommend putting a collection of `!pip install` commands in the first cell of your notebooks that need extra libraries.
- **Request an update to the hub environments**. To request a new or updated package, [open an issue in the `2i2c-org/pilot` repository](https://github.com/2i2c-org/pilot/issues/new?labels=enhancement&template=tech-request.md) and ask for the new package to be installed.
- **Bring your own Docker image**. You may also use your own Docker image. Simply push your image to a public registry, and [open an issue in the `2i2c-org/pilot-hubs` repository](https://github.com/2i2c-org/pilot-hubs/issues/new) to request that your image be used. In the issue, include the public registry, image name, and tag that you wish to use.
  
  See the [pilot hubs custom image documentation](ph:custom-image) for information about the requirements for these Docker images.

We are working on ways to let individual hubs customize their environment on their own, and will update these docs when that happens!

:::{admonition} Try to avoid installing packages in the user directory
:class: note
Each of your users has their own filesystem that persists across sessions, so it is technically possible to use `pip install --user` to install packages to the home directory so they persist across sessions. However, this is discouraged because it often leads to mismatches between user and instructor environments, and may break functionality on the hub if packages are updated in the base environment that clash with a user-installed package.
:::
