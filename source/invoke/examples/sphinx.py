"""Module generation de html améliorer."""


from invoke import task


@task
def clean(ctx):
    """Nettoyage du dossier de destination."""
    ctx.run("rm -rf build/html")


@task(clean)
def build(ctx):
    """Generation des documents html en fonction de rst."""
    ctx.run("sphinx-build -b html source build/html")
