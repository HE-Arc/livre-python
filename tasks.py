"""Module de taches pour l'automatisation de la creation de rst."""

from invoke import run, task


# html start
@task
def clean(ctx):
    """Nettoyage du dossier de destination."""
    run("rm -rf build/html")


@task(clean)
def html(ctx):
    """Generation de l'html."""
    run("sphinx-build -b html source build/html")


# checks start
@task
def checks(ctx):
    """Fait les différents checks du programme."""
    run("pydocstyle source")
    run("pycodestyle source")
