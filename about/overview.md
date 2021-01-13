(about-the-project)=
# Overview of the 2i2c Hubs

2i2c Hubs offer data science environments to multiple users via a JupyterHub that runs in the cloud.
They are designed and deployed by the [International Interactive Computing Collaboration](https://2i2c.org) (or 2i2c). They are [a team with many years of experience](https://2i2c.org/about/) running interactive computing infrastructure for research and education.

There are several flavors of hubs to choose from, each designed for a different use-case in research and education.
Hubs are tailored for the community that uses them - their environments and infrastructure can be customized, and all of the deployment and configuration of a hub is fully transparent and re-usable.

See [](infrastructure.md) for more information about the infrastructure and technology behind 2i2c Hubs.

:::{admonition} Get a hub for your community

If you're interested in working with 2i2c to get a hub for your own community, please [send us an email](mailto:hello@2i2c.org) and we'd be happy to discuss options with you.

:::

## Your Right to replicate

A core principle of 2i2c is to build and manage technology that is controlled by the community that uses it.
One way in which we adhere to this principle is by respecting the [Customer Right to Replicate](https://2i2c.org/right-to-replicate/). This states the following:

```{epigraph}
The Right to Replicate gives customers the right to replicate their infrastructure in its entirety elsewhere, with or without 2i2c.
```

We believe that following this principle will lead to a more equitable and more productive ecosystem for research and education in the cloud. It also helps avoid many of the potential downsides of relying on a cloud vendor for infrastructure. Read the [Right to Replicate](https://2i2c.org/right-to-replicate/) documentation for more information about what this means.

(people-behind-hubs)=
## What 2i2c provides

Each Hub is a collaboration between 2i2c team members, and representatives from the community that uses the hub.
They require a variety of expertise to design, deploy, maintain, and use.

Generally speaking, 2i2c provides **development** and **operation** of a 2i2c hub, as well as **support** for questions and issues that arise with the hub infrastructure.
It does this in collaboration with leaders from the community for a particular hub (usually, these leaders have "administrative" rights on a hub with more priveleges for user control etc).

See {doc}`tc:sre` for more information on the roles needed to run the hub.

## Moving off of a 2i2c Hub?

2i2c Hubs are designed to use entirely open-source tools that work in other contexts. You can take your workflows elsewhere if you wish, and you can even deploy your own JupyterHub that recreates the same cloud-based experience. For more information, see [](migration-guide).

### Wait, you really want it to be easy for people to _leave_ 2i2c Hubs?

Yes! We are a non-profit organization with a mission to make open infrastructure for interactive computing more accessible for the research and education community. We believe that using tools that are interoperable, open-source, and owned by the community will most-benefit research and education and make it more equitable and inclusive. For this reason we are committed to deploying open source infrastructure that you can both take elsewhere or even deploy on your own.
