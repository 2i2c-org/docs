
# Community documentation with Jupyter Book

Community documentation is a great way to spread learning and knowledge across your user base. You can share workflows, tutorials, examples meant for re-use, and topics to help others understand the key ideas in your community.

:::{admonition} Where to find examples of community books
Our [demo gallery](https://2i2c.org/demo-gallery/) has links to a number of example books written with Jupyter Book 2. You can also check out the [Project Pythia](https://projectpythia-mystmd.github.io/) and the [CryoCloud community book](https://book.cryointhecloud.com/intro.html) for real-world examples.
:::

2i2c recommends communities use [Jupyter Book 2](https://next.jupyterbook.org), which uses the [MyST Document Engine](https://mystmd.org/guide), a next-generation engine for technical documentation and computational narratives. Both are developed by the [`Jupyter Book` subproject of Jupyter](https://compass.jupyterbook.org). See [the MyST Ecosystem Overview](https://mystmd.org/guide/overview) for more information about MyST and Jupyter Book.

:::{admonition} Jupyter Book integrations with 2i2c infrastructure is experimental
:class: caution
This feature is an experimental addition by 2i2c. It may change as we learn more about how communities are using it.
:::

## Get started with Jupyter Book

Using the [2i2c community documentation template][2i2c-org/community-docs-template], you can get started by customising an existing bare-bones Jupyter Book. This template includes examples of:

- Basic configuration for a Jupyter Book.
- A [landing page][guide-landing].
- Authoring content that uses [a Python Jupyter kernel][guide-kernel].
- Using rich [cross-referencing] features to create a knowledge base.

Why not start by [adding your own glossary][guide-glossary], or [adding your own logo][guide-logo]? See [](#learn-authoring) for more tips about authoring content with Jupyter Book 2 and the MyST Engine.

(jb-deploy)=
### Deploy your Jupyter Book as a website

To deploy a Jupyter Book online, we recommend the following steps:

- The Community Representative should use the [2i2c-org/community-docs-template] template to [create their own repository][use-template].[^gh]
- For a [custom domain next to your hub](#jb-custom-domain), provide the 2i2c team with _temporary_ **owner access** to the repository. We will ensure that various configuration such as the custom domain and GitHub Actions are set up correctly.
- Use GitHub Pages to host your book content online.[^ssg] See [the MyST Engine guide to GitHub Pages](https://mystmd.org/guide/deployment-github-pages) for more documentation (it uses MyST, which behaves very similarly to Jupyter Book 2).

[^gh]: You can use a different book structure rather than the template if you like. In this case, just make sure you're hosting the book's source files on GitHub in order to use GitHub pages!

[^ssg]: In this case, we use Jupyter Book / MyST as a [Static Site Generator](https://en.wikipedia.org/wiki/Static_site_generator), which creates static HTML files.

(jb-custom-domain)=
## Get a dedicated docs URL next to your hub

Once your documentation is deployed online, 2i2c can give your community a special URL that makes your documentation more memorable and easier to find. If your hub is located at `<COMMUNITY>.2i2c.cloud`, then your documentation will be hosted at the subdomain:

```
docs.<COMMUNITY>.2i2c.cloud
```

To enable this, first [get your Jupyter Book hosted online](#jb-deploy), then open a support ticket with the 2i2c team requesting that this be done.

## Add buttons that launch interactive sessions on your hub

You can create content that is designed to connect with your
2i2c JupyterHub. For example, you can:

- Create course lectures using Jupyter Notebooks as the source files.
- Host your book online by [following the instructions above](#jb-deploy).
- Create a button on each page that will let students launch an interactive session on their hub, with their own copy of the content ready for editing.

To do so, follow these steps:

1. Configure your book to add launch buttons by following the [mystmd instructions launch buttons](https://mystmd.org/guide/website-launch-buttons).
2. Instruct your users to paste in the URL of your community hub to the launch button pop-up (e.g., `https://<your-hub>.2i2c.cloud`).

For example, here's what it would look like to use the URL of the [2i2c showcase hub](https://compass.2i2c.org/projects/managed-hubs/showcase-hub/):

```{figure} ../images/launch-button-menu.png
:width: 75%
The launch button pop-up with the 2i2c showcase hub URL pasted. Clicking the {kbd}`Launch` button will ask your user to log-in, and then launch an interactive Jupyter server with the source file of the current page loaded for editing.
```

(learn-authoring)=

## Learn how to author content with Jupyter Book and MyST Markdown

The [Jupyter Book documentation] and the [MyST Markdown Guide] are useful resources for learning about Jupyter Book 2 and the MyST Engine that powers it. To understand how Jupyter Book 2 and the MyST engine relate to one another, see [this documentation page][jb-toolchain]. A brief overview of the MyST Markdown Syntax can be found at the [MyST Engine Typography Guide](https://mystmd.org/guide/typography).

The MyST Engine implements powerful sharing and reusing features. One of the most exciting of these is the ability to preview and [embed content from external MyST sites][guide-embed]. This can be used to richly reference and include figures, glossary terms, and even entire documents from useful resources! Amongst communities that share a set of best practices and understanding, this feature may be particular useful for building upon the work of others.

[MyST Markdown Guide]: https://mystmd.org/guide/quickstart
[Jupyter Book documentation]: https://next.jupyterbook.org/start
[2i2c-org/community-docs-template]: https://github.com/2i2c-org/community-docs-template
[guide-logo]: https://mystmd.org/guide/website-templates#site-options
[guide-glossary]: https://mystmd.org/guide/glossaries-and-terms
[guide-landing]: https://mystmd.org/guide/website-landing-pages
[guide-kernel]: https://mystmd.org/guide/execute-notebooks
[guide-embed]: https://mystmd.org/guide/embed#embed-from-external-myst-projects
[cross-referencing]: https://mystmd.org/guide/cross-references
[jb-toolchain]: https://next.jupyterbook.org/about/toolchain
[use-template]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
