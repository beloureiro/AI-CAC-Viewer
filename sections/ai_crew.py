import streamlit as st # type: ignore
from PIL import Image # type: ignore
import os

def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
        return None

def ai_crew_component():
    st.markdown("""
        <div style='background-color: #0e1525; padding: 20px; border-radius: 10px;'>
            <h1><span style="color: #1b9e4b;"><i>AI</i></span> Clinical Advisory <span style="color: #1b9e4b;"><i>Crew</i></span></h1>
            <p>Meet our team of AI experts, ready to transform the healthcare experience.</p>
        </div>
    """, unsafe_allow_html=True)

    # Custom CSS for the text input box
    st.markdown("""
        <style>
        /* Customizing the input box for 'Search for AI agents' */
        input {
            background-color: #0e1117 !important;
            color: white !important;
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #1b9e4b;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add search functionality with placeholder
    search_query = st.text_input('Search for AI agents:', '', placeholder='Enter agent name')

    # Define the AI agents and their descriptions
    ai_agents = [
        {
            "name": "Patient Experience Expert (Phi Model 3.8b)",
            "image": "assets/agents/PatientExperienceExpert.png",
            "description": "I'm the Patient Experience Expert. My job is to analyze patient feedback, pinpoint key issues, gauge emotional intensity, and assess the urgency of the concerns. I run on Microsoft's Phi-3.5 Mini, a 3.8 billion parameter model, which excels at reasoning and language understanding. My goal is to turn patient feedback into actionable insights that improve the overall healthcare experience. I look forward to enhancing your services."
        },
        {
            "name": "Patient Experience Expert (Llama Model 8b)",
            "image": "assets/agents/PatientExperienceExpert2.png",
            "description": "I'm the Patient Experience Expert. My job is to analyze patient feedback, pinpoint key issues, gauge emotional intensity, and assess the urgency of the concerns. I operate on Meta's Llama 3.1, an advanced 8 billion parameter model optimized for instruction-based tasks. This model excels in understanding and generating human-like language responses, while the Q8_0 quantization ensures high-quality performance with optimized memory usage. My goal is to turn patient feedback into actionable insights that enhance the overall healthcare experience. I'm here to help your team improve patient satisfaction and outcomes."
        },

        {
            "name": "Health & IT Process Expert (Gemma Model 9b)",
            "image": "assets/agents/HealthAndITProcessExpert.jpeg",
            "description": "I'm the Health & IT Process Expert. My role is to map out the entire patient journey, using BPMN (Business Process Model and Notation) to spot inefficiencies and recommend improvements that benefit all stakeholders. Powered by Google's Gemma 2, a 9 billion parameter model, I strike a perfect balance between performance and efficiency. My mission is to streamline healthcare workflows and integrate better processes and technology. I'm confident you'll appreciate the results I deliver."
        },
        {
            "name": "Health & IT Process Expert (Llama 3.2 Model)",
            "image": "assets/agents/HealthAndITProcessExpert2.jpeg",
            "description": "I'm the Health & IT Process Expert. My role is to map out the entire patient journey using BPMN (Business Process Model and Notation) to identify inefficiencies and suggest process improvements. I operate using Meta's Llama 3.2, a cutting-edge model with 3 billion parameters. The Q5_K_S quantization ensures optimal memory efficiency without sacrificing performance. My goal is to streamline healthcare workflows and integrate advanced technologies to enhance patient care and operational efficiency. I am confident that my insights will help you achieve tangible improvements in healthcare delivery."
        },
        {
            "name": "Clinical Psychologist (OpenHermes Model 7b)",
            "image": "assets/agents/ClinicalPsychologist.jpeg",
            "description": "I'm the Clinical Psychologist. I specialize in analyzing patients' emotional states based on their feedback and crafting personalized psychological support strategies. I leverage the OpenHermes model by NousResearch, which is designed for advanced context understanding and coherent response generation. My aim is to provide effective emotional support, helping patients cope with stressful situations in a thoughtful and empathetic way. I'm here to ensure patients feel heard and supported."
        },
        {
            "name": "Clinical Psychologist (Phi Model 3.8b)",
            "image": "assets/agents/ClinicalPsychologist2.png",
            "description": "I'm the Clinical Psychologist. I specialize in analyzing patients' emotional states based on their feedback and crafting personalized psychological support strategies. I operate using Microsoft's Phi 3.5 Mini, a 3.8 billion parameter model that excels in reasoning and emotional understanding. The Phi 3.5 model is optimized with Q8_0 quantization, offering high-quality performance while efficiently using memory. My focus is to provide empathetic, effective emotional support, helping patients manage stress and improve their mental well-being. I'm here to ensure patients feel heard, valued, and supported."
        },
        {
            "name": "Communication Expert (Mistral Model 12b)",
            "image": "assets/agents/CommunicationExpert.jpeg",
            "description": "I'm the Communication Expert. My expertise lies in evaluating the quality of communication between healthcare professionals and patients, identifying communication gaps, and suggesting improvements. I operate on Mistral NeMo, developed by Mistral AI and NVIDIA, a 12 billion parameter model with an impressive 128k token context window. This allows me to dive deep into interactions and find ways to improve clarity and empathy in communication. My goal is to enhance communication strategies that leave patients feeling understood and valued."
        },
        {
            "name": "Communication Expert (Gemma Model 9b)",
            "image": "assets/agents/CommunicationExpert2.jpeg",
            "description": "I'm the Communication Expert. My expertise lies in evaluating the quality of communication between healthcare professionals and patients, identifying communication gaps, and suggesting improvements. I operate on the Gemma2 model, a state-of-the-art 9 billion parameter system developed by Google. Using the highly efficient quantization format Q5_K_S, I balance precision and memory usage to deliver in-depth analysis of conversations. This model's training on a diverse dataset allows me to assess interactions from various angles, including empathy, clarity, and professionalism. My goal is to enhance communication strategies that foster understanding and trust between professionals and patients."
        },
        {
            "name": "Manager and Advisor (Qwen Model 7b)",
            "image": "assets/agents/ManagerAndAdvisor.jpeg",
            "description": "I'm the Manager and Advisor. I consolidate feedback from various experts, cut out redundancies, and produce clear, actionable reports with strategic recommendations. I use Alibaba's Qwen2 model, with 7 billion parameters and support for 29 languages, along with an extended 128k token context window. My focus is to deliver practical, data-driven reports that help implement meaningful improvements across healthcare processes. I look forward to helping your team take the next step."
        },
        {
            "name": "Manager and Advisor (Gemma Model 27b)",
            "image": "assets/agents/ManagerAndAdvisor2.png",
            "description": "I'm the Manager and Advisor. I consolidate feedback from various experts, cut out redundancies, and produce clear, actionable reports with strategic recommendations. I use Google's Gemma2 model, with an impressive 27 billion parameters, leveraging the highly efficient quantization format Q2_K. While optimizing memory usage, this model still delivers powerful insights across a wide range of tasks. Trained on vast datasets including web content, code, and mathematics, I provide in-depth, data-driven analyses that guide strategic decision-making. My focus is to deliver practical solutions that help streamline operations and implement meaningful improvements across healthcare processes."
        },
        {
            "name": "Data Analyst (LLaVA Model 7b)",
            "image": "assets/agents/DataAnalyst.jpeg",
            "description": "I'm the Data Analyst. I organize and manage data generated by other agents, ensuring efficient storage and accessibility in the backend. Powered by the LLaVA model, built on Meta's LLaMA architecture with 7 billion parameters, I handle tasks like visual question answering and image captioning, making me versatile for multimodal use. I also monitor agent performance and ensure data integrity. My goal is to streamline data management and boost system efficiency. I look forward to supporting your team's continuous improvements."
        },
        {
            "name": "Data Analyst (Gemma Model 2B)",
            "image": "assets/agents/DataAnalyst2.png",
            "description": "I'm the Data Analyst. My role is to organize and manage the data generated by other agents, ensuring efficient storage and easy accessibility in the backend systems. Powered by Google's Gemma 2 model, with 2 billion parameters, and using the Q4_K_S quantization method, I balance memory efficiency with high-performance capabilities. I also monitor the performance of other agents and ensure the integrity of data workflows. My goal is to streamline data management, boost system efficiency, and support your team’s data-driven decision-making process."
        },
        {
            "name": "Output Consistency Agent (LLaMA Model 8b)",
            "image": "assets/agents/OutputConsistencyAgent.jpeg",
            "description": "I'm the Output Consistency Agent. My job is to harmonize the outputs of all agents, ensuring consistency in structure, grammar, and formatting. Powered by Meta's LLaMA 3.1 8B, a state-of-the-art model excelling in natural language tasks like text generation and question answering, I review and correct spelling, grammar, and unwanted characters. I ensure that reports in TXT format are clear for users, while JSON outputs are properly formatted for backend integration. My goal is to deliver clean, structured data for smooth processing. I look forward to improving the accuracy of your data."
        }

    ]

    # Filter agents based on search query
    if search_query:
        filtered_agents = [agent for agent in ai_agents if search_query.lower() in agent['name'].lower()]
    else:
        filtered_agents = ai_agents

    # Custom CSS for better styling, dark mode compatibility, and simple fade-in animation
    st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .agent-container {
        background: rgba(14, 21, 37, 0.5) /* 100% opaco */; /* Cor de fundo trocada para rgba com 80% de opacidade */
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 7px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.5s ease-in-out;
    }
    .agent-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .agent-name {
        color: #ffffff;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        transition: color 0.3s ease;
    }
    .agent-container:hover .agent-name {
        color: #1b9e4b;
    }
    .agent-description {
        color: #e0e0e0;
        font-size: 16px;
        line-height: 1.5;
    }
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stApp h1 {
        color: white;
        font-size: 36px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display filtered AI agents with simple fade-in animation
    if filtered_agents:
        for agent in filtered_agents:
            with st.container():
                st.markdown(f"<div class='agent-container'>", unsafe_allow_html=True)
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    image = load_image(agent["image"])
                    if image:
                        st.image(image, use_column_width=True)
                    else:
                        st.error("Image not available")
                
                with col2:
                    st.markdown(f"<div class='agent-name'>{agent['name']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='agent-description'>{agent['description']}</div>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("No AI agents found matching your search criteria.")

    st.markdown("<hr style='border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

    # Add the powered by Inmotion link
    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    ai_crew_component()
