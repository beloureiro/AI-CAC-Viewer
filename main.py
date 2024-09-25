import streamlit as st
import os
import sys
import pandas as pd

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sections.overview import show_overview
from sections.ai_agents import show_ai_agents
from sections.feedback_analysis import show_feedback_analysis
from sections.styles import custom_css
from utils.data_processor import cleanup_data_directory, extract_and_stack_data
from utils.generate_sample_data import generate_sample_data
from config import DATA_DIR

def setup_page():
    st.set_page_config(page_title="AI Clinical Advisory Crew", layout="wide")
    st.markdown(custom_css, unsafe_allow_html=True)

def load_data():
    st.write("DEBUG: Starting load_data function")
    st.write("DEBUG: Cleaning up data directory...")
    cleanup_data_directory()
    
    st.write("DEBUG: Generating sample data...")
    generate_sample_data()

    st.write("DEBUG: Checking created files...")
    files = os.listdir(DATA_DIR)
    if files:
        st.write(f"DEBUG: Files found in {DATA_DIR}:")
        for file in files:
            st.write(f"- {file}")
        
        st.write("DEBUG: Extracting and stacking data...")
        try:
            df = extract_and_stack_data()
            if df.empty:
                st.warning("No data available. Please check the data files.")
            else:
                st.write(f"DEBUG: Data extraction complete. DataFrame shape: {df.shape}")
                st.write("DEBUG: DataFrame columns:")
                st.write(df.columns)
                st.write("DEBUG: First few rows of the DataFrame:")
                st.write(df.head())
                return df
        except Exception as e:
            st.error(f"An error occurred during data extraction: {str(e)}")
    else:
        st.error(f"No files found in {DATA_DIR}. Unable to proceed with data extraction.")
    
    st.write("DEBUG: load_data function completed")
    return None

def main():
    setup_page()

    # Load data only once when the app starts
    if 'data' not in st.session_state:
        st.session_state.data = load_data()

    st.markdown('<h1 style="color: #1b9e4b; font-style: italic;">AI</span> Clinical Advisory <span style="color: #1b9e4b; font-style: italic;">Crew</span></h1>', unsafe_allow_html=True)

    tab = st.sidebar.radio("Select a Tab", ["Overview", "AI Agents", "Feedback Analysis"])

    if tab == "Overview":
        show_overview()
    elif tab == "AI Agents":
        show_ai_agents()
    elif tab == "Feedback Analysis":
        st.write("DEBUG: Calling show_feedback_analysis()")
        show_feedback_analysis(st.session_state.data)

if __name__ == "__main__":
    main()
