from invoke import task

@task
def play(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)