import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", ".", "_build/html"]

@nox.session(python="3.9")
def docs(session):
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        AUTOBUILD_IGNORE = [
            "_build",
            "build_assets",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
        cmd.extend(build_command)
        session.run(*cmd)
    else:
        session.run("sphinx-build", *build_command)
