import click 
import subprocess


@click.command()
def main():
    """Run as streamlit app."""
    subprocess.run(["streamlit", "run", "src/freebsd_first_steps/Host.py"])
