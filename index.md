# The 2i2c Hubs Pilot

The 2i2c Hubs Pilot is a project to provide JupyterHubs running on cloud infrastructure in a manner that is both accessible and scalable to many hubs and organizations. It is being run by [the international interactive computing collaboration](https://2i2c.org).

Thanks for your interest in the 2i2c Hubs pilot. This documentation should help give you an idea for the goals of this pilot project, as well as information about how you can use and customize the 2i2c Hubs that are deployed.

:::{admonition,warning} The pilot is in an alpha phase!
Information that you see here might be out-of-date as our technology stack and information around it are rapidly changing.
:::

## What are the technical goals of the Hubs for All pilot?

We have the following goals in conducting this pilot:

- Build technical infrastructure that can automatically and flexibly deploy lightweight JupyterHubs
- Understand the limitations of this approach, both technical and user-oriented
- Improve the underlying technology needed in order to accomplish this
- Build relationships with partners in research and education who wish to use these hubs for their use-cases
- Develop a model for sustainably deploying and maintaining these hubs for research and education

## Who is eligible for the 2i2c Hubs pilot?

We are looking for small-ish users from research and education who would like to participate in this pilot program. If you'd like to do one or more of the following using interactive computing infrastructure in the cloud, please [get in touch](https://2i2c.org/#contact).

- Run a 3-50 person class
- Run data science infrastructure for your team or lab
- Run a collaborative project with distributed users
- Provide online interactive environments for content that you write

## What kinds of guarantees do I have for this pilot?

We know that it is really frustrating to rely on infrastructure that is undependable or often breaks. For this reason, we've designed 2i2c Hubs to be as fault-tolerant as possible. If things break, they should break for only one person rather than for an entire hub. If things must be changed, they should be changeable easily and quickly.

In addition, JupyterHub is designed to give you a degree of administrative control over what's going on inside. For example, you can add your own users and even help them debug their problem by taking over their session. See []

That said, this is a pilot being run with limited resources. You should not expect someone to respond to your questions and problems *immediately*. However, we'll do our best to get back to you quickly.

## Using a 2i2c Hub

For information about how to use a hub, see [](use.md).

## What's in a 2i2c Hub?

For information about the infrastructure behind a 2i2c Hub, see [](infrastructure.md).

```{toctree}
:hidden:
use
infrastructure
```
