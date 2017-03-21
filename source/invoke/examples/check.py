from invoke import task, run


@task
def checks(ctx):
    ctx.run("pycodestyle source")
    ctx.run("pydocstyle source")
