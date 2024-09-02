# User environment and interface

When your users log in to their hub, they are presented with a
configured environment with base libraries, user interfaces and
languages installed. This allows them to start working immediately,
without having to install packages themselves.

(environment/custom)=
## Customize your user environment

While all hubs [come with a default environment](environment/default), it is possible to create a custom user environment for the hub. Here are a few ways that you can do this.

(environment:image)=
### Create your own image

Our hubs use [software containers](https://www.docker.com/resources/what-container/) to enable a reproducible 
software environment for all users on the hub. You can build and bring your own image to the hub, which allows you *full control* over your software environment.

There are two ways that you can do this:

1. [Update a community-maintained upstream image](./update-community-image.md) – add required software packages to an existing community-maintained upstream image. This is the recommended approach for most use cases since this reduces the maintenance burden of keeping the image up to date.
1. [Build your own custom image from scratch](./hub-user-image-template-guide.md) – build a new image from scratch that contains all the required software packages. This is an advanced approach if you want full control beyond what is available through community-maintained images.

```{toctree}
:hidden:

update-community-image
hub-user-image-template-guide
```

### Temporarily install packages for a session

You can temporarily install packages in your environment that will
just last the duration of your user session. They will get wiped out
when your user server is stopped, to ensure that you always start from
the 'default' environment.

The recommended way is to put `%pip install <list-of-packages>` or
`%conda install <list-of-packages>` in the first cell of any notebook
you distribute, so when run it'll install necessary packages. For R,
you can use `install.packages("package-name")` as you normally would.

```{warning}

While tempting, do not use `!pip install --user <packages>` to install
packages. This makes the base environment different for different users,
causing hard-to debug-issues. This could also render your user server
unable to start, due to conflicting packages. [See this blog post on using pip in Jupyter](http://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/) for some helpful explanation.
```

## Create multiple environments for users to select

If your hub's community has workflows that differ significantly, it can be useful to create multiple user environments for your hub.
This uses {ref}`Jupyter Hub User Profiles<z2jh:multiple-profiles>` to create a menu of environment options when a user launches a new session.

To add multiple environments for your hub, take these steps:

1. Follow the steps in [](environment:image) for each environment you wish to offer your hub's users.
   You should have one repository per environment, and each one should push to a Docker image registry via the repo2docker action.
2. [Open a support request](../../../support.md) requesting that your hub be set up to serve multiple user environments.
   A 2i2c engineer will assist you in configuring the hub to set up multiple environments.

(environment/default)=
## The default user environment

The default environment for all community hubs is defined [in this
repository](https://github.com/2i2c-org/2i2c-hubs-image).

It is configured with the following:

- **Python packages**: defined in [this `requirements.txt`
  file](https://github.com/2i2c-org/2i2c-hubs-image/blob/main/requirements.txt). Many common scientific python packages are installed here.
- **R packages**: installed from [this `install.R`
  file](https://github.com/2i2c-org/2i2c-hubs-image/blob/main/install.R).
- **Data science interfaces**: many popular data science user interfaces are installed:
  - [Classic Jupyter Notebook](https://github.com/jupyter/notebook/)
  - [JupyterLab](https://github.com/jupyterlab/jupyterlab/)
  - [RStudio](https://rstudio.com/)
- An Ubuntu 20.04 base image, with common utility packages installed.

(environment:default-interface)=
### Default user interfaces

The 2i2c hubs offer the following user interfaces by default:

#### Jupyter Notebook (Classic)

The [original single-document interface](https://jupyter-notebook.readthedocs.io/en/latest/) for creating Jupyter Notebooks.

#### JupyterLab


```{figure} ../../../images/jupyterlab.png
:alt: JupyterLab layout
```

[JupyterLab](https://github.com/jupyterlab/jupyterlab) is a more modern version of the classic Jupyter notebook from
the Jupyter project. It is more customizable and better supports advanced use cases - particularly around [dask](https://dask.org). Many
research organizations use this.

#### RStudio

```{figure} ../../../images/rstudio.png
:alt: RStudio
```

[RStudio](https://rstudio.com) is an IDE for R, created by the RStudio company.

### Ask for changes to the default environment

If you are using the default environment, and think that one or two packages should be installed by default on it, please [send a support request](../../../support.md) and request an update to the default environment.

## Accessing user interfaces

There are three main interfaces available on the 2i2c JupyterHubs.
There are a few different ways that you may encourage users to switch between them.

### by changing your URL

You may switch between user interfaces interactively by altering the URL of your session.
For example, here is the general structure of a URL for your personal 2i2c JupyterHub session:

```
https://<your-hub>.pilot.2i2c.cloud/user/<your-username>/<your-interface>
```

You can replace the contents of `<your-interface>` to be one of the following:

- **JupyterLab**: `/lab`
- **Jupyter Notebook**: `/tree`
- **RStudio**: `/rstudio`

### by changing the hub defaults

A Hub Administrator can also configure the **default** interface that users see.
To do so, see [the configurator interface guide](configurator:interface).

### by using `nbgitpuller` links

In addition, you can configure the interface that **nbgitpuller links** point to, see [](content:nbgitpuller) for information about nbgitpuller links.
