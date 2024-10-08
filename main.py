import streamlit as st  # type: ignore
from sections.feedback_analysis import patient_feedback_analyzer
from sections.overview import show_overview
from sections.use_case import ai_clinical_advisory_crew_tab  # Importa a nova função
from sections.ai_crew import ai_crew_component  # Importa a nova função

def main():
    # Configura a página (deve ser a primeira chamada do Streamlit)
    st.set_page_config(page_title="AI Clinical Advisory Crew", layout="wide")
    
    # Custom CSS para alterar a cor do fundo do sidebar
    st.markdown(
        """
        <style>
        /* Custom sidebar background color */
        [data-testid="stSidebar"] {
            background-color: #0e1525;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Adiciona o logotipo e linha de separação
    st.sidebar.markdown("""
        <div style='background-color: #0e1117; padding: 5px; border-radius: 10px;'>
            <h2 style="text-align: center; font-size: 17px;">
                <span style="color: #1b9e4b; font-style: italic;">AI</span> 
                <span style="color: white;">Clinical Advisory</span> 
                <span style="color: #1b9e4b; font-style: italic;">Crew</span>
            </h2>
        </div>
    """, unsafe_allow_html=True)


    
    st.sidebar.markdown("---")  # Adiciona uma linha de separação após o logotipo

    # Menu lateral para navegação
    tab = st.sidebar.radio("Select a Tab", ["Overview", "How It Works", "AI Agents", "Feedback Analysis"], index=0)  # Reordenado
    
    # Navegação entre as seções
    if tab == "Overview":
        show_overview()  # A página Overview será exibida por padrão
    elif tab == "How It Works":  # Alterado o nome da condição
        ai_clinical_advisory_crew_tab()  # Chama a função da nova aba
    elif tab == "AI Agents":
        ai_crew_component()  # Chama a função da nova aba
    elif tab == "Feedback Analysis":
          
        # Instancia o analisador de feedback
        analyzer = patient_feedback_analyzer()
        
        # Verifica se o analyzer não é None - Se necessário, apenas continue o fluxo sem exibir erro
        if analyzer is None:
            st.stop()  # Para a execução da página se realmente for necessário

        # Escolha de modo de visualização
        view_mode = st.radio("Select view mode:", ("By Feedback", "By Agent", "Table View", "Complete Report (TXT)"), index=0, key="view_mode_radio")
        
        # Modo de visualização: Por Feedback
        if view_mode == "By Feedback":
            selected_feedback = st.selectbox("Select a feedback", options=analyzer.get_feedback_list(), key="feedback_selectbox")
            feedback_data = analyzer.get_feedback_data(selected_feedback)
            
            if feedback_data:
                display_feedback(feedback_data, analyzer)
                display_agent_reports(analyzer, "feedback", analyzer.get_feedback_list().index(selected_feedback))
            else:
                st.error("Selected feedback data not found.")
                
        # Modo de visualização: Por Agente
        elif view_mode == "By Agent":
            selected_agent = st.selectbox("Select an agent", options=analyzer.get_agent_list(), key="agent_selectbox")
            display_agent_reports(analyzer, "agent", selected_agent)
        
        # Modo de visualização: Tabela
        elif view_mode == "Table View":
            display_table_view(analyzer)
        
        # Modo de visualização: Relatório completo (TXT)
        elif view_mode == "Complete Report (TXT)":
            display_complete_txt_report(analyzer)

    elif tab == "Plans & Use Case":  # Alterado o nome da condição
        ai_clinical_advisory_crew_tab()  # Chama a função da nova aba

# Função para exibir feedback e KPIs
def display_feedback(feedback_data, analyzer):
    st.subheader("Patient Feedback")
    st.text_area("Feedback", feedback_data['content'].get('patient_feedback', 'No feedback available.'), height=150)
    
    st.subheader("Key Performance Indicators")
    patient_expert = analyzer.get_patient_expert_data(feedback_data['content'].get('agents', []))
    kpi_data = analyzer.get_kpi_data(patient_expert)
    
    if kpi_data:
        col1, col2, col3 = st.columns(3)
        col1.metric("Sentiment", kpi_data.get('Sentiment', 'N/A'))
        col2.metric("Emotional Intensity", kpi_data.get('Emotional Intensity', 'N/A'))
        col3.metric("Urgency Level", kpi_data.get('Urgency Level', 'N/A'))

# Função para exibir relatórios dos agentes
def display_agent_reports(analyzer, mode, selected_item):
    st.subheader("Agent Reports")
    reports = analyzer.get_agent_reports(mode, selected_item)
    
    # Exibe relatórios expandidos
    for report in reports:
        with st.expander(f"Agent: {report['agent_name']}" if mode == "feedback" else f"Feedback: {report['feedback_name']}"):
            for key, value in report['agent_report']['response'].items():
                st.write(f"{key}: {value}")

# Função para exibir a visão em tabela
def display_table_view(analyzer):
    st.subheader("All Feedback and Agent Reports")
    df = analyzer.get_table_data()  # Obtém a tabela de dados
    st.dataframe(df)

# Função para exibir o relatório completo (TXT)
def display_complete_txt_report(analyzer):
    st.subheader("Complete Report (TXT)")
    selected_feedback = st.selectbox("Select a feedback", options=analyzer.get_feedback_list(), key="complete_report_selectbox")
    report_name = selected_feedback.split('.')[0]  # Remove extensão do nome do arquivo
    txt_report = analyzer.get_txt_report(report_name)  # Obtém o conteúdo do relatório TXT
    st.text_area("TXT Report", txt_report, height=600)
    st.download_button("Download TXT Report", txt_report, file_name=f"{report_name}.txt")

if __name__ == "__main__":
    main()

# to run the app: streamlit run main.py
