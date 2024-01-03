import click
import frappe
import subprocess


@click.command('create-next-app')
@click.option("--name", default="frontend", prompt="Dashboard name")
@click.option("--app", prompt="App Name")
def create_next_app(name, app):
    if not app:
        click.echo("Please provide an app with --app")
        return
    
    click.echo("Adding Next Js app to frappe app {app}...")
    
    subprocess.run(
        ["npx", "degit", "nahomdev/frappe-nextjs-starter", name],
        cwd=Path("../apps", app),
    )

     click.echo(
        f"🖥️  You can start the dev server by running 'yarn dev' in apps/{app}/{name}"
    ) 


def add_next_app_starter(name, app):
    from pathlib import pathlib

    subprocess.run()

    nahomdev
/
frappe-nextjs-starter