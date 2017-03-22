"""Module basic sphinx generation."""


from invoke import run, task


@task
def html(ctx):
    """Generation de l'html en fonction des rst."""
    ctx.run("sphinx-build -b html source build/html")
