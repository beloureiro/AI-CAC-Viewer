import streamlit as st
import pandas as pd
from config import AGENTS

def format_feedback_id(feedback_id):
    parts = feedback_id.split('_')
    if len(parts) > 1:
        return f"Feedback {parts[-1]}"
    return feedback_id

def get_agent_data(df, feedback_id, agent):
    if df is not None and not df.empty:
        feedback_row = df[df['feedback_id'] == feedback_id].iloc[0]
        agent_data = feedback_row.get(agent.lower().replace(' ', '_'), {})
        if isinstance(agent_data, dict):
            return agent_data
        elif isinstance(agent_data, str):
            return {"Report": agent_data}
    return {}

def show_feedback_analysis(df):
    st.header("Patient Feedback Analysis")

    if df is None or df.empty:
        st.error("No feedback data available. Please check the data source.")
        return

    feedback_options = sorted(df['feedback_id'].unique())
    selected_feedback = st.selectbox("Select Feedback", feedback_options, format_func=format_feedback_id)

    try:
        feedback_data = df[df['feedback_id'] == selected_feedback].iloc[0]
    except IndexError:
        st.error(f"No data found for selected feedback: {selected_feedback}")
        return

    st.subheader("Patient Feedback")
    patient_feedback = feedback_data.get("patient_feedback") or feedback_data.get("feedback")
    if patient_feedback:
        st.text_area("Feedback", patient_feedback, height=150)
    else:
        st.warning("Patient feedback not found in the data.")

    st.subheader("Agent Reports")
    
    for i, agent in enumerate(AGENTS):
        col1, col2 = st.columns(2)
        agent_data = get_agent_data(df, selected_feedback, agent)
        
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

if __name__ == "__main__":
    show_feedback_analysis(None)
