# Content creation and sharing

These sections describe ways that you can create content for your JupyterHub and share them with your users.

(content:nbgitpuller)=

## Distribute content with nbgitpuller

You'll often want to distribute _content_ (such as notebooks, scripts, sample
data, etc) to your users so they can do exercises, follow along with a lecture,
or use as a starting point for their own work. This content is often constantly
updated as time goes on, and needs to not overwrite your student's work if you
make an adjustment to content that has already been touched by the student.

[nbgitpuller](https://jupyterhub.github.io/nbgitpuller) is the tool
we recommend for this. The workflow goes something like this:

### Ensure that `nbgitpuller` is installed in your user environment

The default environment for 2i2c JupyterHubs has `nbgitpuller` pre-installed.
However, if you [define a custom environment for your hub's users](environment:image), you'll need to ensure that `nbgitpuller` is installed in order for users to use it!

### Put your content in a public GitHub repository

Create a repository on [GitHub](https://github.com) and start putting your
content there. This is the _source_ of the content that will be distributed
to your users. You can update it as often as you wish. While instructors will
need to know how github works, _your users will never have to interact with
git directly_.

### Generate an nbgitpuller link

Generate an [nbgitpuller link](https://jupyterhub.github.io/nbgitpuller/link). This generates a
_clickable link_ that contains within it the following pieces of information:

1. The URL to your hub. Upon clicking the link, users will be redirected to
   this hub, and content will be pulled into their home directory there.
2. The URL of the git repository where the content lives.
3. The branch in the git repository where the content lives. The default
   specified there is `master`, although newer GitHub repositories use `main`
   as the default. You can find yours on the Github page of your content
   repository
4. The default interface to open when users click this link. The default is
   the classic notebook, but many other apps are available.
5. A file to open when the link is clicked. When left empty, a directory
   listing with the content of the repository will be shown.

```{figure} ../images/nbgitpuller-ui.png
The [`nbgitpuller.link`](https://jupyterhub.github.io/nbgitpuller/link) user interface, along with
some important fields highlighted.
```

```{tip}
Unfortunately, RStudio does not support opening a specific file, and will
always show the home directory. Users will have to manually navigate to
the appropriate file.
```

Once you've filled these out, you can copy the link from the textbox above the form.

### Distribute your nbgitpuller link

Distribute the link you have generated to your users. Upon clicking the link,
they will be:

1. Redirected to your hub, and asked to log in if they have not already
2. The first time the link is clicked, your content repository will be pulled
   into their home directory!
3. If they had already clicked the link before, any new changes in your
   content repository will be pulled in. Any changes the user has made will
   be [automatically
   merged](https://jupyterhub.github.io/nbgitpuller/topic/automatic-merging.html)
   with changes in the content repository, in such a way that the user's
   changes are never overwritten. All merge conflicts will also be
   automatically resolved, so users don't have to interact with git.
4. If you have picked a specific file to be displayed, the user will be
   redirected to that file, open in the application you picked. If not, the
   directory listing of local copy of the content repository will be shown in
   the application you selected.

:::{important}

You **do not** have to create a new link each time you update your content
repository! The same link will continue to work, so you can simply ask your
users to click the link again to fetch the latest changes.

However, if you want to create links to individual files that should be
opened at specific points - like one link per class or assignment - you can
regenerate the links with different values for the file to open or interface.
As long as the hub url, content repository url and the branch name are the
same, users will be not be duplicating content.
:::

<!-- ## Serve static web content with your hub

2i2c hubs can serve static web content as a [JupyterHub service](https://jupyterhub.readthedocs.io/en/stable/reference/services.html).
This is useful for hosting documentation for your hub's community.

The content of your static site should live in a `.git` repository as a collection of static HTML files, and the website for these files will be available at a URL like:

```
https://<hub-address>/services/docs
```

Follow these steps to set up documentation for your hub.

### Create your static HTML files

There are many ways to create your own static HTML files, and this guide doesn't cover a specific method.
Here are a few services you should try out:

- [Jupyter Book](https://jupyterbook.org/) is a tool for building rich computational narrative sites from the Jupyter community.
- [Sphinx](https://www.sphinx-doc.org/) is a popular documentation engine in Python
- [Hugo](https://gohugo.io/) is a popular static website generator that is flexible and fast.

Put the generated HTML into a `github` repository in a dedicated branch (so the branch should **only** contain the HTML files).
**Ensure that the HTML files contain relative links**, not absolute links.

:::{tip}
We highly recommend storing your source files in one branch, and automatically generating the HTML for your site via [GitHub Actions](https://docs.github.com/en/actions).
This way, your HTML files will automatically be updated when you update your site content.
:::

### Ask a 2i2c engineer to enable the documentation service for your hub

Your hub will need to be configured by a 2i2c engineer to enable the docs service (following {doc}`these instructions <infra:howto/features/static-sites>`).

- Find the **GitHub repository** and the **branch** where your HTML files are stored.
- [Send a support request](/support.md) asking them to enable this, and provide the repository/branch you found above.

Once this is deployed, your hub's documentation should be accessible at

```
https://<hub-address>/services/docs
``` -->

## Write public books that connect to a 2i2c JupyterHub

You can create public content that is designed to connect with your
2i2c JupyterHub. For example, you can create lectures from Jupyter Notebooks, and allow
students to grab their own copy of the notebook to interact with on the 2i2c
Hub.

To connect your public content with a 2i2c JupyterHub, we recommend using [Jupyter
Book](https://jupyterbook.org). This is an open-source project that allows you
to share collections of notebooks and markdown files as an online website and
book. Check out the {doc}`Jupyter Book getting started
guide<jb:start/overview>` for more information about
Jupyter Book.

You can tell Jupyter Book to place links _directly to your 2i2c JupyterHub_ on each
page that is served from a notebook. To do so, follow the [launch buttons for
JupyterHubs
instructions](https://jupyterbook.org/interactive/launchbuttons.html#jupyterhub-buttons-for-your-pages).
Make sure that you configure your `jupyterhub_url` to point to the URL of your
2i2c JupyterHub (e.g., `https://<your-hub>.2i2c.cloud`).
This will use automatically [create nbgitpuller links](content:nbgitpuller)
for you.

## Deploy documentation with Jupyter Book

2i2c can share "community documentation" alongside your hub under a special `docs.<COMMUNITY>.2i2c.cloud` subdomain. This feature can be used to establish a home for the best practice, useful resources, and rich visualisations built by your community.

:::{caution} Community Documentation is Experimental
This feature is an experimental addition by 2i2c. It may change as we learn more about how communities are using it, and develop new features.
:::

Using a [2i2c-authored template][2i2c-org/community-docs-template], you can quickly get started by customising an existing bare-bones Jupyter Book. This template includes examples of:

- A [landing page][guide-landing].
- Authoring content that uses [a Python Jupyter kernel][guide-kernel].
- Using rich [cross-referencing] features to create a knowledge base.

Why not start by [adding your own glossary][guide-glossary], or [adding your own logo][guide-logo]? See [](#learn-authoring) for more tips about authoring content with Jupyter Book 2 and the MyST Engine.

### Deploy your site with Jupyter Book

The current iteration of this feature requires you to deploy a Jupyter Book 2 static site from a GitHub repository using GitHub Pages. The community representative should use the [2i2c-org/community-docs-template] template to [create their own repository][use-template], and provide the 2i2c team with _temporary_ owner access. We will then ensure that various configuration such as the custom domain and GitHub Actions are set up correctly.

(learn-authoring)=
### Learn about authoring with Jupyter Book and MyST Markdown

The [Jupyter Book documentation] and the [MyST Markdown Guide] are useful resources for learning about the MyST Engine. To understand how Jupyter Book 2 and the MyST engine relate to one another, see [this documentation page][jb-toolchain].
A brief overview of the MyST Markdown Syntax can be found at the [MyST-MD typography guide](https://mystmd.org/guide/typography).

[MyST Markdown Guide]: https://mystmd.org/guide/quickstart
[Jupyter Book documentation]: https://next.jupyterbook.org/start
[2i2c-org/community-docs-template]: https://github.com/2i2c-org/community-docs-template
[guide-logo]: https://mystmd.org/guide/website-templates#site-options
[guide-glossary]: https://mystmd.org/guide/glossaries-and-terms
[guide-landing]: https://mystmd.org/guide/website-landing-pages
[guide-kernel]: https://mystmd.org/guide/execute-notebooks
[cross-referencing]: https://mystmd.org/guide/cross-references
[jb-toolchain]: https://next.jupyterbook.org/about/toolchain
[use-template]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
