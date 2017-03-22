"""Module d'automatisation de git."""


from invoke import run, task


@task
do_i_need_to_rebase(ctx):
    """Rebase du projet."""
    ctx.run("git fetch")
