import streamlit as st
import pandas as pd 
import plotly.express as px


def app():
  st.image('D:\yashvi\csv_data_explorer\homepage.jpg')
  st.title("CSV Data Explorer")

  st.header("Information Page")

  upload_file = st.file_uploader("Upload File", type='csv')

  if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.session_state['df'] = df


    st.subheader("Data Preview")
    st.dataframe(df)
    st.subheader("Basic Information")


    st.write(f"Shape: {df.shape}")
    st.write("Column Names:", df.columns.tolist())
    st.write("Data Types")
    st.write(df.dtypes)


    st.subheader("Missing Values")
    st.write(df.isnull().sum())
  
    st.subheader("Summary Statistics")
    st.write(df.describe())



