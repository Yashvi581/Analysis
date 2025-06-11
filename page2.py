import pandas as pd
import streamlit as st  
import plotly.express as px 
import numpy as np

def app():

  st.image("D:\yashvi\csv_data_explorer\page2.png")

  st.title('Column-wise Distribution Analysis')
  
  if 'df' not in st.session_state:
        st.warning("Please upload a CSV file from the Home page first.")
        return
  
  df = st.session_state['df']

  numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

  if not numeric_cols:
      st.error("No numeric columns found in the uploaded CSV file.")
      return
  
  selected_columns = st.selectbox("Select a numeric column to analyse", numeric_cols,False)


  if selected_columns:
      col_data = df[selected_columns].dropna()

      st.subheader(f"Stats for {selected_columns}")
      st.write(f"Mean: {col_data.mean():.2f}")
      st.write(f"Median: {col_data.median():.2f}")
      st.write(f"Standard Deviation: {col_data.std():.2f}")


      st.subheader("Histogram")
      hist_fig = px.histogram(df, x=selected_columns, nbins=30, title=f"Histogram of {selected_columns}")
      st.plotly_chart(hist_fig)

      st.subheader("Box Plot")
      box_fig = px.box(df, y = selected_columns ,title=f"Box plot of selected columns: {selected_columns}")
      st.plotly_chart(box_fig)




    