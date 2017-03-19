from invoke import task

@task
def clean(ctx):
    ctx.run("rm -rf build/html")

@task(clean)
def build(ctx):
    ctx.run("sphinx-build -b html source build/html")
