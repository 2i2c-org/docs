# Dynamic image building

Dynamic image building integrates the capabilities of [BinderHub](https://binderhub.readthedocs.io/en/latest/) with a JupyterHub. This flexibility enables users to manage their own software image environments in the cloud. See the [blog post](https://2i2c.org/blog/2024/jupyterhub-binderhub-gesis/) for more details.

## Quickstart

This is a quick guide to getting started with dynamic image building. Note that [repo2docker](https://repo2docker.readthedocs.io/en/latest/) is the underlying technology that powers dynamic image building. This feature presently works with GitHub repositories only.

<video width="100%" autoplay loop>
  <source src="/_static/videos/demo-dynamic-image-building.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

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

   If you include a `Dockerfile`, then `repo2docker` uses this definition and ignores the above files and a regular Docker build is performed. See the [Binder docs](https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html) for guidance on advanced configurations.

:::{note}
Generally it is best practice not to use `environment.yml` and `requirements.txt` together, as this can lead to conflicts. If you need both `conda` and `pip` packages, use `environment.yml` with `pip` packages listed under the `pip:` section. If you need just `pip` packages, use `requirements.txt` only.
:::

### Step 2: Configure the JupyterHub “Build your own image” Option

1. In JupyterHub, choose **“Build your own image”** from the **Image** dropdown in the launcher.
2. Enter your GitHub repo name (e.g. [binder-examples/requirements](https://github.com/binder-examples/requirements))
3. Optionally include a branch, tag or commit to use. By default, the `HEAD` will use the default branch.
4. Click the {bdg-primary}`Build` button to start the build process. You can view the build logs to monitor progress.
5. Once the build is complete, choose the **Resource Allocation** (CPU, RAM) for the server launch.
6. Click {bdg-primary}`Start` to launch your server.

### Step 3: Use and Share Your Environment

1. If you re-launch the same repo and **reuse the same image later**, the build is cached by `repo2docker` unless you update your repo.
1. You can also **share your repo link** with others so they can build the same image in another dynamic image building service or BinderHub.

## Benefits

* **No Dockerfile expertise needed** — `repo2docker` generates a Dockerfile automatically from commonly used configuration files of popular package managers, but allows advanced builds for those who are comfortable with Dockerfiles.
* **Reproducible** – your environment configuration is fully described in version-controlled files.
* **Portable to Binder** – the same setup works on [mybinder.org](https://mybinder.org) and any BinderHub, as well as other JupyterHubs with dynamic image building.
