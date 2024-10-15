import streamlit as st

# Dados de sentimento positivo e negativo por mês
positive_sentiment = [1, 0, 1, 2]  # Julho, Agosto, Setembro, Outubro
negative_sentiment = [1, 1, 1, 0]  # Julho, Agosto, Setembro, Outubro

# Criação do gráfico de linha com dados de sentimentos positivos e negativos
st.line_chart({
    "Positive Sentiment": positive_sentiment,
    "Negative Sentiment": negative_sentiment
})

# Explicação do gráfico
st.write("""
### Trend of Positive and Negative Sentiments Over Time

#### Monthly Breakdown:
- **Positive Comments**:
  - **July**: 1, **August**: 0, **September**: 1, **October**: 2.
- **Negative Comments**:
  - **July**: 1, **August**: 1, **September**: 1, **October**: 0.

The chart displays the evolution of positive and negative sentiments over the months. Positive sentiment shows an increase in October, while negative sentiment decreases, suggesting improved satisfaction.
""")

# Adicionando uma nota para ajudar o usuário a interpretar os dados por mês
st.write("""
**Note:** The X-axis represents months from July (0) to October (3).
""")
