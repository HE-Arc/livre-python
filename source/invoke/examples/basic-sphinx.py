from invoke import task, run


@task
def html(ctx):
    ctx.run("sphinx-build -b html source build/html")
