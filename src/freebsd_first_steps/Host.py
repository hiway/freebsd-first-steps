import streamlit as st
from pydantic import BaseModel
from statelit import StateManager


from freebsd_first_steps import api


HOSTNAME = api.hostname() or "freebsd"


class FreeBSDHost(BaseModel):
    hostname: str = HOSTNAME


state_manager = StateManager(FreeBSDHost)

state = state_manager.form()

if state.hostname != HOSTNAME:
    st.write(f"Change hostname to: {state.hostname!r}?")
    btn_change_hostname = st.button("Change")
    if btn_change_hostname:
        try:
            api.set_hostname(state.hostname)
            st.success(f"Hostname changed to: {state.hostname!r}")
        except Exception as e:
            if "Operation not permitted" in str(e):
                st.error("You must run this app as root")
            else:
                st.error(e)
            st.stop()
