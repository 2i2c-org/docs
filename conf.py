# -- Project information -----------------------------------------------------

project = "2i2c Hubs"
copyright = "2020"
author = "2i2c"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_panels",
    "sphinx.ext.intersphinx",
    "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", ".github"]

myst_enable_extensions = ["colon_fence", "deflist", "linkify"]

myst_url_schemes = ["http", "https", "mailto"]
panels_add_bootstrap_css = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_title = "Hubs Documentation"
html_copy_source = True
html_sourcelink_suffix = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/2i2c-org/pilot",
    "use_issues_button": True,
    "use_repository_button": True,
    "navbar_footer_text": "By the <a href='https://2i2c.org'>International Interactive Computing Collaboration</a> (2i2c)"
}
html_baseurl = "https://2i2c.org/pilot"
html_logo = "images/logo.png"
intersphinx_mapping = {
    "tc": ('https://team-compass.2i2c.org/en/latest', None),
    "ph": ('https://pilot-hubs.2i2c.org/en/latest', None),
    "jb": ('https://jupyterbook.org', None)
}

rediraffe_redirects = {
}


def setup(app):
    app.add_css_file("custom.css")
