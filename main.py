import streamlit as st
import homepage,page1

PAGES = {
  'Home' : homepage,
  'Page 1' : page1,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go To",list(PAGES.keys())
)

page = PAGES[selection]
page.app()