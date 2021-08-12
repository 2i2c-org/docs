# The 2i2c Managed JupyterHubs Pilot

A 2i2c Managed JupyterHub is a cloud-based interactive computing environment built entirely on open-source technology and customized for research and education.
It follows best-practices as recommended from open source communities, and is deployed in a manner that is easy for others to replicate on their own.
Each 2i2c Hub is deployed for a specific community, and can be customized for that community.
It brings together **environments, datasets, computing resources, and content**.

To learn more about 2i2c Hubs, see [](about-the-project).

This guide is for **hub administrators and community representatives** of 2i2c Hubs, or for those who are interested in learning more about the 2i2c Hubs.

:::{seealso}
For more general information about the Managed JupyterHub Service, see [the Team Compass documentation for this service](https://team-compass.2i2c.org/en/latest/projects/managed-hubs/roles.html).
:::

See the sections below (or to the left) for more information.

## About the Managed JupyterHubs Pilot

The Managed JupyterHubs Pilot aims to build an open, scalable, sustainable cloud service for interactive computing environments in research and education.
These sections contain information about the service, our goals and strategy for the pilot, and a high-level description of the infrastructure.

```{toctree}
:maxdepth: 1
:caption: About the Pilot
about/strategy
about/overview
about/infrastructure
about/projects
```

## Hub Administrator Guide


### Configuration reference

These pages list the different ways hub admins can configure how
their hub behaves. Some of these can be changed directly by the hub administrator
via the [configurator](admin/howto/configurator.md) interface, while some of
them require help from a 2i2c engineer.

```{toctree}
:maxdepth: 1
:caption: Hub configuration options

admin/configuration/login
admin/configuration/culling
admin/configuration/default-interface
```

## Hub administrator how-to guides

These guides have information on how hub admins can perform specific
tasks on their hubs, mostly without requiring any interaction with
2i2c engineers.

```{toctree}
:maxdepth: 1
:caption: Administrator how-to guides
admin/howto/support
admin/howto/configurator
admin/howto/environment
admin/howto/nbgitpuller
admin/howto/create-content
admin/howto/manage-users
admin/howto/control-user-server
admin/howto/share-datasets
admin/howto/replicate
admin/howto/create-billing-account

```

## Hub user guides

```{toctree}
:maxdepth: 1
:caption: User guides
user/download-data
user/interface
```
