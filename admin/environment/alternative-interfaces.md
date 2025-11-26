# Enable alternative user interfaces

While JupyterHub is designed for Jupyter Notebooks, it can also serve as a gateway to other interactive applications. By using the jupyter-server-proxy extension, you can provide users with interfaces like **VS Code**, **RStudio**, or a **Linux Desktop** directly from their browser.

## How it works

The [jupyter-server-proxy](https://jupyter-server-proxy.readthedocs.io/) extension runs inside the user's environment. It allows the Jupyter server to proxy web requests to other locally running services.

When a user clicks an icon in their launcher (e.g., "VS Code"), the proxy starts that application and serves it at a unique URL (e.g., /user/my-name/vscode).

:::{note}

These interfaces run inside the user's container. This means they share the same CPU, RAM, and storage limits as the standard JupyterLab session.

:::

## User Experience

Once configured, users will see new icons in their JupyterLab Launcher. Clicking these icons opens the respective application in a new browser tab, authenticated and ready to use.

## Prerequisites

To enable an alternative interface, your user Docker image must contain two things:

1. **The Application:** The binary or service itself (e.g., code-server or rstudio-server).  
2. **The Proxy Glue:** A Python package that configures Jupyter to recognize the app (e.g., jupyter-vscode-proxy).

Many community-maintained images (like the Pangeo or Rocker stacks) include these by default.

## Configuration

The most common way to expose these interfaces is by defining **Profiles** in your hub configuration. This allows you to map a specific interface ("VS Code Environment") to a Docker image that supports it.

### VS Code (code-server)

The **Pangeo Stack** is a popular choice for Python-based communities that need VS Code. Images like pangeo/pangeo-notebook come with code-server pre-installed.

**Example values.yaml configuration:**

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "VS Code Environment"
        description: "Python environment with VS Code support"
        slug: "vscode"
        kubespawner_override:
          image: "pangeo/pangeo-notebook:2024.04.16"
          # VS Code can be memory intensive; consider higher limits
          mem_limit: 4G
          mem_guarantee: 1G

```

### RStudio

For R-based communities, the **Rocker Project** provides Docker images that combine RStudio with JupyterHub compatibility.

**Example values.yaml configuration:**

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "RStudio"
        description: "RStudio Server with Tidyverse"
        slug: "rstudio"
        kubespawner_override:
          image: "rocker/binder:4.3.1"
          # RStudio often requires running as root to handle user switching
          uid: 0
          cmd: ["/usr/bin/python3", "-m", "jupyterhub_singleuser"]

```

### Linux Desktop (VNC)

For applications that require a full graphical user interface (like QGIS, MATLAB, or SNAP), you can run a lightweight Linux desktop (XFCE) via VNC.

**Example values.yaml configuration:**

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "Linux Desktop"
        description: "Full XFCE Desktop via VNC"
        slug: "desktop"
        kubespawner_override:
          # Many jupyter/scipy-notebook derived images support this
          image: "jupyter/scipy-notebook:latest"
          # Ensure the image has 'jupyter-desktop-server' installed

```

## Community Examples

Several 2i2c communities actively use these configurations. You can reference their public infrastructure repositories for production examples:

* **VS Code:** [Openscapes Configuration](https://www.google.com/search?q=https://github.com/2i2c-org/infrastructure/blob/main/config/clusters/openscapes/openscapes.values.yaml)  
* **RStudio:** [University of Washington Hackweeks](https://www.google.com/search?q=https://github.com/2i2c-org/infrastructure/blob/main/config/clusters/uwhackweeks/hub.values.yaml)  
* **Desktop:** [University of Toronto](https://www.google.com/search?q=https://github.com/2i2c-org/infrastructure/blob/main/config/clusters/utoronto/hub.values.yaml)

:::{seealso}

* [Jupyter Server Proxy Documentation](https://jupyter-server-proxy.readthedocs.io/) — The authoritative source for technical configuration and advanced usage.  
* [RStudio on Binder/JupyterHub](https://rocker-project.org/images/versioned/binder.html) — Documentation from the Rocker Project on their Jupyter-compatible images.  
* [Jupyter Remote Desktop Proxy](https://github.com/jupyterhub/jupyter-remote-desktop-proxy) — The underlying tool often used to provide the Linux Desktop experience.  
* [Not Just for Notebooks: JupyterHub in 2025](https://www.youtube.com/watch?v=vsbHMvvsFw8) — A recent talk by Yuvi Panda demonstrating these interfaces and explaining the vision behind them.  
* Running non-Jupyter applications on JupyterHub (JupyterCon 2020\) — A deeper technical dive into jupyter-server-proxy.  
  :::