import streamlit as st
import os
import json
import pandas as pd
import re

# Define the field equivalence dictionary
FIELD_EQUIVALENCE = {
    'Sentiment_Patient_Experience_Expert': 'Sentiment',
    'Emotional_Intensity_Patient_Experience_Expert': 'Emotional Intensity',
    'Urgency_Level_Patient_Experience_Expert': 'Urgency Level',
    'Key_Issues_Patient_Experience_Expert': 'Key Issues',
    'Patient_Journey_Health_IT_Process_Expert': 'Patient Journey',
    'Inefficiencies_Healthcare_Process_Health_IT_Process_Expert': 'Inefficiencies in Healthcare Process',
    'Improvement_Suggestions_Healthcare_Process_Health_IT_Process_Expert': 'Improvement Suggestions',
    'Emotional_State_Clinical_Psychologist': 'Emotional State',
    'Support_Strategy_Clinical_Psychologist': 'Support Strategy',
    'Suggested_Approach_Clinical_Psychologist': 'Suggested Approach',
    'Communication_Quality_Communication_Expert': 'Communication Quality',
    'Issues_Identified_Communication_Expert': 'Issues Identified',
    'Suggested_Improvements_Communication_Expert': 'Suggested Improvements',
    'Final_Recommendation_Communication_Expert': 'Final Recommendation',
    'Key_Issues_Manager_and_Advisor': 'Key Issues',
    'Recommendations_Manager_and_Advisor': 'Recommendations'
}


def load_json_files(data_folder):
    data = []

    # Verifica se a pasta existe
    if not os.path.exists(data_folder):
        st.error(f"The folder '{data_folder}' does not exist.")
        return data

    # Lista todos os arquivos na pasta
    files = os.listdir(data_folder)
    if not files:
        st.warning(f"The folder '{data_folder}' is empty.")
        return data

    # Processa arquivos JSON
    for file_name in files:
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Adiciona conteúdo do arquivo JSON à lista de dados
                    data.append({"name": file_name, "content": json.load(f)})
            except UnicodeDecodeError:
                st.error(f"Error decoding file: {file_name}. Please check the encoding.")
            except json.JSONDecodeError:
                st.error(f"Error parsing JSON file: {file_name}. Please check if it's a valid JSON file.")
    
    # Verifica se algum dado foi carregado
    if not data:
        st.warning(f"No valid JSON files found in the folder '{data_folder}'.")
    
    return data


def read_txt_report(report_name):
    txt_file_path = os.path.join('data_reports', f"{report_name}.txt")
    if os.path.exists(txt_file_path):
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "TXT report not found."

def download_txt_report(report_name):
    txt_content = read_txt_report(report_name)
    return st.download_button(
        label="Download TXT Report",
        data=txt_content,
        file_name=f"{report_name}.txt",
        mime="text/plain"
    )

def convert_time_to_seconds(time_str):
    minutes = 0
    seconds = 0
    time_parts = re.findall(r'\d+\s+\w+', time_str)
    for part in time_parts:
        value, unit = part.split()
        if 'minute' in unit:
            minutes = int(value)
        elif 'second' in unit:
            seconds = int(value)
    return minutes * 60 + seconds

def display_feedback(feedback, report_name, agents_data, total_execution_time):
    st.subheader("Key Performance Indicators")
    patient_expert = next((agent for agent in agents_data if agent['agent_name'] == 'Patient Experience Expert'), None)
    if patient_expert:
        kpi_data = patient_expert['response']
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Sentiment", kpi_data.get('Sentiment_Patient_Experience_Expert', 'N/A'))
        with col2:
            st.metric("Emotional Intensity", kpi_data.get('Emotional_Intensity_Patient_Experience_Expert', 'N/A'))
        with col3:
            st.metric("Urgency Level", kpi_data.get('Urgency_Level_Patient_Experience_Expert', 'N/A'))
        with col4:
            execution_time_seconds = convert_time_to_seconds(total_execution_time)
            st.metric("Crew Performance", f"{execution_time_seconds:.2f}s")
    else:
        st.warning("Patient Experience Expert data not available")

    st.subheader("Patient Feedback")
    st.text_area("Feedback", feedback, height=150)

