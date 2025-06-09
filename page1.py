import pandas as pd
import streamlit as st 
import plotly.express as px
import homepage as homepage

def app():
  st.title('Visualization')

  if 'df' in st.session_state:
    df = st.session_state['df']
    st.dataframe(df)


  x_columns = df.columns.tolist()
  selected_x_columns = st.sidebar.selectbox(
    "Select X-axis",
    x_columns,
    key='x_column_select'
  ) 

  y_columns = df.columns.tolist()
  selected_y_columns = st.sidebar.selectbox(
    "Select Y-axis",
    y_columns,
    key='y_column_select'
  )

  col1,col2 = st.columns(2)

  with col1:
    Bar_chart= st.sidebar.button("Show Bar Chart")

  with col2:
    Pie_chart = st.sidebar.button("Show Pie Chart")

  if Bar_chart:
    st.title("BAR CHART")
    fig = px.bar(df, x=selected_x_columns, y = selected_y_columns, color = selected_x_columns)
    st.plotly_chart(fig)

  if Pie_chart:
    st.title("PIE CHART")
    fig1 = px.pie(df, names=selected_x_columns, values = selected_y_columns, color = selected_x_columns)
    st.plotly_chart(fig1)
