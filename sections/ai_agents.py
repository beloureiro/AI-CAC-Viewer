import streamlit as st
import os
from utils.config import AGENT_DESCRIPTIONS, AI_MODELS

def show_ai_agents():
    # Title and introduction
    st.markdown('''
        <h1 style="text-align: center;">
            <span style="color: #1b9e4b; font-style: italic;">AI</span> 
            <span style="color: white;">Clinical Advisory</span> 
            <span style="color: #1b9e4b; font-style: italic;">Crew</span>
        </h1>
    ''', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center;">Meet our team of AI experts, ready to transform the healthcare experience.</p>', unsafe_allow_html=True)
    st.markdown("---")  # Horizontal line
    agents = list(AGENT_DESCRIPTIONS.keys())
    image_folder = 'assets/agents'  # Folder where the images are stored

    # Mapping agent names to image file names
    image_name_mapping = {
        "Clinical Psychologist (OpenHermes Model)": "ClinicalPsychologist.jpeg",
        "Communication Expert (Mistral Model)": "CommunicationExpert.jpeg",
        "Data Analyst (LLaVA Model)": "DataAnalyst.jpeg",
        "Health & IT Process Expert (Gemma Model)": "HealthAndITProcessExpert.jpeg",
        "Manager and Advisor (Qwen Model)": "ManagerAndAdvisor.jpeg",
        "Output Consistency Agent (LLaMA Model)": "OutputConsistencyAgent.jpeg",
        "Patient Experience Expert (Phi Model)": "PatientExperienceExpert.jpeg"
    }

    # Display agents in two columns
    for i in range(0, len(agents), 2):
        cols = st.columns(2)  # Create two columns for each row

        for j, col in enumerate(cols):
            if i + j < len(agents):  # Check if there are still agents in the list
                agent_name = agents[i + j]
                image_name = image_name_mapping.get(agent_name)
                image_path = os.path.join(image_folder, image_name) if image_name else None

                with col:
                    # Display the image with a width of 400 pixels
                    if image_path and os.path.exists(image_path):
                        st.image(image_path, width=400, caption=f"{agent_name}")  # Set the image width
                    else:
                        st.error(f"Image not found for agent: {agent_name}")

                    # Agent descriptive text
                    st.subheader(agent_name)
                    st.markdown(f"<div style='text-align: justify;'>{AGENT_DESCRIPTIONS[agent_name]}</div>", unsafe_allow_html=True)

        # Add a separator between agent rows
        st.markdown("<hr style='border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# Call to display the agents
# Remove this line if it's causing issues
# show_ai_agents()
