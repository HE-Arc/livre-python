from invoke import task, run


@task
checks(ctx):
    ctx.run("git fetch")
