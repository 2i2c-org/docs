(user:environment-building)=
# Build your own environment from the hub

Dynamic image building allows users to build their own environments on-the-fly, launch interactive sessions with those environments, and share built environments with other users.
It integrates the capabilities of [BinderHub](https://binderhub.readthedocs.io/en/latest/) with a JupyterHub. This flexibility enables users to manage their own software image environments in the cloud.[^blog]

[^blog]: See [this blog post](https://2i2c.org/blog/2024/jupyterhub-binderhub-gesis/) for more details.

:::{admonition} For hub administrators
:class: seealso
To enable dynamic image building, hub administrators should see [](#image-building-setup).
:::

In the demo below, a user selects the {guilabel}`Build your own image` option from the launch dropdown, provides the URL of a GitHub repository containing [repo2docker configuration files](https://repo2docker.readthedocs.io/en/latest/configuration/), builds an environment image from this repository, and launches an interactive session with it.

<video width="100%" autoplay loop>
  <source src="/_static/videos/demo-dynamic-image-building.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

:::{warning}
Currently, user-built environments support only **GitHub** as a repository provider.
:::

## Benefits

* **No Dockerfile expertise needed** — `repo2docker` generates a Dockerfile automatically from commonly used configuration files of popular package managers, but allows advanced builds for those who are comfortable with Dockerfiles.
* **Reproducible** – your environment configuration is fully described in version-controlled files.
* **Portable to Binder** – the same setup works on [mybinder.org](https://mybinder.org) and any BinderHub, as well as other JupyterHubs with dynamic image building.

## How dynamic image building works

This JupyterHub configuration uses the [repo2docker](https://repo2docker.readthedocs.io/en/latest/) tool for building images in a way that JupyterHub can use. It was designed for the [BinderHub technology](https://binderhub.readthedocs.io) which powers [mybinder.org](https://mybinder.org).

## Get started

This is a quick guide to getting started with dynamic image building.

### Step 1: Prepare a GitHub Repository

1. Create a **public GitHub repository**.
2. Add the following optional files (choose what you need):

   * `environment.yml` – for `conda` packages (and/or `pip` Python packages).
   * `requirements.txt` – for `pip` Python packages.
   * `install.R` – for R packages.
   * `apt.txt` – for Ubuntu system packages.
   * `runtime.txt` – to pin Python/R versions if not specified elsewhere.
   * `postBuild` (executable) – script to run after installation.
   * `start` (executable) – script to run each time the container starts.

   If you include a `Dockerfile`, then `repo2docker` uses this definition and ignores the above files and a regular Docker build is performed. See [](#image-building:learn-more) for links to resources to learn more.

### Step 2: Configure the JupyterHub “Build your own image” Option

1. In JupyterHub, choose {bdg-primary}`Build your own image` from the {bdg-primary}`Image` dropdown in the launcher.
2. Enter your GitHub repo name (e.g. [binder-examples/requirements](https://github.com/binder-examples/requirements))
3. Optionally include a branch, tag or commit to use. By default, the `HEAD` will use the default branch.
4. Click the {bdg-primary}`Build` button to start the build process. You can view the build logs to monitor progress.
5. Once the build is complete, choose the {bdg-primary}`Resource Allocation` (CPU, RAM) for the server launch.
6. Click {bdg-primary}`Start` to launch your server.

### Step 3: Use and Share Your Environment

1. If you re-launch the same repo and **reuse the same image later**, the build is cached by `repo2docker` unless you update your repo.
1. You can also **share your repo link** with others so they can build the same image in another dynamic image building service or BinderHub.

(image-building:learn-more)=
## Learn more

### How can I get started with my environment configuration?

See [Get started with repo2docker](https://repo2docker.readthedocs.io/en/latest/start/) for a simple tutorial explaining how to set up your environment repository from scratch.

### What configuration files can I use to configure my environment?

The [repo2docker configuration file guide](https://repo2docker.readthedocs.io/en/latest/configuration/) has a complete list of all configuration files you can use.

### How can I share my hub environment with others on my hub?

Environment images are cached automatically, so if you give another hub user the URL of the repository you used to build your environment, when they follow the same process above, it will be launched from the cache rather than re-built.

### How do I update my hub environment?

Just update any of the files in your environment repository, and your environment will be re-built the next time you launch a session from it.

### Can I use another community's pre-existing environment?

Yes! That's often the simplest choice. See [this repo2docker guide on choosing an environment](https://repo2docker.readthedocs.io/en/latest/use/pathways/) for guidance.

### Where can I learn more about environment configuration and building?

The [repo2docker user guide is the best place to learn more in general](https://repo2docker.readthedocs.io/en/latest/use/).

### Where can I find example repositories?

The [`binder-examples/` GitHub organization](https://github.com/binder-examples/) has a number of repositories that could be built via repo2docker.
