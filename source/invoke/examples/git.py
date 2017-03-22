"""Module d'automatisation de git."""


from invoke import task, run


@task
do_i_need_to_rebase(ctx):
    """Rebase du projet."""
    ctx.run("git fetch")
