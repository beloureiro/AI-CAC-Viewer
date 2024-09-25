import streamlit as st
from config import AGENT_DESCRIPTIONS, AI_MODELS

def show_ai_agents():
    st.markdown('<h1 style="color: #1b9e4b; font-style: italic;">AI</span> Clinical Advisory <span style="color: #1b9e4b; font-style: italic;">Crew</span></h1>', unsafe_allow_html=True)
    st.header("AI Agents")
    
    agents = list(AGENT_DESCRIPTIONS.keys())
    
    for i, agent_name in enumerate(agents):
        col1, col2 = st.columns(2)
        if i % 2 == 0:
            with col1:
                st.markdown(f"**[Image Placeholder for {agent_name}]**")
            with col2:
                st.subheader(agent_name)
                st.write(AGENT_DESCRIPTIONS[agent_name])
        else:
            with col1:
                st.subheader(agent_name)
                st.write(AGENT_DESCRIPTIONS[agent_name])
            with col2:
                st.markdown(f"**[Image Placeholder for {agent_name}]**")
    
    st.markdown("---")  # Add a horizontal line
    show_ai_models()

def show_ai_models():
    st.header("AI Models")
    
    col1, col2 = st.columns(2)
    for i, (model, description) in enumerate(AI_MODELS.items()):
        with (col1 if i % 2 == 0 else col2).expander(model):
            st.write(description)
