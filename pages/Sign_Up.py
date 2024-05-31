import streamlit as st
from streamlit_option_menu import option_menu
import calendar
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from backends.database import *


def signup(fname, lname, dob, phone):
    conn = init_connection()
    check = get_client(phone)
    if check:
        return "You have already sign up"
    else:
        data, _ = conn.table("Client").insert({"First_Name": fname, "Last_Name": lname, "DOB": dob, "Phone_Number": phone, "Point": 0}).execute()
        return "You have sign up successfully"

    submitted = st.form_submit_button("Submit", type="primary")
    if submitted:
        valid = True
        fname = st.session_state["fname"]
        lname = st.session_state["lname"]
        dob = st.session_state["birthdate"]
        phone = st.session_state["phone"]
        client = (
            st.session_state["phone"],
            st.session_state["fname"],
            st.session_state["lname"],
            st.session_state["birthdate"],
            st.session_state["services"],
        )
        if not client[0].isnumeric() or len(client[0]) != 10:
            st.error(
                f"{client[0]}: Please enter a valid 10-digit phone number.",
                icon="⚠️",
            )
            valid = False
        if not client[1].isalpha():
            st.error(
                f"{client[1]}: Please enter your first name. Alphabet only.",
                icon="⚠️",
            )
            valid = False
        if not client[2].isalpha():
            st.error(
                f"{client[2]}: Please enter your last name. Alphabet only.",
                icon="⚠️",
            )
            valid = False
        if not client[3]:
            st.error(f"{client[3]}: Please set your birthdate.", icon="⚠️")
            valid = False
        if valid:
            result = signup(fname, lname, dob, phone)
