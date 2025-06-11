import pandas as pd
import streamlit as st

def app():
    st.image('D:\yashvi\csv_data_explorer\page1.jpg')
    st.title("Filtered Data Export (Multi-Column)")

    if 'df' not in st.session_state:
        st.warning("Please upload a CSV file from the Home page first.")
        return

    df = st.session_state['df']
    st.write("Original Data Preview")
    st.dataframe(df)

    st.write("Select Columns to Filter")
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select Columns", columns)

    filtered_df = df.copy()

    if selected_columns:
        st.write("Select Values for Each Column")

        for col in selected_columns:
            unique_values = df[col].dropna().unique().tolist()
            selected_values = st.multiselect(
                f"Select values for `{col}`", unique_values
            )
            filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

    st.markdown("---")
    st.write("Filtered Data Preview")
    st.dataframe(filtered_df)

    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Download Filtered CSV",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )
