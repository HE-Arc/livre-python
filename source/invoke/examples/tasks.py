"""Hello world avec invoke."""

from invoke import task


@task
def ouverture(ctx):
    """Dit bonjour."""
    print("bonjour")
