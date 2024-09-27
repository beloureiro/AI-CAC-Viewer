import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for dark theme and styling
custom_css = """
<style>
body {
    color: #E0E0E0;
    background-color: #121212;
}
.stSelectbox [data-baseweb="select"] {
    background-color: #1E1E1E;
}
.stSelectbox [data-baseweb="select"] > div {
    background-color: #1E1E1E;
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
'''
    }
    return details[plan]

def ai_clinical_advisory_crew_tab():
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Updated main title styling
    st.markdown('<h1><span style="color: #1b9e4b;"><i>AI</i></span> Clinical Advisory <span style="color: #1b9e4b;"><i>Crew</i></span>: Advanced Analysis with Personalized Support</h1>', unsafe_allow_html=True)

    st.markdown("""
    The AI Clinical Advisory Crew offers a service that combines detailed AI-driven analysis with three plans, each adding more value to healthcare professionals' performance. The process begins by gathering patient feedback and generating reports that identify opportunities for improving care, workflows, and communication.

    The AI Clinical Advisory Crew fosters a cycle of self-development, where healthcare professionals use the provided insights and guidance to enhance their performance. As a result, the patient experience is enriched, attracting more patients and improving the professional's ratings. Over time, this progress can lead to the professional joining the Elite Health Mentors group, where they can mentor peers, be invited to give talks, and earn compensation for helping other professionals enhance their practices.
    """)

    # Updated subheader styling
    st.markdown('<p class="subheader">Available Plans</p>', unsafe_allow_html=True)

    # Detailed breakdown of each plan with expandable sections
    for plan in ["Insight", "Mentor", "Mentor & Care"]:
        with st.expander(plan + " Plan", expanded=(plan == "Insight")):
            st.markdown(f'<p class="expander-header">{plan} Plan</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="plan-details">{get_plan_details(plan)}</div>', unsafe_allow_html=True)

    # Plan Diagrams section
    st.markdown('<p class="subheader">Plan Diagrams</p>', unsafe_allow_html=True)

    selected_plan = st.selectbox(
        "Select a Plan to view its diagram",
        options=["Insight", "Mentor", "Mentor & Care"],
        index=0,
        key="plan_selector"
    )

    # Mermaid diagram display
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
        """
    }

    mermaid_chart = f'''
    <div class="mermaid">
    %%{{init: {{
        'theme': 'dark',
        'themeVariables': {{
            'actorTextColor': '#FFFFFF',
            'actorLineColor': '#1b9e4b',
            'signalColor': '#1b9e4b',
            'signalTextColor': '#FFFFFF',
            'labelTextColor': '#FFFFFF',
            'noteBkgColor': '#262730',
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
    </script>
    '''
    
    components.html(mermaid_chart, height=600)

    # New section for side-by-side comparison
    st.markdown('<p class="subheader">Compare Plans Side-by-Side</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="comparison-column">', unsafe_allow_html=True)
        plan1 = st.selectbox("Select first plan for comparison", ["Insight", "Mentor", "Mentor & Care"], key="plan1")
        st.markdown(f"<h3>{plan1} Plan</h3>", unsafe_allow_html=True)
        st.markdown(f'<div class="plan-details">{get_plan_details(plan1)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="comparison-column">', unsafe_allow_html=True)
        plan2 = st.selectbox("Select second plan for comparison", ["Insight", "Mentor", "Mentor & Care"], key="plan2")
        st.markdown(f"<h3>{plan2} Plan</h3>", unsafe_allow_html=True)
        st.markdown(f'<div class="plan-details">{get_plan_details(plan2)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Add new section for the cycle of well-rated professionals
    st.write("---")  # Usando st.write
    st.markdown('<p class="subheader">Cycle of Well-Rated Professionals</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The AI Clinical Advisory Crew fosters a virtuous cycle of professional growth and patient satisfaction. This cycle illustrates the journey of both patients and healthcare professionals within the AI Clinical Advisory Crew framework:

    1. **Patient Interaction**: The cycle begins with a patient seeking healthcare services.
    
    2. **Cycle of Self-Development**: Healthcare professionals engage in a continuous process of improvement:
       - **Well-Rated Professionals**: These are the healthcare providers who have already achieved high ratings and success.
       - **Mentorship**: Well-rated professionals provide mentorship and guidance to others.
       - **Improved Professionals**: Through mentorship and the AI Clinical Advisory Crew's insights, professionals enhance their skills and practices.
    
    3. **Outcomes**:
       - **Happy Patients**: The improved healthcare services lead to increased patient satisfaction.
       - **Fully Booked Professionals**: As professionals improve and gain higher ratings, they attract more patients, leading to a thriving practice.

    This cycle demonstrates how the AI Clinical Advisory Crew contributes to both professional growth and patient satisfaction, creating a win-win situation for all involved.
    """)


    # New Mermaid diagram
    mermaid_chart = """
    <div class="mermaid">
    %%{init: {
        'theme': 'dark',
        'themeVariables': {
            'primaryColor': '#1b9e4b',
            'primaryTextColor': '#fff',
            'primaryBorderColor': '#1b9e4b',
            'lineColor': '#F8B229',
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
    
    components.html(mermaid_chart, height=600)
    
    st.markdown("<hr style='border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    ai_clinical_advisory_crew_tab()
