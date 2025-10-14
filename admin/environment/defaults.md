(environment/default)=
# The default user environment

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
## Default user interfaces

The 2i2c hubs offer the following user interfaces by default:

### Jupyter Notebook (Classic)

The [original single-document interface](https://jupyter-notebook.readthedocs.io/en/latest/) for creating Jupyter Notebooks.

### JupyterLab


```{figure} images/jupyterlab.png
:alt: JupyterLab layout
```

[JupyterLab](https://github.com/jupyterlab/jupyterlab) is a more modern version of the classic Jupyter notebook from
the Jupyter project. It is more customizable and better supports advanced use cases - particularly around [dask](https://dask.org). Many
research organizations use this.

### RStudio

```{figure} images/rstudio.png
:alt: RStudio
```

[RStudio](https://rstudio.com) is an IDE for R, created by the RStudio company.

## Ask for changes to the default environment

If you are using the default environment, and think that one or two packages should be installed by default on it, please [send a support request](../../support.md) and request an update to the default environment.
