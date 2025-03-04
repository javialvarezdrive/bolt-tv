import streamlit as st
from app.database import init_supabase_client
from app.components import auth, dashboard, user_management, activity_management

st.set_page_config(
    page_title="Gym Management App",
    page_icon="💪",
)

def main():
    supabase = init_supabase_client()

    # Initialize session state
    if 'user' not in st.session_state:
        st.session_state.user = None

    st.title("Gym Management App")

    if not st.session_state.user:
        if auth.display_auth_forms(supabase):
            st.rerun()
    else:
        st.sidebar.write(f"Welcome, {st.session_state.user.user.email}!")
        auth.logout()

        app_mode = st.sidebar.selectbox(
            "Choose the App mode",
            ["Dashboard", "User Management", "Activity Management"]
        )

        if app_mode == "Dashboard":
            dashboard.dashboard()
        elif app_mode == "User Management":
            user_management.user_management()
        elif app_mode == "Activity Management":
            activity_management.activity_management()

if __name__ == "__main__":
    main()
