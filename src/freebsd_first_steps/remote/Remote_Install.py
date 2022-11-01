from pathlib import Path
from traceback import print_exc

import streamlit as st
from plumbum import SshMachine
from pydantic import BaseModel
from statelit import StateManager
from streamlit_searchbox import st_searchbox


PYTHON = "python3.10"
PYTHON_PKG = "python310"

class SSHConnectionModel(BaseModel):
    hostname: str = ""
    username: str = ""
    identity_file: str = ""


ssh_state_manager = StateManager(SSHConnectionModel)

st.title("FreeBSD First Steps: Remote Install")
st.markdown(
    f"""
    This is an interactive guide to set up `FreeBSD First Steps` on a remote machine.
    """
)

ssh_connection = ssh_state_manager.form()
if ssh_connection.hostname and (btn_connect := st.button("Connect and Install…")):
    st.info(f"Connecting to {ssh_connection.hostname}...")

    with SshMachine(
        ssh_connection.hostname,
        user=ssh_connection.username,
        keyfile=ssh_connection.identity_file,
    ) as machine:
        st.caption("Running `uname -a`")
        uname_output = machine["uname"]("-a")
        st.code(uname_output)
        if "FreeBSD" not in uname_output:
            st.error("FreeBSD not detected")
            st.stop()
        st.success("FreeBSD detected")

        # Python
        try:
            st.caption(f"Running `{PYTHON} --version`")
            python_installed = machine[PYTHON]("--version")
        except Exception:
            st.text(f"Installing {PYTHON}...")
            st.code(machine["pkg"]("install", "-y", PYTHON_PKG))
            st.success(f"{PYTHON} installed")
        finally:
            python_installed = machine[PYTHON]("--version")
            st.code(python_installed)

        # Pip
        try:
            st.caption(f"Running `{PYTHON} -m pip --version`")
            pip_installed = machine[PYTHON]("-m", "pip", "--version")
        except Exception:
            st.text(f"Installing pip...")
            st.code(machine[PYTHON]("-m", "ensurepip"))
            st.success(f"pip installed")
        finally:
            pip_installed = machine[PYTHON]("-m", "pip", "--version")
            st.code(pip_installed)
        
        # Poetry
        try:
            st.caption(f"Running `poetry --version`")
            poetry_installed = machine["poetry"]("--version")
        except Exception:
            st.text(f"Installing poetry...")
            st.code(machine[PYTHON]("-m", "pip", "install", "poetry"))
            st.success(f"poetry installed")
        finally:
            poetry_installed = machine["poetry"]("--version")
            st.code(poetry_installed)

        # Git
        try:
            st.caption(f"Running `git --version`")
            git_installed = machine["git"]("--version")
        except Exception:
            st.text(f"Installing git...")
            st.caption(f"Running `pkg install -y git`")
            st.code(machine["pkg"]("install", "-y", "git"))
            st.success("git installed")
        finally:
            git_installed = machine["git"]("--version")
            st.code(git_installed)

        # Ensure latest freebsd-first-steps
        repo_exists = False
        try:
            repo_exists = machine["ls"]("/root/freebsd-first-steps")
            st.caption(f"Running `git pull`")
            st.code(machine["git"]("pull", cwd="/root/freebsd-first-steps"))
            st.success("freebsd-first-steps updated")
        except Exception as e:
            print_exc()
            st.text(f"Cloning freebsd-first-steps...")
            st.caption(f"Running `git clone https://github.com/hiway/freebsd-first-steps.git`")
            st.code(machine["git"]("clone", "https://github.com/hiway/freebsd-first-steps.git", "/root/freebsd-first-steps"))
            st.success("FreeBSD First Steps cloned")

        # Install freebsd-first-steps via poetry
        st.text(f"Installing freebsd-first-steps...")
        st.caption(f"Running `poetry install`")
        st.code(machine["poetry"]("install", cwd="/root/freebsd-first-steps"))

        # Run freebsd-first-steps
        st.success("FreeBSD First Steps is now installed on the remote machine.")
        st.warning("You must ssh into the remote machine to run the app.")
        st.code(f"ssh -i {ssh_connection.identity_file} {ssh_connection.username}@{ssh_connection.hostname}")
        st.code(f"{PYTHON} -m freebsd_first_steps serve")
