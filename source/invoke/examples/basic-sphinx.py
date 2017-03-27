"""Module basic sphinx generation."""

from invoke import task


@task
def html(ctx):
    """Génération de la documentation Sphinx en HTML."""
    ctx.run("sphinx-build -b html source build/html")
