import streamlit as st

def show_overview():
    st.markdown("""
    <div style='background-color: #1E2129; padding: 20px; border-radius: 10px;'>
    <h1><span style="color: #1b9e4b; font-style: italic;">AI</span><span style="color: #FFFFFF;"> Clinical Advisory </span><span style="color: #1b9e4b; font-style: italic;">Crew</span></h1>
    <p>An advanced and flexible system designed to transform and elevate the patient experience in healthcare. This project brings together a team of specialized AI agents, each with a unique role in analyzing patient feedback, improving healthcare workflows, assessing emotional states, and delivering actionable recommendations for communication and operational improvements.</p>
    <p>At the heart of this system lies its dynamic flexibility: it navigates across a suite of <strong>Large Language Models (LLMs)</strong> to determine the optimal AI configuration for each specific task. By utilizing models like Meta's LLaMA, NousResearch's Hermes, Microsoft's Phi, and others, the system continuously tests and refines outputs to ensure that the best-suited AI crew is selected to address the task at hand.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    Key Benefits:
    - Operates using local LLMs, ensuring maximum data security
    - Processes all information internally, without reliance on third-party APIs
    - Delivers significant cost savings by eliminating the need for external API usage
    - Maintains full control over data privacy
    """)
