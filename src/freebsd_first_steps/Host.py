from traceback import print_exc

import streamlit as st
from streamlit_searchbox import st_searchbox

from freebsd_first_steps.api import hostname, timezone


HOSTNAME = hostname.get()
TIMEZONE = timezone.get_system_timezone()


st.title("FreeBSD First Steps")
st.markdown(
    f"""
    This is an interactive guide to set up your new FreeBSD machine.

    It will help you set up a Virtual Private Network (VPN) 
    using [Tailscale](https://tailscale.com) to access your
    FreeBSD machine from anywhere, harden and lock it down, 
    and set up any common private or public services you may want.
    """
)


st.markdown(
    f"""
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
        print_exc()
        st.error(e)
        st.stop()


st.markdown(
    f"""
    ### Timezone

    When hosting public services, prefer UTC.
    Local timezone might be more convenient for private services.

    The current timezone is `{TIMEZONE}`.
    """
)
new_timezone = st_searchbox(
    timezone.search,
    key="timezone_searchbox",
)
if new_timezone and new_timezone != TIMEZONE:
    try:
        timezone.set_system_timezone(new_timezone)
        st.success(f"Timezone changed to {new_timezone}")
    except Exception as e:
        print_exc()
        st.error(e)
        st.stop()


st.markdown(
    """
    #### Next

    [Set up a Private Network](/Private_Network)
    """
)
