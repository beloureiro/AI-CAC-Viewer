import streamlit as st
import os
import json

# Caminho da pasta onde os arquivos JSON estão armazenados
DATA_DIR = "data_reports_json"

# Função para carregar os arquivos JSON
def load_json_files(data_folder):
    data = []
    if not os.path.exists(data_folder):
        st.error(f"A pasta {data_folder} não existe. Verifique o caminho.")
        return data

    # Carregar os arquivos JSON da pasta
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data.append(json.load(f))
            except json.JSONDecodeError:
                st.error(f"Erro ao decodificar o arquivo: {file_name}")
    return data

# Função para formatar o ID do feedback
def format_feedback_id(feedback_id):
    parts = feedback_id.split('_')
    if len(parts) > 1:
        return f"Feedback {parts[-1]}"
    return feedback_id

# Função para exibir os dados do agente
def get_agent_data(feedback_data, agent):
    for entry in feedback_data.get("agents", []):
        if entry["agent_name"] == agent:
            return entry.get("response", {})
    return {}

# Função para exibir a análise do feedback
def show_feedback_analysis(feedback_list):
    st.header("Patient Feedback Analysis")

    if not feedback_list:
        st.error("No feedback data available. Please check the data source.")
        return

    # Criar uma lista de feedback IDs para o selectbox
    feedback_options = [f"Feedback {i+1}" for i in range(len(feedback_list))]
    selected_feedback_idx = st.selectbox("Select Feedback", range(len(feedback_list)), format_func=lambda x: feedback_options[x])
    
    feedback_data = feedback_list[selected_feedback_idx]

    # Exibir o feedback do paciente
    st.subheader("Patient Feedback")
    patient_feedback = feedback_data.get("patient_feedback")
    if patient_feedback:
        st.text_area("Feedback", patient_feedback, height=150)
    else:
        st.warning("Patient feedback not found in the data.")

    # Exibir os relatórios dos agentes
    st.subheader("Agent Reports")
    
    agents = [entry["agent_name"] for entry in feedback_data.get("agents", [])]

    for i, agent in enumerate(agents):
        col1, col2 = st.columns(2)
        agent_data = get_agent_data(feedback_data, agent)
        
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

# Função principal
def main():
    st.title("AI Clinical Advisory Crew")
    
    # Carregar os dados JSON
    feedback_list = load_json_files(DATA_DIR)
    
    # Exibir a análise do feedback
    show_feedback_analysis(feedback_list)

if __name__ == "__main__":
    main()
