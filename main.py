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

# Function to display feedback data
def show_feedback_analysis(feedback_data):
    st.header("Patient Feedback Analysis")

    if not feedback_data:
        st.error("No feedback data available. Please check the data source.")
        return

    # Create a list of feedback options based on the loaded JSON data
    feedback_options = [f"Feedback {i+1}" for i in range(len(feedback_data))]
    selected_feedback_idx = st.selectbox("Select Feedback", range(len(feedback_data)), format_func=lambda x: feedback_options[x])
    
    selected_feedback = feedback_data[selected_feedback_idx]

    # Display the patient feedback
    st.subheader("Patient Feedback")
    patient_feedback = selected_feedback.get("patient_feedback", "No feedback found.")
    st.text_area("Feedback", patient_feedback, height=150)

    # Display agent reports
    st.subheader("Agent Reports")
    
    agents = [entry["agent_name"] for entry in selected_feedback.get("agents", [])]

    for i, agent in enumerate(agents):
        col1, col2 = st.columns(2)
        agent_data = next((entry["response"] for entry in selected_feedback.get("agents", []) if entry["agent_name"] == agent), None)
        
        if i % 2 == 0:
            with col1:
                st.markdown(f"**{agent}**")
            with col2:
                if agent_data:
                    for key, value in agent_data.items():
                        st.markdown(f"**{key}:** {value}")
                else:
                    st.warning(f"No data found for {agent}")
        else:
            with col1:
                if agent_data:
                    for key, value in agent_data.items():
                        st.markdown(f"**{key}:** {value}")
                else:
                    st.warning(f"No data found for {agent}")
            with col2:
                st.markdown(f"**{agent}**")

        st.markdown("---")  # Add a separator between rows

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
            # Call the function to display the data
            show_feedback_analysis(st.session_state.feedback_data)

if __name__ == "__main__":
    main()
