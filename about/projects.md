# Communities using the 2i2c Hubs

This page has information about the communities that are currently using the 2i2c Hubs, as well as some domain-focused projects.

:::{admonition} If you'd like a 2i2c Hub for your community

Please [shoot us an email](mailto:hello@2i2c.org) and let us know that you're interested.

:::

## Pilot Hub Projects

2i2c is running a few focused pilots to explore hub infrastructure for specific use-cases, sometimes in partnership with other communities. Below is a short description of each.

### Hubs for Education pilot

The Hubs for Education pilot is an attempt at making interactive computing environments more accessible to the research and education community, with a focus on smaller colleges and minority-serving institutions. It is a collaboration between [CloudBank](https://www.cloudbank.org/), the [Berkeley Division of Computing, Data Science, and Society](https://data.berkeley.edu/dsep), and [2i2c](https://2i2c.org).

Cloud computing credits for these hubs are provided by [CloudBank](https://www.cloudbank.org/) as part of a collaboration with UC Berkeley.

In addition, hubs that are not covered by CloudBank credits are paid for by a grant from [the JROST Rapid Response Fund](https://investinopen.org/blog/jrost-rapid-response-fund-awardees/).


### Pangeo Hubs pilot

The Pangeo Hubs pilot is a collaboration with [the Pangeo Project](https://pangeo.io/), which is a distributed scientific community for big-data geoscience.
The Pangeo approach has become a leading approach in cloud-native geospatial analytics, and drives development across many parts of the PyData ecosystem.
This pilot is an attempt at deploying Pangeo-like hubs with scalable Dask clusters via Kubernetes.


### Events Hubs pilot

A common pattern in the research and education community is to run a hub for a time-bound event.
For example, for a workshop or a hackathon.
This hub infrastructure is ephemeral, and should be both created and taken down quickly, in order to avoid spending too much on cloud costs.
This pilot is an experiment in building a fast and flexible deployment infrastructure that is well-suited to these short-term events.


## A list of current hubs

Below is a relatively up-to-date list of the hubs we are currently deploying as part of this pilot.

```{include} ../_build/hubs-table.txt
```
