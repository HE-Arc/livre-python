from invoke import task, run

@task
def build(ctx):
    ctx.run("sphinx-build -b html source build/html")
