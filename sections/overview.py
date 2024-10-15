import streamlit as st  # type: ignore

def show_overview():
    """
    Displays the overview of the AI Clinical Advisory Crew.

    This function renders the main content of the overview page, including the title, value proposition,
    available plans, and details about the AI team. It uses Streamlit's markdown capabilities to format
    the content and includes custom CSS for styling.

    No parameters or return values.
    """
    st.markdown("""
    <h1>
        <span style="color: #1b9e4b; font-style: italic; text-shadow: 1px 1px 2px #000000;">AI</span> 
        Clinical Advisory 
        <span style="color: #1b9e4b; font-style: italic; text-shadow: 1px 1px 2px #000000;">Crew</span>
    </h1>
    <p>Welcome to the <strong>AI Clinical Advisory Crew</strong>, a platform that blends artificial intelligence with healthcare expertise to elevate care standards. Here, you can explore our framework, access insights from AI agents, review workflows, learn more about the agents and available plans, and even try out a demo preview of our chatbot.</p>
    <p>Our system leverages a robust <strong>AI-Driven Problem Solving</strong> strategy, powered by AI models from top tech innovators like Anthropic, OpenAI, Mistral AI, Meta, Google, Microsoft, Tencent, EleutherAI, Stability AI, and other open-source collaborators. This enables efficient workflows and fosters innovation within healthcare.</p>
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
    <h2>Available Plans</h2>
    <ul>
        <li><strong>Insight Plan</strong>: Ideal for professionals who value independent self-improvement and data-driven insights.</li>
        <li><strong>Mentor Plan</strong>: Designed for professionals seeking personalized guidance and mentorship from experienced peers.</li>
        <li><strong>Mentor & Care Plan</strong>: Perfect for professionals committed to comprehensive patient care, combining expert mentorship with emotional support.</li>
        <li><strong>Elite AI-Powered Care Plan</strong>: Designed for forward-thinking professionals who desire 24/7 access to the AI-Skills Advisor chatbot, providing continuous AI-driven guidance, detailed patient feedback analysis, and personalized coaching for enhanced patient care.</li>
    </ul>                            
    """, unsafe_allow_html=True)

    # Insert new expander here
    custom_css = """
    <style>
    body {
        color: #E0E0E0;
        background-color: #121212;
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
    </style>
    """

    # Apply custom CSS for the new expander
    st.markdown(custom_css, unsafe_allow_html=True)

    # Expander for the AI Clinical Advisory Crew content
    with st.expander("Expand to explore the plans in detail", expanded=False):
        st.markdown('<p class="expander-header">AI Clinical Advisory Crew</p>', unsafe_allow_html=True)
        st.markdown(
            '''
            <div class="plan-details">
            The AI Clinical Advisory Crew offers a service that combines detailed AI-driven analysis with four plans, each adding more value to healthcare professionals' performance. The process begins with collecting patient feedback and generating reports that identify opportunities to improve care, workflows, and communication.

            - <strong style="color: #1b9e4b;">Insight Plan</strong>: For professionals seeking to pursue self-improvement independently, based on patient feedback analysis, this plan provides detailed reports crafted by a team of AI specialists. The content includes insights from the following: the AI Patient Experience Expert, who analyzes patient feedback and evaluates emotional intensity; the AI Health & IT Process Expert, who maps the patient journey and identifies process inefficiencies; the AI Clinical Psychologist, who develops psychological support strategies for a post-consultation approach; the AI Communication Expert, who assesses communication and offers guidance in this area; and the AI Manager and Advisor, who provides a managerial overview and summary of patient feedback. This plan allows professionals to explore and implement their own improvement strategies at their own pace.
            
            - <strong style="color: #1b9e4b;">Mentor Plan</strong>: For those who understand the value of learning from high-performing peers and seek strategic guidance, this plan not only includes all the benefits of the Insight Plan but also provides personalized mentoring sessions with the Elite Health Mentors. Participants receive specific guidance to implement improvements based on the experience and knowledge of their peers, learning from the best in their field in a customized way, accelerating their professional development.
            
            - <strong style="color: #1b9e4b;">Mentor & Care Plan</strong>: Designed for professionals who, beyond valuing AI insights and mentoring, understand that processes can sometimes fail but remain committed to demonstrating dedication to patient care, regardless of process failures or day-to-day stress. In this plan, qualified psychologists provide emotional support to patients over the phone, validate the AI team's insights, and adjust reports as needed, which are then used by mentors to customize the mentoring content. This plan ensures that care is comprehensive, reinforcing a human-centered approach in patient care and offering a holistic management of the care process.
            
            - <strong style="color: #1b9e4b;">Elite AI-Powered Care Plan</strong>: Designed for innovative professionals seeking 24/7 access to the AI-Skills Advisor chatbot, this plan provides continuous guidance, detailed patient feedback analysis, and personalized coaching. By combining all the benefits of previous plans—including specialized AI reports, expert mentoring, and emotional support for patients—the Elite AI-Powered Care Plan is ideal for those looking for a comprehensive and innovative approach to professional development. With the AI-Skills Advisor available anytime, professionals receive instant data-driven guidance and recommendations from the AI-based clinical advisory team. This is the ultimate solution for those committed to excellence and continuous growth, leveraging the best of technology.

            **Cycle of self-improvement**

            The AI Clinical Advisory Crew fosters a continuous cycle of self-improvement, where highly rated professionals who are part of the "Elite Health Mentors" use customized evaluation reports and insights from the AI team to promote best practices among colleagues who received lower ratings. With support and guidance, these professionals improve their performance and become well-rated, qualifying them to mentor others and repeating the development cycle, ultimately resulting in a better patient experience. Thus, each professional, with ongoing AI support, enhances their performance and contributes to improving the entire healthcare network, creating a continuous flow of evolution and collaboration.
            </div>
            ''', unsafe_allow_html=True
        )

    # Continue with the rest of the overview content...
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
        <li><strong>AI-Skills Advisor</strong>: A 24/7 chatbot providing real-time, personalized advice for ongoing professional development and patient care improvement.</li>
    </ol>
    <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Powered by <a href="https://inmotion.today/" style='color: #1b9e4b;'>Inmotion</a></p>
    </div>
    """, unsafe_allow_html=True)

    # st.markdown("""
    # <strong>Key Benefits:</strong><br>
    # - Runs on local AI models, maximizing data security<br>
    # - Handles all processing internally, avoiding third-party APIs<br>
    # - Reduces costs by eliminating external API reliance<br>
    # - Maintains full control over data privacy<br>
    # - Supports continuous skill improvement and quality enhancement
    # <hr style='border-top: 0.5px solid #1c2333; margin: 10px 0;' />
    # """, unsafe_allow_html=True)