def display_agent_reports(data, mode, selected_item):
    st.subheader("Agent Reports")
    if mode == "agent":
        for feedback in data:
            with st.expander(f"Feedback: {feedback['name']}"):
                agent_report = next((agent for agent in feedback['content']['agents'] if agent['agent_name'] == selected_item), None)
                if agent_report:
                    display_name = "Health & IT Process Expert" if agent_report['agent_name'].startswith("Health & IT Process Expert") else agent_report['agent_name']
                    st.markdown(f"<h3 style='color: #1b9e4b;'>{display_name}</h3>", unsafe_allow_html=True)
                    for key, value in agent_report['response'].items():
                        display_key = FIELD_EQUIVALENCE.get(key, key)
                        st.markdown(f"<strong style='color: #e0e0e0;'>{display_key}:</strong>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color: #b0b0b0; margin-left: 20px;'>{value}</p>", unsafe_allow_html=True)
                else:
                    st.write("No report available for this feedback.")
    elif mode == "feedback":
        for agent in data[selected_item]['content']['agents']:
            display_name = "Health & IT Process Expert" if agent['agent_name'].startswith("Health & IT Process Expert") else agent['agent_name']
            with st.expander(f"Agent: {display_name}"):
                st.markdown(f"<h3 style='color: #1b9e4b;'>{display_name}</h3>", unsafe_allow_html=True)
                for key, value in agent['response'].items():
                    display_key = FIELD_EQUIVALENCE.get(key, key)
                    st.markdown(f"<strong style='color: #e0e0e0;'>{display_key}:</strong>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color: #b0b0b0; margin-left: 20px;'>{value}</p>", unsafe_allow_html=True)

def display_table_view(data):
    st.subheader("All Feedback and Agent Reports")
    
    table_data = []
    for feedback in data:
        feedback_name = feedback['name']
        patient_feedback = feedback['content'].get('patient_feedback', 'No feedback available.')
        
        for agent in feedback['content']['agents']:
            agent_name = agent['agent_name']
            display_name = "Health & IT Process Expert" if agent_name.startswith("Health & IT Process Expert") else agent_name
            for key, value in agent['response'].items():
                display_key = FIELD_EQUIVALENCE.get(key, key)
                table_data.append({
                    "Feedback": feedback_name,
                    "Patient Feedback": patient_feedback,
                    "Agent": display_name,
                    "Field": display_key,
                    "Value": value
                })
    
    df = pd.DataFrame(table_data)
    
    st.subheader("Filters")
    filter_option = st.radio("Filter by:", ("Feedback", "Agent"), key="table_view_filter_radio")  # Adicionado chave única
    
    if df.empty:
        st.warning("No data available for filtering.")
        return
    
    if filter_option == "Feedback":
        selected_feedback = st.selectbox("Select Feedback", options=df["Feedback"].unique(), key="table_view_feedback_selectbox")  # Adicionado chave única
        filtered_df = df[df["Feedback"] == selected_feedback]
    else:
        selected_agent = st.selectbox("Select Agent", options=df["Agent"].unique(), key="table_view_agent_selectbox")  # Adicionado chave única
        filtered_df = df[df["Agent"] == selected_agent]
    
    st.dataframe(filtered_df)

def display_complete_txt_report(data):
    st.subheader("Complete Report (TXT)")
    if not data:
        st.warning("No reports available.")
        return
    
    selected_feedback = st.selectbox("Select a feedback", options=[file['name'] for file in data], key="complete_report_feedback_selectbox")  # Adicionado chave única
    selected_data = next((file for file in data if file['name'] == selected_feedback), None)
    if selected_data:
        report_name = os.path.splitext(selected_data['name'])[0]
        txt_report = read_txt_report(report_name)
        st.text_area("TXT Report", txt_report, height=600)
        download_txt_report(report_name)
    else:
        st.error("Selected feedback data not found.")

