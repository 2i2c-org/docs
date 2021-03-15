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

myst_url_schemes = ("http", "https", "mailto")
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
    "tc": ('https://2i2c.org/team-compass', None),
    "ph": ('https://2i2c.org/pilot-hubs', None),
    "jb": ('https://jupyterbook.org', None)
}

rediraffe_redirects = {
}

# -- Pull the latest list of hubs---------------------------------------------
import requests
from textwrap import dedent
from yaml import safe_load
from pathlib import Path

resp = requests.get("https://raw.githubusercontent.com/2i2c-org/pilot-hubs/master/hubs.yaml")
hubs = safe_load(resp.text)
entries = ""
for cluster in hubs["clusters"]:

    for hub in cluster["hubs"]:

        if any(ii in hub["name"] for ii in ["staging", "demo", "ephemeral"]):
            continue
        # Some hub configs are at the top level, others are under a `base-hub` sub-field
        if "jupyterhub" in hub["config"]:
            hub_config = hub["config"]["jupyterhub"]
        else:
            for kind in ["base-hub", "ephemeral-hub"]:
                if kind in hub["config"]:
                    hub_config = hub["config"][kind]["jupyterhub"]
                    break
        template_dict = {
            "daskhub": "[Pangeo](hub-types:pangeo)",
            "base-hub": "[Educational](hub-types:education)",
            "ephemeral-hub": "[Ephemeral](hub-types:ephemeral)"
        }
        template = template_dict[hub["template"]]
        info = hub_config["homepage"]["templateVars"]
        org = info["org"]
        website = hub["domain"][0] if isinstance(hub["domain"], list) else hub["domain"]
        entries += f"""
        ---
        [{org["name"]}]({org["url"]})

        [`{website}`](https://{website})

        +++
        Hub Engineer: [{info["operated_by"]["name"]}]({info["operated_by"]["url"]})

        Hub Funder: [{info["funded_by"]["name"]}]({info["funded_by"]["url"]})

        Hub Architect: [{info["designed_by"]["name"]}]({info["designed_by"]["url"]})

        Hub Type: {template}
        """
        # Whenever we get approval, can add this to include logos
        # ^^^
        # [![logo]({hub["org_logo"]})]({hub["org_url"]})
entries = dedent(entries)

hubs_table = f"""
```{{panels}}
:container: full-width current-hubs
:column: col-6 py-2 text-center
:body: +d-flex flex-wrap align-items-center text-center
{entries}
```
"""
path_build = Path("_build")
if not path_build.is_dir():
    path_build.mkdir()
path_build.joinpath("hubs-table.txt").write_text(hubs_table)


def setup(app):
    app.add_css_file("custom.css")
