import streamlit as st  # type: ignore
from sections.feedback_analysis import patient_feedback_analyzer
from sections.overview import show_overview
from sections.use_case import ai_clinical_advisory_crew_tab  # Import the new function
from sections.ai_crew import ai_crew_component  # Import the new function
from sections.new_bot import new_bot_component  # Import the new function

def main():
    """
    Main function to set up the Streamlit application layout and sidebar navigation.
    Initializes the application configuration, applies custom CSS, 
    and manages navigation between different sections based on sidebar selections.
    """
    st.set_page_config(page_title="AI Clinical Advisory Crew", layout="wide")
    
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #0e1525;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("""
        <div style='border: 2px solid #1c2333; padding: 5px; border-radius: 10px;'>
            <h2 style="text-align: center; font-size: 17px;">
                <span style="color: #1b9e4b; font-style: italic;">AI</span> 
                <span style="color: white;">Clinical Advisory</span> 
                <span style="color: #1b9e4b; font-style: italic;">Crew</span>
            </h2>
        </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    tab = st.sidebar.radio("Select a Tab", ["Overview", "How It Works", "AI Agents", "Feedback Analysis", "AI-Skills Advisor"], index=0)
    
    if tab == "Overview":
        show_overview()
    elif tab == "How It Works":
        ai_clinical_advisory_crew_tab()
    elif tab == "AI Agents":
        ai_crew_component()
    elif tab == "Feedback Analysis":
        analyzer = patient_feedback_analyzer()
        
        if analyzer is None:
            st.stop()

        view_mode = st.radio("Select view mode:", ("By Feedback", "By Agent", "Table View", "Complete Report (TXT)"), index=0, key="view_mode_radio")
        
        if view_mode == "By Feedback":
            selected_feedback = st.selectbox("Select a feedback", options=analyzer.get_feedback_list(), key="feedback_selectbox")
            feedback_data = analyzer.get_feedback_data(selected_feedback)
            
            if feedback_data:
                display_feedback(feedback_data, analyzer)
                display_agent_reports(analyzer, "feedback", analyzer.get_feedback_list().index(selected_feedback))
            else:
                st.error("Selected feedback data not found.")
        elif view_mode == "By Agent":
            selected_agent = st.selectbox("Select an agent", options=analyzer.get_agent_list(), key="agent_selectbox")
            display_agent_reports(analyzer, "agent", selected_agent)
        elif view_mode == "Table View":
            display_table_view(analyzer)
        elif view_mode == "Complete Report (TXT)":
            display_complete_txt_report(analyzer)

    elif tab == "AI-Skills Advisor":
        new_bot_component()

def display_feedback(feedback_data, analyzer):
    """
    Displays patient feedback and associated Key Performance Indicators (KPIs).
    
    Parameters:
        feedback_data (dict): Data containing the patient's feedback and other details.
        analyzer: An instance of the feedback analyzer with methods to retrieve additional data.
    """
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

def display_agent_reports(analyzer, mode, selected_item):
    """
    Displays reports for agents based on the selected feedback or agent.
    
    Parameters:
        analyzer: An instance of the feedback analyzer with methods to retrieve agent reports.
        mode (str): Mode of selection, either "feedback" or "agent".
        selected_item: The specific feedback or agent selected by the user.
    """
    st.subheader("Agent Reports")
    reports = analyzer.get_agent_reports(mode, selected_item)
    
    for report in reports:
        with st.expander(f"Agent: {report['agent_name']}" if mode == "feedback" else f"Feedback: {report['feedback_name']}"):
            for key, value in report['agent_report']['response'].items():
                st.write(f"{key}: {value}")

def display_table_view(analyzer):
    """
    Displays a table view of all feedback and agent reports.
    
    Parameters:
        analyzer: An instance of the feedback analyzer with methods to retrieve data for the table view.
    """
    st.subheader("All Feedback and Agent Reports")
    df = analyzer.get_table_data()
    st.dataframe(df)

def display_complete_txt_report(analyzer):
    """
    Displays and allows download of a complete feedback report in TXT format.
    
    Parameters:
        analyzer: An instance of the feedback analyzer with methods to retrieve the complete TXT report.
    """
    st.subheader("Complete Report (TXT)")
    selected_feedback = st.selectbox("Select a feedback", options=analyzer.get_feedback_list(), key="complete_report_selectbox")
    report_name = selected_feedback.split('.')[0]
    txt_report = analyzer.get_txt_report(report_name)
    st.text_area("TXT Report", txt_report, height=600)
    st.download_button("Download TXT Report", txt_report, file_name=f"{report_name}.txt")

if __name__ == "__main__":
    main()


# to run the app: streamlit run main.py