def patient_feedback_analyzer():
    # Title and introduction
    st.markdown('''
        <h1 style="text-align: center;">
            <span style="color: #1b9e4b; font-style: italic;">AI</span> 
            <span style="color: white;">Clinical Advisory</span> 
            <span style="color: #1b9e4b; font-style: italic;">Crew</span>
        </h1>
    ''', unsafe_allow_html=True)
    
    # Centraliza o sub-título
    st.markdown("<h2 style='text-align: center;'>Patient Feedback Analysis</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Adiciona o disclaimer
    st.markdown('''
    <p><strong>Disclaimer</strong></p>
    <p>The analyses in this report were conducted by different LLM models in <em>training mode</em>, which take patient feedback as absolute truth. Feedback reflects the patient's individual perception and, in some cases, may not capture the full complexity of the situation, including institutional and contextual factors.</p>
    <p>AI Clinical Advisory Crew framework, <em>beyond</em> providing technical analyses, acts as a strategic driver, steering managerial decisions across various operational areas.<br>
    <em>The reader is responsible for validating the feasibility of the suggested actions and their alignment with stakeholder objectives.</em></p>
    ''', unsafe_allow_html=True)
    st.markdown("---")
    
    # Carrega os dados da pasta data_reports_json
    data = load_json_files('data_reports_json')

    # Verifica se os dados estão vazios
    if not data:
        st.error("No feedback data available. Please check if the 'data_reports_json' folder exists and contains valid JSON files.")
        # Remover o retorno de None para continuar o fluxo mesmo que falte dados
        return  # Apenas parar a execução, mas continuar o fluxo geral sem retornar None

    # Mostra opções de visualização (essa parte já está correta)
    st.subheader("View Options")
    view_mode = st.radio(
        "Select view mode:", 
        ("By Feedback", "By Agent", "Table View", "Complete Report (TXT)"), 
        index=0, 
        key="feedback_analysis_view_mode_radio"
    )

    # Visualização: Relatório completo (TXT)
    if view_mode == "Complete Report (TXT)":
        st.write("Displaying complete TXT report")  # Depuração
        display_complete_txt_report(data)

    # Visualização: Por Feedback
    elif view_mode == "By Feedback":
        st.write("Displaying feedback-based view")  # Depuração
        selected_feedback = st.selectbox(
            "Select a feedback", 
            options=[file['name'] for file in data], 
            key="feedback_analysis_feedback_selectbox"
        )
        selected_data = next((file for file in data if file['name'] == selected_feedback), None)
        
        # Verifica se os dados do feedback selecionado foram encontrados
        if selected_data:
            report_name = os.path.splitext(selected_data['name'])[0]
            total_execution_time = selected_data['content'].get('total_execution_time', '0')
            
            # Exibe os dados de feedback
            st.write(f"Selected feedback: {selected_feedback}")  # Depuração
            display_feedback(
                selected_data['content'].get('patient_feedback', 'No feedback available.'),
                report_name,
                selected_data['content'].get('agents', []),
                total_execution_time
            )
            display_agent_reports(data, "feedback", data.index(selected_data))
        else:
            st.error("Feedback data not found.")
    
    # Visualização: Por Agente
    elif view_mode == "By Agent":
        st.write("Displaying agent-based view")  # Depuração
        all_agents = list(set([agent['agent_name'] for file in data for agent in file['content']['agents']]))

        # Verifica se há agentes disponíveis
        if not all_agents:
            st.error("No agents data available.")
            return

        display_agents = [
            "Health & IT Process Expert" if agent.startswith("Health & IT Process Expert") else agent 
            for agent in all_agents
        ]

        agent_name_mapping = {display: original for display, original in zip(display_agents, all_agents)}

        selected_agent_display = st.selectbox(
            "Select an agent", 
            options=display_agents, 
            key="feedback_analysis_agent_selectbox"
        )
        selected_agent = agent_name_mapping[selected_agent_display]

        display_agent_reports(data, "agent", selected_agent)
    
    # Visualização: Tabela
    else:
        st.write("Displaying table view")  # Depuração
        display_table_view(data)
    
    st.markdown("<hr style='border-top: 1px solid #ddd;'>", unsafe_allow_html=True)
  
    # Add the powered by Inmotion link
    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)