# Modify your hub's user environment

When your users log in to their hub, they are presented with a
configured environment with base libraries, user interfaces and
languages installed. This allows them to start working immediately,
without having to install packages themselves.

## Default user environment

The default environment for all pilot hubs is defined [in this
folder](https://github.com/2i2c-org/pilot-hubs/tree/master/images/user). 
It is configured with the following:

- Python packages defined in [this `environment.txt`
  file](https://github.com/2i2c-org/pilot-hubs/blob/master/images/user/environment.txt). Many common scientific python packages are installed here.
- R packages installed from [this `install.R`
  file](https://github.com/2i2c-org/pilot-hubs/blob/master/images/user/install.R).
- Many popular data science user interfaces installed:
  - [Classic Jupyter Notebook](https://github.com/jupyter/notebook/)
  - [JupyterLab](https://github.com/jupyterlab/jupyterlab/)
  - [RStudio](https://rstudio.com/)
- An Ubuntu 20.04 base image, with common utility packages installed.

(environment/custom)=
## Customizing your hub environment

Sometimes, what is in the base user environment is not enough for
your use case. You might need new packages installed, a different 
language version, etc. Here are a few ways to customize yours.

### Ask for changes to the base image

If you only need one / two extra packages, the easiest way is to
[open an issue in the `2i2c-org/pilot` repository](https://github.com/2i2c-org/pilot/issues/new?labels=enhancement&template=tech-request.md) 
and ask for the new package to be installed. This is often the simplest
way forward.

### Bring your own docker image

Our hubs use [docker images](https://www.docker.com/) to provide the
user environment. You can build and bring your own docker image,
which gives you *full control* over your environment.

We recommend the following setup for building & maintaining your
docker image:

1. Create a GitHub repository that will contain just your *environment* files,
   not content. You could use just files that help [create your environment on
   mybinder.org](https://repo2docker.readthedocs.io/en/latest/config_files.html) - like `environment.yml` or `requirements.txt` for python,
   `install.R` for R, etc. You can also instead have a `Dockerfile`
   for full control. Another popular option is to use a `Dockerfile` but
   inherit from a [pangeo base image](https://github.com/pangeo-data/pangeo-docker-images),
   making just the modifications you need.
  
2. Use the [repo2docker GitHub Action](https://github.com/jupyterhub/repo2docker-action)
   to automatically build, name and push your image to a docker registry.
   We recommend [pushing to quay.io](https://github.com/jupyterhub/repo2docker-action#push-image-to-quayio),
   a registry with more generous rate limits than DockerHub's. You can
   [use DockerHub](https://github.com/jupyterhub/repo2docker-action#push-repo2docker-image-to-dockerhub),
   or any other public registry.
   
3. Use the [JupyterHub configurator](configurator.md) to configure the image used
   by your hub. You **must** include the tag your built image was pushed with,
   and specify that. So something like `quay.io/my-user/my-image:784f4b3dac34`,
   not `quay.io/my-user/my-image` or `quay.io/my-user/my-image:latest`. Selecting
   'Tags' in either dockerhub or quay.io should give you the correct tag. Looking
   in the output of the GitHub action for your repository also gives you the tag
   to use.
   
```{note}
If the new image you use breaks user server starts, or is broken in some other
way, you can revert back to the old image by specifying *that*. You can also
leave the field blank to use the default 2i2c image.
```
   
### Temporarily install packages for a session


You can temporarily install packages in your environment that will 
just last the duration of your user session. They will get wiped out
when your user server is stopped, to ensure that you always start from
a 'clean slate' environment.

The recommended way is to put `%pip install <list-of-packages>` or
`%conda install <list-of-packages>` in the first cell of any notebook
you distribute, so when run it'll install necessary packages. For R,
you can use `install.packages("package-name")` as you normally would.

```{warning}

While tempting, do not use `!pip install --user <packages>` to install
packages. This makes the base environment different for different users,
causing hard to debug issues. This could also render your user server
unable to start, due to conflicting packages.
```
