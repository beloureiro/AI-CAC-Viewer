import streamlit as st
import time

# Dicionário contendo as perguntas e respostas
data = {
    "what_can_you_do": {
        "question": "What can you do?",
        "answer": "I am the AI-Skills Advisor, a key component of the AI Clinical Advisory Crew..."
    },
    "quick_wins_to_improve_patient_satisfaction": {
        "question": "Are there quick wins to improve patient satisfaction?",
        "answer": "To improve patient satisfaction quickly, consider the following suggestions..."
    },
    "biggest_inefficiencies": {
        "question": "Where are my biggest inefficiencies right now?",
        "answer": "Based on the information provided, your biggest inefficiencies seem to be..."
    },
    "advice_on_improving_workflow": {
        "question": "Any advice on improving my workflow?",
        "answer": "To improve your workflow, consider the following suggestions..."
    },
    "display_patient_feedback": {
        "question": "Please display the patient feedback.",
        "answer": "The patient feedback is as follows:\n\nPositive:\n- \"I can't thank the team enough for their amazing work...\""
    },
    "overall_patient_feedback_trend": {
        "question": "What's the overall patient feedback trend over time?",
        "answer": "The overall patient feedback trend over time indicates a mix of positive and negative experiences..."
    }
}

# Título e introdução
st.title("AI-Skills Advisor")
st.markdown("Hello! I'm the AI-Skills Advisor, a part of the Clinical Advisory Crew.")

# Inicializa o estado da sessão
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Função para adicionar mensagem ao chat
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# Função para processar a resposta
def process_response(answer):
    with st.chat_message("assistant"):
        with st.status("Processing your request...", expanded=True):
            st.write("Analyzing your question...")
            time.sleep(0.5)
            st.write("Generating insights...")
            time.sleep(0.5)
            st.write("Preparing response...")
            time.sleep(0.5)
        st.markdown(answer)
    add_message("assistant", answer)

# Exibe o histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Organização dos botões
button_cols = st.columns(3)
button_rows = list(data.keys())

# Responde às interações do usuário com botões
for idx, key in enumerate(button_rows):
    col = button_cols[idx % 3]
    if col.button(data[key]["question"]):
        add_message("user", data[key]["question"])
        process_response(data[key]["answer"])

# Campo de entrada para perguntas personalizadas
user_input = st.chat_input("Any other questions?")
if user_input:
    add_message("user", user_input)
    process_response("I'm here to assist with insights and guidance.")


# to run the app: streamlit run sections/new_bot.py
