import streamlit as st
import homepage
import page1

PAGES = {
    "Home": homepage,
    "Visualization": page1
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
