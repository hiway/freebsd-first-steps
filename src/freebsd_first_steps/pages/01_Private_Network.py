import streamlit as st

from freebsd_first_steps.api import tailscale



st.title("Private Network")

st.markdown(
    """
    In order to access your FreeBSD machine, we need to set up a private network
    between your computer and the machine. This is done using
    [Tailscale](https://tailscale.com/).

    Tailscale is a Virtual Private Network (VPN) that allows you to access your devices from anywhere.
    It is free for personal use and is open source.

    ## Install Tailscale on your local computer

    Tailscale is available for all major operating systems. You can install it
    from the [Tailscale website](https://tailscale.com/download).

    Once installed, you can log in using your email address and password.

    ## Install Tailscale on your FreeBSD machine

    Tailscale is available in the FreeBSD ports tree. 
    You can install it using `pkg`:

    ```bash
    pkg install tailscale
    ```

    Once installed, you can start Tailscale using:

    ```bash
    service tailscaled enable
    service tailscaled start
    ```

    You can then authorize your FreeBSD machine on Tailscale using:

    ```bash
    tailscale up
    ```

    You will be asked to log in using a web browser.
    Open the link provided by Tailscale and authorize.

    ### Access your FreeBSD machine from anywhere

    Once your FreeBSD machine is authorized on Tailscale, you can access it from
    anywhere using the Tailscale network on your local computer.

    You can find your FreeBSD machine's private IP address 
    in the Tailscale app and connect to it instead of the public IP address.
    """
)