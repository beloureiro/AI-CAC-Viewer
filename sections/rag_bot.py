import streamlit as st  # type: ignore

# Dicionário contendo as perguntas e respostas
data = {
    "what_can_you_do": {
        "question": "What can you do?",
        "answer": "I am the AI-Skills Advisor, a key component of the AI Clinical Advisory Crew. My role is to provide continuous, data-driven support to healthcare professionals like yourself. Here's what I can do for you:\n\n1. Analyze patient feedback and generate insights to improve care quality.\n2. Identify opportunities to enhance workflows and processes in healthcare delivery.\n3. Offer communication strategies to improve patient-provider interactions.\n4. Provide psychological insights for better post-consultation patient care.\n5. Deliver managerial overviews and summaries of patient feedback.\n6. Offer personalized recommendations for professional development.\n7. Provide instant, 24/7 access to AI-driven guidance and support.\n\nMy goal is to help you excel in your healthcare practice by leveraging AI-powered insights and continuous learning. How can I assist you in improving your professional skills today?"
    },
    "quick_wins_to_improve_patient_satisfaction": {
        "question": "Are there quick wins to improve patient satisfaction?",
        "answer": "To improve patient satisfaction quickly, consider the following suggestions:\n\n1. Implement regular follow-up protocols: This will help monitor patient progress and address any worsening conditions promptly. According to the Patient Experience Expert, this is crucial in preventing missed opportunities for intervention.\n2. Provide language interpretation services: Ensure that patients with language barriers can communicate effectively with healthcare providers. The Communication Expert suggests providing immediate measures for language interpretation services and ongoing training programs for staff.\n3. Maintain timely appointments: Continue scheduling practices to ensure patients are seen on time, as this contributes positively to patient experience. According to the Health & IT Process Expert, timeliness is a key aspect of a positive patient journey.\n4. Train staff in empathy and active listening: Conduct mandatory training sessions focused on empathy and active listening for healthcare providers. This will help them demonstrate genuine concern for patients' well-being and address issues like lack of interest in patient evolution. According to the Manager and Advisor, this is essential in rebuilding trust and improving patient outcomes.\n5. Enhance communication around wait times: Inform patients about expected wait times more precisely to manage expectations, and offer engaging activities or periodic updates to mitigate the perceived length of the wait. The Communication Expert suggests clear communication on waiting times and engagement during wait periods.\n\nBy implementing these suggestions, you can improve patient satisfaction quickly and create a positive experience for your patients."
    },
    "biggest_inefficiencies": {
        "question": "Where are my biggest inefficiencies right now?",
        "answer": "Based on the information provided, your biggest inefficiencies seem to be related to patient communication and follow-up protocols.\n\nAccording to the Clinical Psychologist, there's a significant decline in mental well-being among patients who experience lack of interest from healthcare providers in their evolution and worsening conditions. This indicates a need for more empathetic interactions and timely interventions.\n\nAccording to the Communication Expert, poor communication quality is identified as an issue due to lack of interest in patient's evolution and worsening condition. They suggest implementing regular follow-up protocols to monitor patient progress actively and training staff on empathy and active listening techniques.\n\nAccording to the Manager and Advisor, it is recommended to implement regular follow-up protocols to monitor patient progress actively and conduct mandatory training sessions focused on empathy and active listening for healthcare providers.\n\nAdditionally, there are concerns about language barriers causing misunderstandings between doctors and patients. According to the Communication Expert, providing language interpretation services during consultations and training healthcare staff in basic phrases of common languages spoken by patients can help bridge communication gaps.\n\nAccording to the Health & IT Process Expert, inefficiencies include lack of monitoring and interest in patient evolution, leading to missed opportunities for intervention. They suggest implementing regular follow-up protocols to monitor patient progress actively.\n\nTo address these issues, consider implementing the following recommendations:\n\n1. Implement regular follow-up protocols to monitor patient progress actively.\n2. Conduct mandatory training sessions focused on empathy and active listening for healthcare providers.\n3. Provide language interpretation services during consultations to bridge communication gaps.\n4. Train healthcare staff in basic phrases of common languages spoken by patients for better rapport.\n\nBy addressing these inefficiencies, you can improve patient outcomes, enhance the overall quality of care, and foster a more empathetic and supportive environment within your healthcare setting."
    },
    "advice_on_improving_workflow": {
        "question": "Any advice on improving my workflow?",
        "answer": "To improve your workflow, consider the following suggestions:\n\n1. Implement regular follow-up protocols: According to the Patient Experience Expert and Manager and Advisor, this will help monitor patient progress actively and address any worsening conditions promptly.\n2. Train staff on empathy and active listening: The Communication Expert recommends implementing mandatory training sessions focused on empathy and active listening for healthcare providers to demonstrate genuine concern for patients' well-being.\n3. Provide language interpretation services: According to the Communication Expert, this will bridge communication gaps between doctors and non-native speaking patients.\n4. Review scheduling practices: The Manager and Advisor suggest reviewing scheduling practices to optimize patient flow and reduce waiting periods.\n5. Maintain high standards for cleanliness: According to the Health & IT Process Expert, maintaining a clean environment contributes positively to patient experience.\n6. Continue emphasizing clear explanations and empathetic interactions: The Communication Expert recommends continuing to prioritize clarity and empathy in interactions with patients.\n\nAdditionally, consider implementing digital check-in options and providing real-time updates on estimated wait times communicated via digital screens or mobile notifications to enhance the patient experience.\n\nTo address specific issues:\n- For patients experiencing language barriers: Provide immediate measures for language interpretation services and ongoing training programs for staff.\n- For patients with long wait times: Review scheduling practices, implement a system for real-time updates on estimated wait times, and consider digital check-in options.\n- For patients expressing frustration due to wait time: Validate their experience, express empathy, and provide practical strategies for managing future appointments.\n\nBy implementing these suggestions, you can improve your workflow, enhance patient satisfaction, and maintain high standards of care."
    },
    "display_patient_feedback": {
        "question": "Please display the patient feedback.",
        "answer": "The patient feedback is as follows:\n\nPositive:\n- \"I can't thank the team enough for their amazing work. I was seen on time, and everyone was so kind. I'm feeling great!\" (Date: 08-09-2024)\n- \"The clinic was clean and the staff was efficient. The appointment went as expected.\" (Date: 23-07-2024)\n- \"The doctor was fantastic! They explained everything clearly and made me feel at ease. Highly recommend\" (Date: 09-10-2024)\n- \"What a pleasant experience! The nurse was so gentle, and the doctor was very thorough. I'm impressed!\" (Date: 05-10-2024)\n\nNeutral:\n- \"The visit was okay. The staff was polite, but the wait was a bit long\" (Date: 01-10-2024)\n\nNegative:\n- \"Absolute lack of interest in the patient's evolution and worsening\" (Date: 01-10-2024)\n- \"I don't understand this doctor. I think it is a problem with the language\" (Date: 23-07-2024)\n\nKey issues identified by specialists include:\n- Lack of interest in patient’s evolution and worsening condition, according to the Patient Experience Expert.\n- Language barrier causing misunderstanding between doctor and patient, according to the Communication Expert.\n- Long wait times, according to the Health & IT Process Expert.\n\nRecommendations from various specialists are as follows:\n- Implement regular follow-up protocols to monitor patient progress actively, according to the Manager and Advisor.\n- Provide language interpretation services during consultations, according to the Communication Expert.\n- Review scheduling practices to optimize patient flow and reduce waiting periods, according to the Manager and Advisor."
    },
    "overall_patient_feedback_trend": {
        "question": "What's the overall patient feedback trend over time?",
        "answer": "The overall patient feedback trend over time indicates a mix of positive and negative experiences. According to the Patient Experience Expert, there is a high urgency level for addressing issues related to lack of interest in patient evolution and worsening conditions, as well as language barriers causing misunderstandings.\n\nPositive feedback accounts for approximately 60% of the responses, highlighting strengths such as timely appointments, kindness of staff, cleanliness of the clinic, efficiency of staff, clear explanations by doctors, and gentle care from nurses. According to the Health & IT Process Expert, maintaining these positive practices through ongoing training programs is essential for consistent patient experiences.\n\nNegative feedback (around 20%) points out areas that need improvement, including lack of interest in patient evolution, language barriers, long wait times, and poor communication quality. According to the Communication Expert, establishing a structured communication protocol emphasizing patient engagement, regular updates, and empathetic interactions can help rebuild trust and improve patient outcomes.\n\nNeutral feedback (around 20%) suggests subtle frustration due to wait times but also acknowledges positive aspects such as efficiency and cleanliness. According to the Clinical Psychologist, validating patients' experiences and emotions is crucial in addressing these concerns and fostering a supportive environment.\n\nTo address these trends and improve patient satisfaction, consider implementing regular follow-up protocols, providing language interpretation services, optimizing scheduling practices, maintaining high standards for cleanliness, and emphasizing clear explanations and empathetic interactions during consultations. According to the Manager and Advisor, conducting mandatory training sessions focused on empathy and active listening can also help healthcare providers better engage with patients.\n\nBy addressing these areas of improvement and reinforcing positive practices, you can enhance patient satisfaction and overall experience within your healthcare setting."
    }
}


