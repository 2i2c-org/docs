# Alternative user interfaces

2i2c hubs can run other web applications (for example VS Code, RStudio, or a desktop) inside the same user server. These rely on [`jupyter-server-proxy`](https://jupyter-server-proxy.readthedocs.io/) packages shipped in the user image (see [](./customize.md) to add the proxy packages to your own image).

## How it works

- `jupyter-server-proxy` runs in the user container and forwards web requests to a local process started by a launcher tile or URL such as `/vscode`, `/rstudio`, or `/desktop`.
- A small proxy package (for example `jupyter-vscode-proxy`, `jupyter-rsession-proxy`, or `jupyter-remote-desktop-proxy`) registers the launcher entry and start command for each application.

:::{note}

All interfaces share the same CPU, memory, and storage limits as the Jupyter server.

:::

Once configured, users see new launcher tiles in JupyterLab. Each tile opens the selected interface in a new authenticated browser tab. Below we show an example for a [Linux Desktop and QGIS](#interfaces:desktop).

```{figure} images/jupyterlab-alternative-launcher.png
:alt: JupyterLab launcher showing tiles for VS Code, RStudio, Terminal, and Desktop
:width: 90%

Example launcher showing additional interfaces alongside the default Notebook tile.
```

## Prerequisites

Your [user image](customize.md) needs:

1. The application binary (for example [`code-server`](https://github.com/coder/code-server), [`rstudio-server`](https://posit.co/download/rstudio-server/), or a desktop stack).  
2. The matching proxy package so Jupyter knows how to start and route to it.
3. `jupyter-server-proxy` installed in the environment.

Many community-maintained images (for example Pangeo or Rocker stacks) already include these pieces. If you build your own image, add the proxy package with your package manager (for example `pip install jupyter-vscode-proxy`) so the launcher tile is registered. See [](customize.md) for guidance on building custom images.

## Configure a profile that includes the interface

Expose an interface by pointing a `profileList` entry at an image that contains the app and proxy. Optionally, set `default_url` to the proxy route so users land in the right interface.

### VS Code (code-server)

`jupyter-vscode-proxy` lets you proxy `code-server` (VS Code in the browser), allowing users to develop in VS Code without leaving the hub.

Here is an example from the [Strudel](https://strudel.science/) hub that launches VS Code via `code-server`: 

- [JupyterHub configuration](https://github.com/2i2c-org/infrastructure/blob/a042ecc16ed9d7111eece2ff19261446e69cc0e2/config/clusters/strudel/common.values.yaml#L57-L66)
- [User image configuration repository](https://github.com/strudel-science/strudel-infra)

Pangeo images ship `code-server` with `jupyter-vscode-proxy`. This image is an example of one that already contains the required packages. You can substitute your own image if it includes `code-server` and `jupyter-vscode-proxy`.

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "VS Code"
        slug: "vscode"
        kubespawner_override:
          image: "pangeo/pangeo-notebook:2024.04.16"  # includes code-server + jupyter-vscode-proxy
          default_url: /vscode  # send users straight to VS Code
```

Pin to a specific image tag and adjust resource limits if your community needs more memory for VS Code.

(interfaces:desktop)=
### Linux Desktop (VNC)

`jupyter-remote-desktop-proxy` lets you proxy desktop interfaces as well, allowing users to run GUI applications in the browser.

Here are examples for the desktop proxy (any image with `jupyter-remote-desktop-proxy` works):

* NASA VEDA (QGIS desktop profile):
  - [Hub configuration](https://github.com/2i2c-org/infrastructure/blob/a042ecc16ed9d7111eece2ff19261446e69cc0e2/config/clusters/nasa-veda/common.values.yaml#L166-L173)
  - [User environment image configuration repository](https://github.com/2i2c-org/nasa-qgis-image)

Images with `jupyter-remote-desktop-proxy` expose a lightweight [XFCE](https://www.xfce.org/) desktop for GUI tools such as [QGIS](https://qgis.org/) or [MATLAB](https://www.mathworks.com/products/matlab.html). Use any image that includes `jupyter-remote-desktop-proxy`. The one below is for illustration.

```
jupyterhub:
  singleuser:
    profileList:
      - display_name: "Linux Desktop"
        slug: "desktop"
        kubespawner_override:
          image: "quay.io/2i2c/nasa-qgis-image:0d0765090250"  # includes jupyter-remote-desktop-proxy
          default_url: /desktop  # open the desktop interface
```

```{figure} images/alternative-ui-arcgis.png
:alt: ArcGIS Desktop running in a browser via the remote desktop interface
:width: 90%

Example remote desktop session running [ArcGIS Pro](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview) through the desktop profile.
```

:::{seealso}

* [Jupyter Server Proxy Documentation](https://jupyter-server-proxy.readthedocs.io/) - Authoritative technical guidance.  
* [Jupyter Remote Desktop Proxy](https://github.com/jupyterhub/jupyter-remote-desktop-proxy) - The tool used to provide the desktop experience.  
* [RStudio on Binder/JupyterHub via Rocker](https://rocker-project.org/images/versioned/binder.html) - Documentation on Jupyter-compatible R images.  
* [Not Just for Notebooks: JupyterHub in 2025](https://www.youtube.com/watch?v=vsbHMvvsFw8) - A recent talk by Yuvi Panda on these interfaces (includes others not shown here, like OpenRefine).  
* [Launching alternative UIs on JupyterHub](https://www.youtube.com/watch?v=MvZ-UUpqYMw) - A short walkthrough of VS Code, RStudio, and desktop launchers from [Konstantin Taletskiy](https://taletskiy.com/).  
:::
