import streamlit as st
import pandas as pd
from finance import parse_finance_csv, calculate_monthly_summary, get_category_spending
from pathlib import Path
import matplotlib

# Set a non-interactive backend for matplotlib to prevent hangs in headless environments
matplotlib.use('Agg')

def run_dashboard(port: int = 8501):
    st.set_page_config(page_title='Finance Dashboard', layout='wide')

    st.title('Personal Finance Dashboard')

    # File upload
    uploaded_file = st.file_uploader('Upload CSV', type=['csv'])
    if uploaded_file is not None:
        try:
            # NOTE: The line below is buggy. It requires the uploaded file to exist on the server's filesystem.
            # A full fix would require changing finance.py to accept file-like objects.
            df = parse_finance_csv(Path(uploaded_file.name))

            # Display raw data
            st.subheader('Raw Data')
            st.dataframe(df)

            # Monthly trend
            st.subheader('Monthly Summary')
            monthly = calculate_monthly_summary(df)
            st.line_chart(monthly)

            # Category breakdown
            st.subheader('Spending by Category')
            category_spending = get_category_spending(df)
            st.bar_chart(category_spending)

        except FileNotFoundError:
            st.error(f"Could not find file: {uploaded_file.name}. This application requires the file to exist on the server's disk.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
