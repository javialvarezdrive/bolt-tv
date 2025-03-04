import streamlit as st
from supabase import create_client, Client
from app.config import SUPABASE_URL, SUPABASE_KEY

@st.cache_resource
def init_supabase_client():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase
