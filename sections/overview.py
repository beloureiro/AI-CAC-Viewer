import streamlit as st  # type: ignore

def show_overview():
    st.markdown("""
    <h1>
        <span style="color: #1b9e4b; font-style: italic; text-shadow: 1px 1px 2px #000000;">AI</span> 
        Clinical Advisory 
        <span style="color: #1b9e4b; font-style: italic; text-shadow: 1px 1px 2px #000000;">Crew</span>
    </h1>
    <p>Welcome to the <strong>AI Clinical Advisory Crew</strong>, a platform combining artificial intelligence with healthcare expertise to elevate care standards. This WebApp lets you explore the framework, access insights from AI agents, review workflows, learn about the agents and available plans, and try out a chatbot demo in development mode. For those interested in the technical backend, you can check out the full repository on GitHub <a href="https://github.com/beloureiro/AI-CAC-V1.3" style='color: #1b9e4b; text-shadow: 1px 1px 2px #000000;'>here</a>.</p>
    <p>Our system uses a robust <strong>AI-Driven Problem Solving</strong> strategy, featuring AI models from top tech companies like Anthropic, OpenAI, Mistral AI, Meta, Google, Microsoft, Tencent, EleutherAI, Stability AI, and other open-source collaborators. This enables streamlined workflows and innovation in the healthcare setting.</p>
    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)


    st.markdown("""
    <h2>Value Proposition</h2>
    <p>The <strong>AI Clinical Advisory Crew</strong> is here to drive self-improvement for healthcare professionals, while enhancing patient care. Designed for freelancers, clinics, and hospitals, our framework combines direct patient feedback with technical insights from AI and industry experts, fostering continuous improvement in care quality.</p>
    
    <div style='background-color: #1c2333; padding: 15px 10px; border-radius: 8px; text-align: center; color: #FFFFFF; margin-top: 5px;'>
        <p style='font-size: 1.2em; margin: 0; line-height: 1.5em;'><strong>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">FEEDBACK</span>
            <span>&nbsp; + &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">TECHNICAL DIAGNOSIS</span>
            <span>&nbsp; = &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">PERFORMANCE PATH</span>
            <span>&nbsp; = &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">QUALITY CARE</span>
            <span>&nbsp; = &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">SATISFIED PATIENTS</span>
            <span>&nbsp; = &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">FULL SCHEDULE</span>
            <span>&nbsp; = &nbsp; </span>
            <span style="color: #1b9e4b; text-shadow: 1px 1px 2px #000000;">PROFESSIONAL RECOGNITION</span>
        </strong></p>
    </div>

    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Our AI Team Includes Eight Key Agents:</h2>
    <ol>
        <li><strong>Patient Experience Expert</strong>: Analyzes patient feedback, pinpoints key issues, and evaluates emotional intensity to improve the overall experience.</li>
        <li><strong>Health & IT Process Expert</strong>: Maps out the patient journey, finds inefficiencies, and suggests workflow improvements.</li>
        <li><strong>Clinical Psychologist</strong>: Specializes in understanding emotional states and creating customized psychological support strategies.</li>
        <li><strong>Communication Expert</strong>: Assesses communication quality between healthcare providers and patients, offering tips for better clarity and empathy.</li>
        <li><strong>Manager and Advisor</strong>: Collects feedback from all agents, providing actionable reports with strategic insights.</li>
        <li><strong>Data Analyst</strong>: Analyzes large datasets to derive meaningful insights from patient feedback and healthcare data.</li>
        <li><strong>Output Consistency Agent</strong>: Ensures consistent structure, grammar, and formatting across all outputs.</li>
        <li><strong>AI-SkillsAdvisor</strong>: A 24/7 chatbot providing real-time, personalized advice for ongoing professional development and patient care improvement.</li>
    </ol>
    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>Available Plans</h2>
    <ul>
        <li><strong>Insight Plan</strong>: Provides detailed reports and analyses to support data-driven improvements.</li>
        <li><strong>Mentor Plan</strong>: Offers one-on-one mentorship from experienced professionals to guide your growth.</li>
        <li><strong>Mentor & Care Plan</strong>: Combines expert mentorship with psychological support for a more human approach to care.</li>
        <li><strong>Elite AI-Powered Care Plan</strong>: Includes all benefits plus 24/7 access to the AI-SkillsAdvisor chatbot for continuous support.</li>
    </ul>
    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)

    st.markdown("""
    <strong>Key Benefits:</strong><br>
    - Runs on local AI models, maximizing data security<br>
    - Handles all processing internally, avoiding third-party APIs<br>
    - Reduces costs by eliminating external API reliance<br>
    - Maintains full control over data privacy<br>
    - Supports continuous skill improvement and quality enhancement
    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)
