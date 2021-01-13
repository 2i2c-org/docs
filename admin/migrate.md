(migration-guide)=
# Migrating off of a 2i2c Hub

2i2c Hubs are designed to use entirely open source tools that are vendor- and workflow-agnostic. Our goal is to provide you with interactive computing environments that seamlessly integrate with pre-existing workflows across the research and education community. That means we want it to be **extremely easy to move off of a 2i2c Hub**. This section has a few tips for how you can move off of a 2i2c Hub and into a different environment that uses the Jupyter stack.

## The 2i2c Hubs for All deployment repository

If you'd like to see the configuration and deployment scripts for the Hubs for All pilot, you can find it at [the `2i2c-hubs` configuration repository](https://github.com/2i2c-org/pilot-hubs). This is more complex than setting up a single JupyterHub, since it manages the entire federation of 2i2c Hubs in this pilot. You can also find [our documentation for running and configuring hubs with this repository](https://2i2c.org/pilot-hubs/).

## Different ways to re-create your environment without 2i2c

### Deploy your own JupyterHub

2i2c Hubs are an opinionated collection of open source tools, customized for research and education. Using an entirely open stack means that you can deploy these tools yourself if you wish. The first step is to deploy your own JupyterHub, which can run on a variety of cloud vendors (or even your own hardware).

[The Zero to JupyterHub for Kubernetes guide](https://z2jh.jupyter.org) is an opinionated guide to deploying JupyterHub on Kubernetes. The 2i2c team has written much of the content in this guide, and encourages you to follow it in deploying your own hub infrastructure! The 2i2c Hubs use much of the steps in this guide for their deployment. They also use the [JupyterHub Helm Chart](https://github.com/jupyterhub/helm-chart) in order to deploy JupyterHub in a scalable and flexible way.

:::{tip}
If you'd like a more lightweight distribution of JupyterHub, you can try out  [The Littlest JupyterHub](https://tljh.jupyter.org). This distribution of JupyterHub is easier to set up for smaller teams.
:::

### Re-create the user environment locally

The `pilot-hubs` repository has [the configuration for default user environments](https://github.com/2i2c-org/pilot-hubs/tree/master/../images/user). These scripts and files are used to create the Docker image that is used in a 2i2c Hub. We upload that Docker image to a registry and then [configure each JupyterHub to use it here](https://github.com/2i2c-org/pilot-hubs/blob/master/hub/values.yaml#L85).

For more information about creating custom environments for a JupyterHub, we recommend checking out the [repo2docker project](https://repo2docker.readthedocs.io/), which builds Docker images from Binder repositories.

### Use a different managed cloud service

Finally, if you wish to use a different managed cloud service, there are many for you to choose from. These tend to have proprietary components interwoven with open-source ones, which can be a "pro" or a "con" depending on your use-case. 2i2c Hubs are designed to be 100% open source and interoperable with a variety of cloud vendors, however your workflows may be transportable to a proprietary cloud service just the same.

## Download your content and data

(download-as-pdf)=
### Download your notebooks as PDFs

2i2c Hub come with the ability to convert a Jupyter Notebook as a PDF that users may download locally. To do so, use the Jupyter interface of your choice as shown below:

````{panels}
:container: full-width
:column: + text-center
Classic Notebooks
```{figure} ../images/download-latexpdf-classic.png
:height: 300px
```
---
JupyterLab
```{figure} ../images/download-latexpdf-lab.png
:height: 300px
```
````


(download-user-files)=
### Download your data from a hub

If you'd like to stop using your 2i2c Hub, or would simply like to move your data onto your own machine (or elsewhere in the cloud), take the following steps to download your data locally:

1. Navigate to the Jupyter "tree" view by changing your URL path to `/tree`. e.g., `<your-hub>.pilot.2i2c.cloud/user/<your-username>/tree`
2. Click on **`Download Directory`**.

   ```{figure} ../images/download-directory.png
   :alt: The download directory button
   ```

This will zip up the contents of your user file system and download them to your machine.
