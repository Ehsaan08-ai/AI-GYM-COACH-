import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults


def main():

    st.set_page_config(
        page_icon="🏋️",
        page_title="AI Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    if not render_login_wall():
        return

    initial_session_defaults()

    with st.sidebar:
        st.title("🏋️ AI GYM COACH")

        if st.session_state.username:
            st.caption(f"👤Login as {st.session_state.username}")

        st.divider()


if __name__ == "__main__":
    main()
