# Getting Started

## Access the hub

To access the hub, you will need to navigate to the URL provided by your hub administrator. This URL will look something like `https://<your-hub>.2i2c.cloud`.

Logging into the hub depends on the authentication method. The most common methods are:

- **CILogon**: You will be redirected to the CILogon portal to log in with your institutional account/Google account/Microsoft account, etc.
- **GitHub**: You will be redirected to GitHub to log in with your GitHub account.

If you are having trouble logging in, please contact your hub administrator.

## Start a new server

Depending on the configuration of your hub, a new server may start automatically when you log in that drops you into JupyterLab/RStudio.

For other hubs, you will presented with a *Server Options* page where you can select the memory and CPU resources for your server. You can also select the software environment that you would like to use.

![JupyterHub server options](/images/server-options.jpeg)

It is important to use cloud resources responsibly to maximize efficiency and minimize carbon emissions. Selecting a larger server incurs a larger financial cost, as well as an environmental cost!

Best practices for using resources responsibly include

- shutting your server as soon as you are finished with your work
- selecting the server option with the minimum number of CPU cores and RAM needed to carry out your work
- running code efficiently and developing sustainable research software where possible, e.g. test your program first before scaling to larger datasets.

## Environment and interface

There are three main interfaces available on the 2i2c JupyterHubs: JupyterLab, Jupyter Notebook, and RStudio.

You may switch between these user interfaces by navigating to the appropriate URL

```bash
https://<your-hub>.2i2c.cloud/user/<your-username>/<your-interface>
```

where you can replace `<your-interface>` with one of the following (where available in your software environment):

- **JupyterLab**: `/lab`
- **Jupyter Notebook**: `/tree`
- **RStudio**: `/rstudio`

### JupyterLab

```{figure} /images/jupyterlab.png
:alt: JupyterLab layout
```

[JupyterLab](https://github.com/jupyterlab/jupyterlab) is a modern version of the classic Jupyter notebook from
the Jupyter project. This typically includes the classic notebook, a file explorer, an integrated terminal, as well as powerful extensions.

### Jupyter Notebook (Classic)

The [original single-document interface](https://jupyter-notebook.readthedocs.io/en/latest/) for creating Jupyter Notebooks.

### RStudio

```{figure} /images/rstudio.png
:alt: RStudio
```

[RStudio](https://rstudio.com) is an IDE for R, created by the RStudio company.

### Software environment

You can temporarily install packages in your environment that will
last the duration of your user session. They will get wiped out
when your user server is stopped, to ensure that you always start from
the 'default' environment provided by your hub administrator.

You can add `%pip install <list-of-packages>` or
`%conda install <list-of-packages>` in the first cell of any notebook
you distribute if you need to install any necessary extra packages. For R,
you can use `install.packages("package-name")` as you normally would.

```{warning}
While tempting, do not use `!pip install --user <packages>` to install
packages. This makes the base environment different for different users,
causing hard to debug issues. This could also render your user server
unable to start, due to conflicting packages. [See this blog post on using pip in Jupyter](http://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/) for some helpful explanation.
```

## Shutting down your server

When you are finished with your work, it is important to shut down your server to save resources and reduce costs.

### Shut down from JupyterLab

To shut down your server in JupyterLab, click on the `File` menu, then `Hub Control Panel`, and then `Stop My Server`.

### Shut down from Jupyter Notebook

To shut down your server in Jupyter Notebook, click on the `File` menu, then `Hub Control Panel`, and then `Stop My Server`.

### Shut down from RStudio

To shut down your server in RStudio, navigate to

```bash
https://<your-hub>.2i2c.cloud/hub/home
```

to access the `Hub Control Panel` and then click on the `Stop My Server` button.

:::{caution}
For technical reasons, pressing the red power button in the top-right corner of the RStudio interface does not actually shut down your server. Please use the `Hub Control Panel` to stop your server.
:::
