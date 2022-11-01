import streamlit as st
from freebsd_first_steps.api import hostname


HOSTNAME = hostname.get()


st.title("FreeBSD First Steps")

st.markdown(
    """
    This is an interactive tutorial to set up your new FreeBSD machine.

    It will help you set up a Virtual Private Network (VPN) 
    using [Tailscale](https://tailscale.com) to access your
    FreeBSD machine from anywhere, harden and lock it down, and set up
    common private or public services.

    ## Welcome to FreeBSD!

    Review and make any changes to the default configuration below.

    ### Hostname

    The hostname is used to identify your machine on the network. 
    It is also used to generate the default domain name on Tailscale VPN.

    The current hostname is `{HOSTNAME}`.
    """
)

if (new_hostname := st.text_input("Change hostname:", HOSTNAME))!= HOSTNAME:
    try:
        hostname.set(new_hostname)
        st.success(f"Hostname changed to {new_hostname}")
    except Exception as e:
        if "Operation not permitted" in str(e):
            st.error(
                "**Operation not permitted**: Please run this tutorial as root."
            )
        else:
            st.error(f"Failed to set hostname: {e}")
        st.stop()
