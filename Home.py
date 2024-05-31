'''
- Trong multipage app, ngoại trừ trang chủ chính (home or main), những trang còn lại phải ở trong folder pages:
- Ngoài ra, những files backends, hoặc templates, components, media (images, video, text data
) nên group vào chung từng folders.

    Ví dụ:
    project_directory/
        Home.py
        .streamlit/
            config.toml
            secrets.toml #store api key, and api url
        pages/
            1_Page_Name_1.py
            2_Page_Name_2.py
        backends/
            database.py
            message.py
        components/
            ...
        static/
            logo.svg
            content.toml
            ...
'''

import streamlit as st
from backends.database import init_connection, get_client

# ---------------Settings -----------------

page_title = "Posh Lounge | Home"
page_icon = "💅"
layout = "centered"


# -----------------------------------------

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout,
    initial_sidebar_state="collapsed",
)
st.title("Welcome to Posh Nail Lounge")

# ----- HIDE Streamlit Style --------------

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        h1 {text-align:center;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container(border=True):

    st.link_button(
        label="Go to Check In",
        url="/Check_In",
        use_container_width=True,
        type="primary",
    )
    st.link_button(
        label="Go to Option",
        url="/Option",
        use_container_width=True,
        type="primary",
    )
