import subprocess

import click
from plumbum import SshMachine


@click.group()
def main():
    pass


@main.command()
def serve():
    """Run as streamlit app."""
    subprocess.run(["streamlit", "run", "src/freebsd_first_steps/Host.py"])


@main.command()
def ssh_install():
    """Install FreeBSD on a remote machine."""
    subprocess.run(["streamlit", "run", "src/freebsd_first_steps/remote/Remote_Install.py"])