def rag_bot_component():
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "AI Skills Overview",
        "Quick Wins",
        "Inefficiencies Analysis",
        "Workflow Improvement",
        "Patient Feedback",
        "Feedback Trend"
    ])

    with tab1:
        st.header("AI Skills Overview")
        st.image("assets/agents/ragbot1.png", caption="AI Skills Overview", use_column_width=True)
        if st.button("Show Answer"):
            st.write(data["what_can_you_do"]["answer"])

    with tab2:
        st.header("Quick Wins for Patient Satisfaction")
        st.image("assets/agents/ragbot2.png", caption="Quick Wins", use_column_width=True)
        if st.button("Show Answer", key="quick_wins"):
            st.write(data["quick_wins_to_improve_patient_satisfaction"]["answer"])

    with tab3:
        st.header("Inefficiencies Analysis")
        st.image("assets/agents/ragbot3.png", caption="Inefficiencies Analysis", use_column_width=True)
        if st.button("Show Answer", key="inefficiencies"):
            st.write(data["biggest_inefficiencies"]["answer"])

    with tab4:
        st.header("Workflow Improvement Advice")
        st.image("assets/agents/ragbot4.png", caption="Workflow Improvement", use_column_width=True)
        if st.button("Show Answer", key="workflow"):
            st.write(data["advice_on_improving_workflow"]["answer"])

    with tab5:
        st.header("Patient Feedback Display")
        st.image("assets/agents/ragbot5.png", caption="Patient Feedback", use_column_width=True)
        if st.button("Show Answer", key="feedback"):
            st.write(data["display_patient_feedback"]["answer"])

    with tab6:
        st.header("Overall Patient Feedback Trend")
        st.image("assets/agents/ragbot6.png", caption="Feedback Trend", use_column_width=True)
        if st.button("Show Answer", key="feedback_trend"):
            st.write(data["overall_patient_feedback_trend"]["answer"])

# Executa o componente do RAG Bot
rag_bot_component()
