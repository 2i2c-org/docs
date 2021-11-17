# -- Project information -----------------------------------------------------

project = "Hub Service Guide"
copyright = "2021"
author = "2i2c"
version = "0.1alpha"
master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", ".github", ".nox", "CONTRIBUTING.md"]

myst_enable_extensions = ["colon_fence", "deflist", "linkify"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_2i2c_theme"
html_title = "Hub Service Guide"
html_copy_source = True
html_sourcelink_suffix = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/2i2c-org/pilot",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "extra_navbar": "",
    "show_toc_level": 2,
}

intersphinx_mapping = {
    "tc": ('https://team-compass.2i2c.org/en/latest', None),
    "infra": ('https://infrastructure.2i2c.org/en/latest', None),
    "jb": ('https://jupyterbook.org', None),
    "z2jh": ('https://z2jh.jupyter.org/en/latest', None),
}

rediraffe_redirects = {
}

# Disable linkcheck for anchors because it throws false errors for any JS anchors
linkcheck_anchors = False


def setup(app):
    app.add_css_file("custom.css")


# Scripts to run
import subprocess
from pathlib import Path
build_assets = Path("build_assets")
build_assets.mkdir(exist_ok=True)
subprocess.run(["python", "feature-table.py"], cwd="scripts")

# ==========================================

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from docutils.nodes import paragraph

def create_summary_card(app, pagename, templatename, context, doctree):
    if not doctree:
        return
    # +
    site_title = context.get("docstitle", "")
    page_title = context.get("title", "")
    text = " ".join([ii.astext() for ii in doctree.traverse(paragraph)])
    N_CHAR_DESCRIPTION = 50
    tagline = " ".join(text.split()[:N_CHAR_DESCRIPTION])
    logo = "./images/logo.png"
    img = mpimg.imread(logo)

    # Colors
    # background_color = "#7e7e7e"
    background_color = "white"
    # text_color = "white"
    text_color = "#7e7e7e"
    # -

    # Size of figure
    ratio = 800 / 418
    multiple = 3

    # +
    fig = plt.figure(figsize=(ratio*multiple, multiple))
    fig.set_facecolor(background_color)

    left_margin = .05

    with plt.rc_context({'font.sans-serif': ["Roboto"], "text.color": text_color}):
        axtext = fig.add_axes((0, 0, 1, 1))
        txt_title = axtext.text(left_margin, .90, site_title, {"size":20,}, ha='left', va='top', wrap=True)
        txt_page = axtext.text(left_margin, .7, page_title, {"size":25, "fontweight": "bold"}, ha='left', va='top', wrap=True)
        txt_page._get_wrap_line_width = lambda : 300

        txt_description = axtext.text(left_margin, .25, tagline, {"size":15}, ha='left', va='top', wrap=True)
        txt_description._get_wrap_line_width = lambda : 400
        axtext.set_axis_off()

    axim = fig.add_axes((.8, .7, .2, .2))
    axim.imshow(img)
    axim.set_axis_off()

    from pathlib import Path
    static_dir = Path(app.builder.outdir) / '_static'
    static_dir.mkdir(exist_ok=True)
    path_out = f"summary_{pagename.replace('/', '_')}.png"
    fig.savefig(static_dir / path_out)
    n_depth = len(pagename.split('/')) - 1
    path_out_image = f"{'../' * n_depth}_static/{path_out}"
    context["metatags"] += f'\n    <meta property="og:image" content="{path_out_image}" />'




# ==================================
def setup(app):
    app.connect("html-page-context", create_summary_card)