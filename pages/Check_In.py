import streamlit as st
from streamlit_option_menu import option_menu
import calendar
from backends.database import *



def add_checkin(phone, services):
    conn = init_connection()
    if (get_client(phone) == None):
        return "Please Sign Up"
    else:
        try:
            data, _ = conn.table("Check_in").insert({"Phone_Number": phone, "Service": services, "Date": date.today()}).execute()
            update_point(phone)
            return "Check In Successfully"
        except:
            return "Check In Unsuccessfully"

    submitted = st.form_submit_button("Enter", type="primary")
    if submitted:
        phone = st.session_state.phone
        services = st.session_state.services
        if not phone.isnumeric() or not len(phone) == 10:
            st.error(
                f"{phone}: Please enter a valid 10-digit phone number.", icon="⚠️"
            )
        else:
            results = add_checkin(phone=phone, services=services)
            if results != "Please Sign Up" and results != "Check In Unsuccessfully":
                st.success(
                    f"Welcome, {results[0]}! You have {results[1]} points.",
                    icon="🥳",
                )
            if results == "Please Sign Up":
                st.warning(f"{phone}: New Client. Please sign up.", icon="🙏")
            if results == "Check In Unsuccessfully":
                st.error("Update error. Please retry.", icon="⚠️")
