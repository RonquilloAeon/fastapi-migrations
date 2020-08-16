import nox


@nox.session(python="3.8", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-e", ".")


@nox.session(python="3.8", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "src")


@nox.session(python="3.8", reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8", "src")
