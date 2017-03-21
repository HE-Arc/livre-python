from invoke import task, run


@task
def html(ctx):
    result = ctx.run("sphinx-build -b html source build/html")


@task
def do_i_need_to_rebase(ctx):
    result = ctx.run("git fetch")


@task
def checks(ctx):
    ctx.run("pycodestyle source")
    ctx.run("pydocstyle source")
