import streamlit as st
import os
from utils.config import AGENT_DESCRIPTIONS, AI_MODELS

def show_ai_agents():
    # Título estilizado com "AI" e "Crew" em verde e as demais palavras em branco
    st.markdown('''
        <h1 style="text-align: center;">
            <span style="color: #1b9e4b; font-style: italic;">AI</span> 
            <span style="color: white;">Clinical Advisory</span> 
            <span style="color: #1b9e4b; font-style: italic;">Crew</span>
        </h1>
    ''', unsafe_allow_html=True)
    
    # Frase introdutória
    st.markdown('<p style="text-align: center;">Meet our team of AI experts, ready to transform the healthcare experience.</p>', unsafe_allow_html=True)
    
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

    # Apresentar dois agentes por linha
    for i in range(0, len(agents), 2):
        cols = st.columns(2)  # Cria duas colunas para cada linha

        for j, col in enumerate(cols):
            if i + j < len(agents):  # Verifica se ainda há agentes na lista
                agent_name = agents[i + j]
                image_name = image_name_mapping.get(agent_name)
                image_path = os.path.join(image_folder, image_name) if image_name else None

                with col:
                    # Exibindo a imagem
                    if image_path and os.path.exists(image_path):
                        st.image(image_path, use_column_width=True, caption=f"{agent_name}")
                    else:
                        st.error(f"Image not found for agent: {agent_name}")

                    # Texto descritivo do agente
                    st.subheader(agent_name)
                    st.markdown(f"<div style='text-align: justify;'>{AGENT_DESCRIPTIONS[agent_name]}</div>", unsafe_allow_html=True)

        # Adiciona um separador entre as linhas de agentes
        st.markdown("<hr style='border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# Chamada para exibir os agentes
show_ai_agents()
