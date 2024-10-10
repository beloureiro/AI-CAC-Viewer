import streamlit as st  # type: ignore
import streamlit.components.v1 as components  # type: ignore

# Custom CSS for dark theme and styling
custom_css = """
<style>
body {
    color: #E0E0E0;
    background-color: #121212;
}
.stSelectbox [data-baseweb="select"] {
    background-color: #0e1525;
}
.stSelectbox [data-baseweb="select"] > div {
    background-color: #0e1525;
    color: #E0E0E0;
}
.plan-name {
    color: #1b9e4b;
    font-weight: bold;
}
.plan-details {
    margin-left: 20px;
    padding: 10px;
    border-left: 2px solid #1b9e4b;
}
.expander-header {
    font-size: 18px;
    font-weight: bold;
    color: #1b9e4b;
}
.subheader {
    color: #1b9e4b;
    font-size: 24px;
    font-weight: bold;
}
.comparison-column {
    padding: 10px;
    border-radius: 5px;
    margin: 5px;
}
</style>
"""


def get_plan_details(plan):
    details = {
        "Insight": '''
Who it's for: Healthcare professionals who prefer independent self-improvement and data-driven insights.

Key Features:
- Detailed patient feedback analysis
- Comprehensive reports on patient experience, workflows, and communication
- Self-guided improvement strategies

Benefits:
- Gain deep insights into your practice
- Identify areas for improvement independently
- Implement changes at your own pace

Focused on patient feedback analysis, this plan generates detailed reports on patient experience, workflows, and communication, allowing the professional to explore and implement their own improvement strategies.
''',
        "Mentor": '''
Who it's for: Healthcare professionals seeking guidance from experienced peers and personalized mentorship.

Key Features:
- Personalized mentorship from Elite Health Mentors
- Tailored guidance based on peer experience and knowledge
- Strategic advice for implementing improvements

Benefits:
- Learn from the best in your field
- Receive personalized guidance for growth
- Accelerate your professional development

With personalized mentorship from Elite Health Mentors, professionals receive specific guidance to implement improvements based on the experience and knowledge of their peers.
''',
        "Mentor & Care": '''
Who it's for: Healthcare professionals committed to comprehensive patient care and continuous improvement through mentorship and psychological support.

Key Features:
- All benefits of the Mentor Plan
- Emotional support for patients provided by qualified psychologists
- AI insights validated and adjusted by experts

Benefits:
- Provide holistic care to your patients
- Improve patient satisfaction and outcomes
- Enhance your practice with expert-validated insights

Designed for professionals who, in addition to valuing mentorship, understand that processes can fail but remain committed to showing their dedication to patient care, regardless of any process flaws or daily stressors. In this plan, qualified psychologists provide emotional support to patients by phone, validate the AI insights, and adjust the reports, which are then used by mentors to develop the mentoring plan, ensuring that care is comprehensive and humanized.
''',
        "Elite AI-Powered Care": '''
Who it's for: Healthcare professionals seeking the most comprehensive, AI-enhanced support system for continuous improvement and patient care excellence.

Key Features:
- All benefits from Insight, Mentor, and Mentor & Care plans
- 24/7 access to AI-SkillsAdvisor chatbot for personalized advice
- Real-time tips based on patient feedback and AI Clinical Advisory Crew recommendations
- Continuous learning and improvement opportunities

Benefits:
- Comprehensive support: Combine data-driven insights, expert mentorship, and psychological care
- Round-the-clock improvement: Receive instant, personalized guidance at any time
- Holistic patient care: Provide emotional support to patients while continuously enhancing your skills
- AI-powered growth: Leverage cutting-edge AI technology to accelerate your professional development

The Elite AI-Powered Care plan offers the ultimate package for healthcare professionals committed to excellence. It includes all the benefits of the previous plans:
1. Detailed patient feedback analysis and self-guided improvement strategies (from Insight plan)
2. Personalized mentorship from Elite Health Mentors (from Mentor plan)
3. Emotional support for patients provided by qualified psychologists (from Mentor & Care plan)

Additionally, this plan introduces the AI-SkillsAdvisor, an AI-powered chatbot available 24/7. This innovative tool provides personalized advice and tips based on real-time patient feedback and recommendations from the AI Clinical Advisory Crew. By combining human expertise with advanced AI capabilities, this plan offers unparalleled support for continuous learning, improvement, and patient care enhancement.
'''
    }
    return details[plan]


