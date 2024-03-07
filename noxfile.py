import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["--builder", "dirhtml", "."]
sphinx_build_command = ["-b", "dirhtml", ".","_build/html"]

@nox.session(venv_backend="conda")
def docs(session):
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        AUTOBUILD_IGNORE = [
            "_build",
            "build_assets",
            "images/shared_responsibility_diagram.png",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
        cmd.extend(sphinx_build_command)
        session.run(*cmd)
    else:
        session.run("jupyter-book", "build", *build_command)
