#import streamlit as st
'''
    File này chỉ nên dùng để chứa những functions/classes liên quan đến database thôi,
    những function này sẽ gọi ở font end. Tất cả test code nên chứa trong main function.
   Ko nên có những code bên ngoài bất kỳ function nào.
'''
'''
    This `create_client` function return a supabase client object
    connecting to the database, which is then used to fetch/write/update database.
'''
from supabase import create_client
from datetime import date
import toml

#@st.cache_resource
def init_connection():
    path = ".streamlit/secrets.toml"
    with open(path, "r") as f:
        data = toml.load(f)
    url = data["SUPABASE_URL"]
    key = data["SUPABASE_KEY"]
    return create_client(url,key)

# Ko cần thiết.
# supabase = init_connection()


def get_client(phone):
    conn = init_connection()
    try:
        data, _ = conn.table("Client").select("*").eq("Phone_Number", phone).single().execute()
        return data[1]
    except:
        return None


def get_point(phone):
    conn = init_connection()
    curr_point = conn.table("Client").select("Point").eq("Phone_Number", phone).single().execute()
    return curr_point


def update_point(phone):
    conn = init_connection()
    data = get_point(phone)
    data = data.data['Point']
    new_data = data+1
    updated_data, _ = conn.table("Client").update({"Point": new_data}).eq("Phone_Number", phone).execute()
    return updated_data[1]
