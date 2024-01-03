import click
import frappe
import subprocess


@click.command('create-frappe-next')
@click.option("--name", default="frontend", prompt="Dashboard name")
@click.option("--app", prompt="App Name")
def create_frappe_next(name, app):
    if not app:
        click.echo("Please provide an app with --app")
        return
    
    click.echo("Adding Next Js app to frappe app {app}...")
    
    add_next_app_starter(name, app)

    click.echo(
        f"🖥️  You can start the dev server by running 'yarn dev' in apps/{app}/{name}"
    ) 


def add_next_app_starter(name, app):
    from pathlib import Path

    subprocess.run(
        ["npx", "degit", "nahomdev/frappe-nextjs-starter", name],
        cwd=Path("../apps", app),
    )

    subprocess.run(["yarn"], cwd=Path("../apps", app, name))
 

 commands = [add_next_app_starter]