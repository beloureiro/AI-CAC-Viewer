import streamlit as st
import os
import sys
import json

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importing functions from other sections
from sections.overview import show_overview
from sections.ai_agents import show_ai_agents
from utils.config import DATA_DIR

# Function to load JSON files (only used in the Feedback Analysis tab)
def load_json_files(data_folder):
    data = []
    if not os.path.exists(data_folder):
        st.error(f"The folder {data_folder} does not exist.")
        return data

    # Load JSON files from the folder
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            try:
                # Try to open the JSON file with the correct encoding (UTF-8)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data.append(json.load(f))
            except UnicodeDecodeError:
                st.error(f"Encoding error while reading the file {file_name}. Ensure the file is in UTF-8.")
            except json.JSONDecodeError:
                st.error(f"Error decoding JSON in file: {file_name}")
    return data

# Initial page setup
def setup_page():
    st.set_page_config(page_title="AI Clinical Advisory Crew", layout="wide")

# Main function
def main():
    setup_page()

    # Sidebar tab selection, setting "Overview" as default
    tab = st.sidebar.radio("Select a Tab", ["Overview", "AI Agents", "Feedback Analysis"], index=0)

    if tab == "Overview":
        show_overview()
    elif tab == "AI Agents":
        show_ai_agents()
    elif tab == "Feedback Analysis":
        # Load JSON data only when the Feedback Analysis tab is selected
        if 'feedback_data' not in st.session_state:
            st.session_state.feedback_data = load_json_files(DATA_DIR)
        
        # Check if data has been loaded
        if not st.session_state.feedback_data:
            st.error("No data has been loaded.")
        else:
            st.success("Data loaded successfully!")
            # Place logic here to display the data
            st.write("Displaying feedback data... (future implementation)")

if __name__ == "__main__":
    main()