def ai_clinical_advisory_crew_tab():
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    # Updated main title styling
    st.markdown("""
    <h1 style='color: #ffffff;'>Advanced Analysis with Personalized Support</h1>
    <p style='color: #ffffff;'>The AI Clinical Advisory Crew offers four plans designed to support healthcare professionals. The Insight Plan provides detailed patient feedback and reports, allowing professionals to identify areas for self-improvement. The Mentor Plan includes personalized guidance from experienced mentors to help implement strategic changes. The Mentor & Care Plan adds psychological support for patients, ensuring emotional support and improving patient experience. The Elite AI-Powered Care Plan combines insights, mentorship, psychological care, and 24/7 access to the AI-SkillsAdvisor chatbot, offering continuous AI-driven guidance for growth and patient care excellence.</p>
    """, unsafe_allow_html=True)

    # Linha Horizontal
    # st.markdown("---")

    # Updated subheader styling
    st.markdown('<p class="subheader">Available Plans</p>',
                unsafe_allow_html=True)

    # Updated list of plans
    plans = ["Insight", "Mentor", "Mentor & Care", "Elite AI-Powered Care"]

    # Detailed breakdown of each plan with expandable sections
    for plan in plans:
        with st.expander(plan + " Plan", expanded=(plan == "Insight")):
            st.markdown(
                f'<p class="expander-header">{plan} Plan</p>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="plan-details">{get_plan_details(plan)}</div>', unsafe_allow_html=True)

    # Plan Diagrams section
    st.markdown('<p class="subheader">Plan Workflow Diagrams</p>',
                unsafe_allow_html=True)

    selected_plan = st.selectbox(
        "Select a Plan to view its diagram",
        options=plans,
        index=0,
        key="plan_selector"
    )

    # Updated Mermaid diagrams dictionary
    mermaid_diagrams = {
        "Insight": """
        sequenceDiagram
            autonumber
            actor Patient as Patient
            actor Healthcare_Professionals as Healthcare Professionals
            participant AI Clinical Advisory Crew
            
            Patient->>+AI Clinical Advisory Crew: Provides Feedback
            Note over AI Clinical Advisory Crew: Patient Experience Expert
            Note over AI Clinical Advisory Crew: Health & IT Process Expert
            Note over AI Clinical Advisory Crew: Clinical Psychologist
            Note over AI Clinical Advisory Crew: Communication Expert
            Note over AI Clinical Advisory Crew: Manager and Advisor
        
            AI Clinical Advisory Crew-->>-Healthcare_Professionals: Delivers Detailed Report for Self-Development
        """,
        "Mentor": """
        sequenceDiagram
            autonumber
            actor Patient as Patient
            actor Healthcare_Professionals as Healthcare Professionals
            participant AI Clinical Advisory Crew
            
            Patient->>+AI Clinical Advisory Crew: Provides Feedback
            Note over AI Clinical Advisory Crew: Patient Experience Expert
            Note over AI Clinical Advisory Crew: Health & IT Process Expert
            Note over AI Clinical Advisory Crew: Clinical Psychologist
            Note over AI Clinical Advisory Crew: Communication Expert
            Note over AI Clinical Advisory Crew: Manager and Advisor
            
            create participant Mentors as Elite Mentors
            AI Clinical Advisory Crew->>+Mentors: Sends Report to Mentors (Mentor Plan)
            Note over Mentors: Provide strategic advice based on peer knowledge.
            
            Mentors-->>-Healthcare_Professionals: Offers guidance for improvement
        """,
        "Mentor & Care": """
        sequenceDiagram
            autonumber
            actor Patient as Patient
            actor Healthcare_Professionals as Healthcare Professionals
            participant AI Clinical Advisory Crew
            
            Patient->>+AI Clinical Advisory Crew: Provides Feedback
            Note over AI Clinical Advisory Crew: Patient Experience Expert
            Note over AI Clinical Advisory Crew: Health & IT Process Expert
            Note over AI Clinical Advisory Crew: Clinical Psychologist
            Note over AI Clinical Advisory Crew: Communication Expert
            Note over AI Clinical Advisory Crew: Manager and Advisor
            
            create participant Psychologist as Psychologist
            AI Clinical Advisory Crew->>+Psychologist: Connects with Psychologist
            Psychologist->>+Patient: Provides Emotional Support to the Patient
            Psychologist-->>-AI Clinical Advisory Crew: Validates Report
        
            create participant Mentors as Elite Mentors
            AI Clinical Advisory Crew->>+Mentors: Sends Report to Mentors (Mentor & Care Plan)
            Note over Mentors: Develop personalized coaching strategies.
            
            Mentors-->>-Healthcare_Professionals: Conduct mentorship sessions with professionals.
        """,
        "Elite AI-Powered Care": """
        sequenceDiagram
            autonumber
            actor Patient as Patient
            actor Healthcare_Professionals as Healthcare Professionals
            participant AI_Clinical_Advisory_Crew as AI Clinical Advisory Crew
            
            Patient->>+AI_Clinical_Advisory_Crew: Provides Feedback
            Note over AI_Clinical_Advisory_Crew: Patient Experience Expert
            Note over AI_Clinical_Advisory_Crew: Health & IT Process Expert
            Note over AI_Clinical_Advisory_Crew: Clinical Psychologist
            Note over AI_Clinical_Advisory_Crew: Communication Expert
            Note over AI_Clinical_Advisory_Crew: Manager and Advisor

            create participant Psychologist as Psychologist
            AI_Clinical_Advisory_Crew->>+Psychologist: Connects with Psychologist
            Psychologist->>+Patient: Provides Emotional Support to the Patient
            Psychologist-->>-AI_Clinical_Advisory_Crew: Validates Report

            create participant Mentors as Elite Mentors
            AI_Clinical_Advisory_Crew->>+Mentors: Validated and updated sends to Elite Mentors
            Note over Mentors: Develop personalized coaching strategies.
            
            Mentors-->>-Healthcare_Professionals: Conduct mentorship sessions with professionals.

            create participant AI_SkillsAdvisor as AI-Skills Advisor
            AI_Clinical_Advisory_Crew->>+AI_SkillsAdvisor: Sends reports 
            AI_SkillsAdvisor-->>Healthcare_Professionals: Provides 24/7 personalized advice and tips based on patient feedback and AI Clinical Advisory Crew recommendations
        """
    }

    # Updated diagram heights
    diagram_heights = {
        "Insight": 600,
        "Mentor": 700,
        "Mentor & Care": 800,
        "Elite AI-Powered Care": 900
    }

    mermaid_chart = f'''
    <div class="mermaid" id="mermaid-diagram">
    %%{{init: {{
        'theme': 'dark',
        'themeVariables': {{
            'actorTextColor': '#FFFFFF',
            'actorLineColor': '#1b9e4b',
            'signalColor': '#1b9e4b',
            'signalTextColor': '#FFFFFF',
            'labelTextColor': '#FFFFFF',
            'noteBkgColor': '#0e1525',
            'noteTextColor': '#FFFFFF'
        }}
    }}}}%%
    {mermaid_diagrams[selected_plan]}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'dark'
    }});

    function adjustMermaidHeight() {{
        var mermaidDiv = document.getElementById('mermaid-diagram');
        var svgElement = mermaidDiv.querySelector('svg');
        if (svgElement) {{
            var height = svgElement.getBBox().height;
            mermaidDiv.style.height = (height + 40) + 'px';  // Add more padding
        }}
    }}

    // Adjust height after Mermaid has rendered the diagram
    mermaid.init(undefined, ".mermaid");
    setTimeout(adjustMermaidHeight, 500);  // Increased delay for rendering

    // Adjust height when window is resized
    window.addEventListener('resize', adjustMermaidHeight);
    </script>
    '''

    components.html(mermaid_chart, height=diagram_heights[selected_plan])
    # Linha Horizontal
    st.markdown("---")

    # New section for side-by-side comparison
    st.markdown('<p class="subheader">Compare Plans Side-by-Side</p>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="comparison-column">', unsafe_allow_html=True)
        plan1 = st.selectbox("Select first plan for comparison", [
                             "Insight", "Mentor", "Mentor & Care", "Elite AI-Powered Care"], key="plan1")
        st.markdown(f"<h3>{plan1} Plan</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div class="plan-details">{get_plan_details(plan1)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="comparison-column">', unsafe_allow_html=True)
        plan2 = st.selectbox("Select second plan for comparison", [
                             "Insight", "Mentor", "Mentor & Care", "Elite AI-Powered Care"], key="plan2")
        st.markdown(f"<h3>{plan2} Plan</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div class="plan-details">{get_plan_details(plan2)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Linha Horizontal
    st.markdown("---")
    # Add new section for the cycle of well-rated professionals
    st.markdown('<p class="subheader">Cycle of Well-Rated Professionals</p>',
                unsafe_allow_html=True)

    st.markdown("""
    The AI Clinical Advisory Crew fosters a virtuous cycle of professional growth and patient satisfaction. This cycle illustrates the journey of both patients and healthcare professionals within the AI Clinical Advisory Crew framework:

    1. **Patient Interaction**: The cycle begins with a patient seeking healthcare services.
    
    2. **Cycle of Self-Development**: Healthcare professionals engage in a continuous process of improvement:
       - <span style="color:#1b9e4b"><b>Well-Rated Professionals</b></span>: These are the healthcare providers who have already achieved high ratings and success.
       - <span style="color:#1b9e4b"><b>Mentorship</b></span>: Well-rated professionals provide mentorship and guidance to others.
       - <span style="color:#1b9e4b"><b>Improved Professionals</b></span>: Through mentorship and the AI Clinical Advisory Crew's insights, professionals enhance their skills and practices.
    
    3. **Outcomes**:
       - <span style="color:#1b9e4b"><b>Happy Patients</b></span>: The improved healthcare services lead to increased patient satisfaction.
       - <span style="color:#1b9e4b"><b>Fully Booked Professionals</b></span>: As professionals improve and gain higher ratings, they attract more patients, leading to a thriving practice.

    This cycle demonstrates how the AI Clinical Advisory Crew contributes to both professional growth and patient satisfaction, creating a win-win situation for all involved.
    """, unsafe_allow_html=True)

    # New Mermaid diagram
    mermaid_chart = """
    <div class="mermaid">
    %%{init: {
        'theme': 'dark',
        'themeVariables': {
            'primaryColor': '#1b9e4b',
            'primaryTextColor': '#fff',
            'primaryBorderColor': '#1b9e4b',
            'secondaryColor': '#006100',
            'tertiaryColor': '#fff'
        }
    }}%%
    stateDiagram
        direction TB

        accTitle: Journey of Patient and Professionals
        accDescr: This diagram illustrates the interaction between patients and health professionals in the AI Clinical Advisory Crew framework.

        classDef patientState stroke:#1b9e4b,stroke-width:2px
        classDef professionalState stroke:#1b9e4b,stroke-width:2px
        classDef transitionState stroke:#1b9e4b,,stroke-width:1px

        [*] --> Patient
        Patient --> Cycle_of_Self_Development
        state Cycle_of_Self_Development {
            direction TB
         
                direction LR
                Well_Rated_Professional --> Mentorship
                Mentorship --> Improved_Professionals
                Improved_Professionals --> Well_Rated_Professional
        }
        Cycle_of_Self_Development --> Happy_Patient
        Cycle_of_Self_Development --> Fully_Booked_Professionals
        Happy_Patient --> [*]
        Fully_Booked_Professionals --> [*]
        class Patient patientState
        class Cycle_of_Self_Development transitionState
        class Well_Rated_Professional, Mentorship, Comprehensive_Training_Process, Improved_Professionals professionalState
        class Happy_Patient transitionState
        class Fully_Booked_Professionals transitionState
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
    mermaid.initialize({
      startOnLoad: true,
      theme: 'dark'
    });
    </script>
    """

    components.html(mermaid_chart, height=500)

    st.markdown("<hr style='border-top: 1px solid #ddd;'>",
                unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    ai_clinical_advisory_crew_tab()
