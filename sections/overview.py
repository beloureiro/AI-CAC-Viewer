import streamlit as st

def show_overview():
    st.markdown("""
    <div style='background-color: #1E2129; padding: 20px; border-radius: 10px;'>
    <h1><span style="color: #1b9e4b; font-style: italic;">AI</span><span style="color: #FFFFFF;"> Clinical Advisory </span><span style="color: #1b9e4b; font-style: italic;">Crew</span></h1>
    <p>Welcome to the <strong>AI Clinical Advisory Crew</strong>, an advanced and flexible system designed to transform and elevate the patient experience in healthcare. This project brings together a team of specialized AI agents, each with a unique role in analyzing patient feedback, improving healthcare workflows, assessing emotional states, and delivering actionable recommendations for communication and operational improvements.</p>
    <p>At the heart of this system lies its dynamic flexibility: it navigates across a suite of <strong>Large Language Models (LLMs)</strong> to determine the optimal AI configuration for each specific task. By utilizing models like Meta's LLaMA, NousResearch's Hermes, Microsoft's Phi, and others, the system continuously tests and refines outputs to ensure that the best-suited AI crew is selected to address the task at hand. This multi-agent approach allows for the combination of strengths across different models, ensuring comprehensive, data-driven analysis that adapts to the unique needs of your healthcare environment.</p>
    <p><strong>A major benefit</strong> of this system is that it operates using <strong>local LLMs</strong>, ensuring <strong>maximum data security</strong> by processing all information internally, without reliance on third-party APIs. This also delivers <strong>significant cost savings</strong>, as there is no need for external API usage, keeping operational costs low while maintaining full control over data privacy.</p>
    
    <h2>Our AI team consists of seven dedicated agents:</h2>
    <ol>
        <li><strong>Patient Experience Expert (Phi Model)</strong>: Analyzes patient feedback, identifies key issues, and gauges emotional intensity to enhance the overall healthcare experience.</li>
        <li><strong>Health & IT Process Expert (Gemma Model)</strong>: Maps the patient journey, identifies inefficiencies, and recommends improvements in healthcare workflows.</li>
        <li><strong>Clinical Psychologist (OpenHermes Model)</strong>: Specializes in analyzing emotional states and crafting personalized psychological support strategies.</li>
        <li><strong>Communication Expert (Mistral Model)</strong>: Evaluates communication quality between healthcare professionals and patients, suggesting improvements for clarity and empathy.</li>
        <li><strong>Manager and Advisor (Qwen Model)</strong>: Consolidates feedback from all agents, producing actionable reports with strategic recommendations.</li>
        <li><strong>Data Analyst (LLaVA Model)</strong>: Processes and analyzes large datasets to extract valuable insights from patient feedback and healthcare operations data.</li>
        <li><strong>Output Consistency Agent (LLaMA Model)</strong>: Harmonizes outputs from all agents, ensuring consistency in structure, grammar, and formatting.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    Key Benefits:
    - Operates using local LLMs, ensuring maximum data security
    - Processes all information internally, without reliance on third-party APIs
    - Delivers significant cost savings by eliminating the need for external API usage
    - Maintains full control over data privacy
    """)
