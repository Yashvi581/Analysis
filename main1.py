import streamlit as st
import homepage
import page1,page2,page3

PAGES = {
    "Home": homepage,
    "Visualization": page1,
    "Column Distribution" :page2,
    "Export filtered data" : page3,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
