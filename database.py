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
from datetime import datetime
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

#function này ko nên ở file này, vì ko phải thuần database,
#và nó có thể viết lại bằng cách call lại những functions ở trên.
# nên add function to add_checkin(phone) như ở dưới

def add_checkin(phone, services):
    conn = init_connection()
    try:
        data, _ = conn.table("Check_in").insert({"Phone_Number": phone, "Service": services, "Date": date}).execute()
        return True
    except:
        return False

# Khi đó, function này đc viết lại với logic như sau:
    # check for client ìnfo,
    # ìf found,
        # add to checkin
        # update point
    # else,
        # prompt user to signup

# Chú ý, function này ko nên nằm ở file này.
def checkin(phone, services):
    conn = init_connection()
    check = get_client(phone)
    date = datetime.today()
    if check != None:
        add_checkin(phone, services)
        update_point(phone)
        return True
    else:
        return "Please sign up"

# tương tự check in
def signup(fname, lname, dob, phone):
    conn = init_connection()
    check = get_client(phone)
    if check:
        return "You have already sign up"
    else:
        data, _ = conn.table("Client").insert({"First_Name": fname, "Last_Name": lname, "DOB": dob, "Phone_Number": phone, "Point": 0}).execute()
        return data[1]

def main():
    phone = "6027238354"
    services = "Full_set"
    client = checkin(phone, services)
    print(client)

if __name__ == "__main__":
    main()
