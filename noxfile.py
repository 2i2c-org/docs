import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True


@nox.session()
def docs(session):
    """Build the documentation."""
    session.install("mystmd")
    session.run("python", "scripts/download-images.py")
    session.run("myst", "build", "--html", *session.posargs)


@nox.session(name="docs-live")
def docs_live(session):
    """Build the documentation with live preview server."""
    session.install("mystmd")
    session.run("python", "scripts/download-images.py")
    session.run("myst", "start", *session.posargs)
