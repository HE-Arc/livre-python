"""Module de demonstration."""


from invoke import task


@task
def ouverture(ctx):
    """Dit bonjour."""
    print("bonjour")
