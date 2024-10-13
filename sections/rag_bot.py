import streamlit as st  # type: ignore

def rag_bot_component():
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "AI Skills Overview",
        "Quick Wins",
        "Inefficiencies Analysis",
        "Workflow Improvement",
        "Patient Feedback"
    ])

    with tab1:
        st.header("AI Skills Overview")
        st.image("assets/agents/ragbot1.png", caption="AI Skills Overview", use_column_width=True)
    with tab2:
        st.header("Quick Wins for Patient Satisfaction")
        st.image("assets/agents/ragbot2.png", caption="Quick Wins", use_column_width=True)
    with tab3:
        st.header("Inefficiencies Analysis")
        st.image("assets/agents/ragbot3.png", caption="Inefficiencies Analysis", use_column_width=True)
    with tab4:
        st.header("Workflow Improvement Advice")
        st.image("assets/agents/ragbot4.png", caption="Workflow Improvement", use_column_width=True)
    with tab5:
        st.header("Patient Feedback Display")
        st.image("assets/agents/ragbot5.png", caption="Patient Feedback", use_column_width=True)

