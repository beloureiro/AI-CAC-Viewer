import streamlit as st
import os
import sys

# Adicionar o diretório atual ao caminho do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importando as funções de outras sections
from sections.overview import show_overview
from sections.ai_agents import show_ai_agents

# Configuração inicial da página
def setup_page():
    st.set_page_config(page_title="AI Clinical Advisory Crew", layout="wide")

# Função principal
def main():
    setup_page()

    # Navegação entre as abas
    tab = st.sidebar.radio("Selecione uma Aba", ["Overview", "AI Agents", "Feedback Analysis"])

    if tab == "Overview":
        show_overview()
    elif tab == "AI Agents":
        show_ai_agents()
    elif tab == "Feedback Analysis":
        st.write("A aba de Feedback Analysis será implementada em breve!")

if __name__ == "__main__":
    main()
