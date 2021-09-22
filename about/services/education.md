(hub-types:education)=
# Collaborative learning hub

The 2i2c Educational Hubs provide learning environments and infrastructure that is meant for teaching data science.
These hubs are inspired by 2i2c's experience with the [DataHubs at UC Berkeley](https://docs.datahub.berkeley.edu/en/latest/) and the [Syzygy service](https://syzygy.ca/) for Canada.
See the sections below for a description of these hubs and how they are used.

## A brief overview of learning hubs

This hub deployment is designed for distributed learning for students with a variety of backgrounds.

Below is a diagram that showcases some of the major components of this hub:

```{figure} https://drive.google.com/uc?export=download&id=1Mr51-s3D_KHPsAuTXbczaQ7mlPZUs9gm

A high level overview of major components in a collaborative learning hub.
```

And here are a few major aspects of these distributions:

Environment
: By default this hub comes iwth a data science environment that covers most introductory workflows in Python and R.
  It has been inspired by [the Data 8 course at UC Berkeley](http://data8.org/), and has both Python and R environments for learning.
  However, you may also [create your own environment image](environment:image) for your community.
  This can then be paired with auto-grading infrastructure such as [Otter Grader](https://otter-grader.readthedocs.io/), which makes grading large courses much easier.

Content
: The hub comes integrated with [nbgitpuller](https://jupyterhub.github.io/nbgitpuller), which allows you to distribute content that is based online in GitHub repositories.
  This can be paired with tools like [Jupyter Book](https://jupyterbook.org) to provide online textbooks for your hub.

Interfaces
: This hub comes with both JupyterLab, Jupyter Notebook, and RStudio interfaces by default.

Cloud infrastructure
: The cloud infrastructure needed for this hub is relatively minimal, and defaults to **2GB RAM** and **1 CPU** per user.
  This is usually sufficient for most introductory courses.
  It can be increased by Hub Administrators, though this will lead to higher cloud costs.

## A common workflow

Below is a common workflow that communities use with this type of hub:

- **Use Jupyter Book for course textbooks**. This allows you to keep all of your source material in markdown files and Jupyter Notebooks, and hosted online as a book for your course.
- **Use `nbgitpuller` links to distribute content to your students**. To distribute worksheets, labs, etc to students, use [nbgitpuller.link](https://jupyterhub.github.io/nbgitpuller/link) to create nbgitpuller links for your content. Clicking these links will give a student their own version of the content that they may modify and save.
- **Use "launch buttons" to connect your book to your hub**. Jupyter Book allows you to [connect your book with a JupyterHub](https://jupyterbook.org/interactive/launchbuttons.html), which students may use to launch directly into your hub from the textbook.

## Inspiration for this hub

Collaborative learning hubs are inspired by 2i2c's experience running the [DataHubs at UC Berkeley](https://docs.datahub.berkeley.edu/en/latest/), which provide interactive environments for thousands of students across campus.
You can find the [online textbook for the course here](https://inferentialthinking.com).
They are also inspired by our experience with the [Syzygy service](https://syzygy.ca/) for Canada, which runs JupyterHubs for institutions across Canada.
