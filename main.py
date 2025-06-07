# import streamlit as st
# from home import app as home_app
# from docs import app as docs_app
# from data import app as data_app

# if "page" not in st.session_state:
#     st.session_state.page = "Home"

# col1, col2, col3, _ = st.columns([1,1,1, 10])
# with col1:
#     if st.button("Home"):
#         st.session_state.page = "Home"
# with col2:
#     if st.button("Docs"):
#         st.session_state.page = "Docs"
# with col3:
#     if st.button("Data"):
#         st.session_state.page = "Data"

# st.markdown("---")  
# if st.session_state.page == "Home":
#     home_app()
# elif st.session_state.page == "Docs":
#     docs_app()
# elif st.session_state.page == "Data":
#     data_app()


# Your column buttons here...

import streamlit as st
from home import app as home_app
from docs import app as docs_app
from data import app as data_app

# Use the updated query param API
query_params = st.query_params
page = query_params.get("page", "Home")

# Top horizontal nav links
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: start;
            gap: 20px;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        .navbar a {
            text-decoration: none;
            font-weight: 600;
            color: #4a4a4a;
            padding: 8px 16px;
            border-radius: 8px;
        }
        .navbar a:hover {
            background-color: #eee;
        }
    </style>
    <div class="navbar">
        <a href='?page=Home' target="_self">Home</a>
        <a href='?page=Docs' target="_self">Docs</a>
        <a href='?page=Data' target="_self">Data</a>
    </div>
""", unsafe_allow_html=True)

# Load the correct page
if page == "Home":
    home_app()
elif page == "Docs":
    docs_app()
elif page == "Data":
    data_app()
else:
    st.error("Page not found.")
