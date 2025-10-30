import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "dirhtml", ".", "_build/dirhtml"]

@nox.session()
def docs(session):
    """Build the documentation with sphinx-build"""
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", *build_command)

@nox.session(name="docs-live")
def docs_live(session):
    """Build the documentation with sphinx-autobuild for live preview"""
    session.install("-r", "requirements.txt")
    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
        "images/shared_responsibility_diagram.png",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command)
    session.run(*cmd)
