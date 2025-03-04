import streamlit as st
from supabase import Client
import hashlib

def create_md5_hash(password: str):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def login(supabase: Client):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.error("Please enter both email and password.")
        else:
            try:
                # Hash the password
                hashed_password = create_md5_hash(password)

                # Sign in with email and password
                user = supabase.auth.sign_in_with_password({"email": email, "password": password})

                if user:
                    st.session_state.user = user
                    st.success("Login successful!")
                    return True
                else:
                    st.error("Invalid email or password.")
                    return False
            except Exception as e:
                st.error(f"An error occurred: {e}")
                return False
    return False

def signup(supabase: Client):
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")

    if st.button("Signup"):
        if not new_email or not new_password:
            st.error("Please enter both email and password.")
        else:
            try:
                user = supabase.auth.sign_up({"email": new_email, "password": new_password})
                if user:
                    st.success("Signup successful! Please check your email to verify your account.")
                else:
                    st.error("Signup failed.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def forgot_password(supabase: Client):
    email = st.text_input("Enter your email to reset password")
    if st.button("Reset Password"):
        if not email:
            st.error("Please enter your email.")
        else:
            try:
                response = supabase.auth.reset_password_for_email(email)
                if response:
                    st.success(f"Password reset email sent to {email}!")
                else:
                    st.error("Failed to send reset email.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def display_auth_forms(supabase: Client):
    auth_method = st.radio("Choose authentication method:", ("Login", "Signup", "Forgot Password"))

    if auth_method == "Login":
        return login(supabase)
    elif auth_method == "Signup":
        signup(supabase)
        return False
    elif auth_method == "Forgot Password":
        forgot_password(supabase)
        return False
    return False

def logout():
    if st.button("Logout"):
        del st.session_state.user
        st.rerun()
