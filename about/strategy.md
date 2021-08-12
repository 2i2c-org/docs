# Strategy and goals

2i2c aims to make interactive computing infrastructure more accessible through a sustainable and scalable service model.
The 2i2c Managed JupyterHubs Pilot is an attempt at building infrastructure, process, and a sustainability model for this service.
We aim to run this pilot for several months, gaining experience and sharpening our understanding of how the service could best-meet the needs of the communities we wish to serve.

2i2c values transparency and inclusion, and aims to run this pilot in an open manner.
This page describes the major strategy of the 2i2c Managed JupyterHubs pilot.

## Goals of the pilot

The primary aim for this pilot is **understanding how the managed JupyterHub service can be most impactful**.
Below are some major goals that we have:

- Gain experience in running infrastructure for many different research and education organizations.
- Understand the diversity of organizations we may wish to serve, and the best way to reach each of them.
    - For example, large vs. small organizations, research vs. education.
- Build deployment infrastructure that allows us to serve a small number of institutions, with a pathway to scaling to more institutions more quickly.

## Communities we'll focus on

2i2c aims to serve a diverse group of institutions during the pilot in order to understand the unique needs that each of them has.
We hope to serve around **20-25** communities in the pilot.
Here are a few major types of communities we hope to serve and learn from:

- Community Colleges
- Research teams within universities
- University-wide education
- Event-based commmunities of practice

## Use-cases we'll focus on

2i2c must understand the major use-cases that it can focus its infrastructure efforts around, in order to build a repeatable and scalable service.
In the pilot, we will focus on a subset of use-cases that we believe are impactful across many communities of practice and organizations.

- **Collaborative learning environments** - Communities of Practice that are focused around teaching and learning, and benefit from shared infrastructure to facilitate communicating and sharing with one another. Similar to our experience with Data 8, Syzygy, and Callysto.
- **Scalable research environments** - Communities of Practice that use cloud infrastructure to scale their workflows - either by accessing large datasets or leveraging scalable computing infrastructure from an interactive session. Similar to our experience with the Pangeo project.
- **Community event hubs** - Communities of Practice that have a time-bound event (e.g., a workshop or hackathon) that would benefit from a shared space to do their work and collaborate with one another. Similar to our experience with the NeuroHackademy and Pangeo workshops.

## Infrastructure strategy for the pilot

We make a few base assumptions about the kind of infrastructure we will focus on in this pilot.
Here are several major components.

### Where to deploy the infrastructure

We'll focus our deployments on **major commercial cloud providers**.
These are the most likely places for organizations to want to run cloud infrastructure, and are the most scalable and sustainable.
In addition, getting Jupyter infrastructure to run well on all of the major cloud providers will have a large impact on a community's right to replicate.

We'll focus on the following cloud providers:

- Google Cloud
- Amazon Web Services
- Microsoft Azure

### Why Jupyter and JupyterHub?

- The Jupyter ecosystem is a collection of building blocks that are highly customizable and composable. They are popular and useful for many use-cases, but still require expertise to customize for a particular need. This is well-suited for 2i2c's skillset and the kind of service it wishes to provide.
- Jupyter is a community-led and multi-stakeholder ecosystem that aligns well with 2i2c's commitment to vendor-agnosticity and the [Right to Replicate](https://2i2c.org/right-to-replicate/).
- JupyterHub allows you to access centralized infrastructure for a community, but in a way that gives that community a lot of control over the details. It is a good balance between "SaaS" and "Fully bespoke community infrastructure". JupyterHub can be deployed via a single repository, but is also deployable by individual people or communities, providing them a clear off-ramp.


## Major questions to answer

Below are the major questions we'd like to answer with this pilot.

- How much work does it take to manage a community of JupyterHubs? What scaling efficiencies can we achieve? 
- What are the major opportunities to improve technology or process to scale more efficiently?
- What is the balance of work between development, operations, administration, and sales?
- What are the major use-cases that can be met with repeatable JupyterHub distributions?
- What kind of support model is sustainable for our team?
- What are the major roles that should exist for a given hub? (both on the 2i2c side and the Community side)
- What other services do communities want other than just a JupyterHub? How would the JupyterHub connect with other services?
- What new development is needed to facilitate collaboration, communication, and exploration on a JupyterHub?

## Deployment and operations strategy

Our goal is to provide a service that minimizes infrastructural complexity while providing JupyterHubs that can be used my Communities of Practice independently of one another.
We wish to minimize the amount of engineering labor needed to develop and operate these deployments.
Below are a few major aspects of the service that we believe provide a good chance of accomplishing these goals:

- Deploy independent JupyterHubs from a centralized deployment system
- Use Terraform to build Kubernetes clusters on cloud providers, and Kubernetes as a base to run the actual JupyterHub infrastructure.
- JupyterHubs should be pre-configured for a use-case, but customizable by the community
- JupyterHubs will respect the Community's [Right to Replicate](https://2i2c.org/right-to-replicate/)
- JupyterHubs may be more bespoke than is sustainable provided we can learn from them.
- JupyterHubs should be able to connect with external datasets and services, as the community needs.
- JupyterHubs should be customizable by the communities they serve, ideally without intervention from a 2i2c Engineer.

## Our Timeframe
- Begin serving hub infrastructure immediately, as long as we do not over-extend our team
- Finish one iteration by Q1 2022.
- major questions should have research and answers by then.
- model for scaling the hub service should be developed by then

## Where will we work?

All of the work done in this pilot should be open and public by default, leveraging workflows that are common to open source communnities.
We will need to create some private channels for communication for conversations with sensitive or private information, but will strive to do everything that we can in public.

Currently, all of our deployment infrastructure and development can be found at [the `pilot-hubs/` repository](https://pilot-hubs.2i2c.org).
