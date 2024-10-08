DATA_DIR = "data_reports_json"

AGENT_DESCRIPTIONS = {
    "Patient Experience Expert (Phi Model)": "I’m the Patient Experience Expert. My job is to analyze patient feedback, pinpoint key issues, gauge emotional intensity, and assess the urgency of the concerns. I run on Microsoft’s Phi-3.5 Mini, a 3.8 billion parameter model, which excels at reasoning and language understanding. My goal is to turn patient feedback into actionable insights that improve the overall healthcare experience. I look forward to enhancing your services.",
    "Health & IT Process Expert (Gemma Model)": "I’m the Health & IT Process Expert. My role is to map out the entire patient journey, using BPMN (Business Process Model and Notation) to spot inefficiencies and recommend improvements that benefit all stakeholders. Powered by Google’s Gemma 2, a 9 billion parameter model, I strike a perfect balance between performance and efficiency. My mission is to streamline healthcare workflows and integrate better processes and technology. I’m confident you’ll appreciate the results I deliver.",
    "Clinical Psychologist (OpenHermes Model)": "I’m the Clinical Psychologist. I specialize in analyzing patients' emotional states based on their feedback and crafting personalized psychological support strategies. I leverage the OpenHermes model by NousResearch, which is designed for advanced context understanding and coherent response generation. My aim is to provide effective emotional support, helping patients cope with stressful situations in a thoughtful and empathetic way. I’m here to ensure patients feel heard and supported.",
    "Communication Expert (Mistral Model)": "I’m the Communication Expert. My expertise lies in evaluating the quality of communication between healthcare professionals and patients, identifying communication gaps, and suggesting improvements. I operate on Mistral NeMo, developed by Mistral AI and NVIDIA, a 12 billion parameter model with an impressive 128k token context window. This allows me to dive deep into interactions and find ways to improve clarity and empathy in communication. My goal is to enhance communication strategies that leave patients feeling understood and valued.",
    "Manager and Advisor (Qwen Model)": "I’m the Manager and Advisor. I consolidate feedback from various experts, cut out redundancies, and produce clear, actionable reports with strategic recommendations. I use Alibaba’s Qwen2 model, with 7 billion parameters and support for 29 languages, along with an extended 128k token context window. My focus is to deliver practical, data-driven reports that help implement meaningful improvements across healthcare processes. I look forward to helping your team take the next step.",
    "Data Analyst (LLaVA Model)": "I’m the Data Analyst. I organize and manage data generated by other agents, ensuring efficient storage and accessibility in the backend. Powered by the LLaVA model, built on Meta's LLaMA architecture with 7 billion parameters, I handle tasks like visual question answering and image captioning, making me versatile for multimodal use. I also monitor agent performance and ensure data integrity. My goal is to streamline data management and boost system efficiency. I look forward to supporting your team's continuous improvements.",
    "Output Consistency Agent (LLaMA Model)": "I’m the Output Consistency Agent. My job is to harmonize the outputs of all agents, ensuring consistency in structure, grammar, and formatting. Powered by Meta’s LLaMA 3.1 8B, a state-of-the-art model excelling in natural language tasks like text generation and question answering, I review and correct spelling, grammar, and unwanted characters. I ensure that reports in TXT format are clear for users, while JSON outputs are properly formatted for backend integration. My goal is to deliver clean, structured data for smooth processing. I look forward to improving the accuracy of your data."
}

AI_MODELS = {
    "llama_model": "Meta's Llama 3.1 8B is a state-of-the-art language model known for its balance between performance and efficiency.",
    "hermes_model": "NousResearch's Hermes 3 8B is designed for advanced reasoning and conversation.",
    "phi_model": "Microsoft's Phi-3.5 Mini 3.8B is a lightweight model built for high performance in reasoning and language comprehension tasks.",
    "gemma_model": "Google's Gemma 2 9B strikes an excellent balance between size and performance.",
    "openhermes_model": "OpenHermes by NousResearch is built for superior text generation and assistant capabilities.",
    "mistral_model": "Mistral AI's Mistral NeMo 12B features a 128k token context window.",
    "quwen_model": "Alibaba's Qwen2 7B is a multilingual model supporting 29 languages with a 128k token context window.",
    "llava_model": "LLaVA (Large Language and Vision Assistant) 7B integrates visual and language understanding."
}

AGENTS = [
    "Patient Experience Expert (Phi Model)",
    "Health & IT Process Expert (Gemma Model)",
    "Clinical Psychologist (OpenHermes Model)",
    "Communication Expert (Mistral Model)",
    "Manager and Advisor (Qwen Model)",
    "Data Analyst (LLaVA Model)",
    "Output Consistency Agent (LLaMA Model)"
]

# Adicione o dicionário de mapeamento
AGENT_NAME_MAPPING = {
    "Patient Experience Expert (Phi Model)": "Patient Experience Expert",
    "Health & IT Process Expert (Gemma Model)": "Health & IT Process Expert with expertise in Business Process Model and Notation (BPMN)",
    "Clinical Psychologist (OpenHermes Model)": "Clinical Psychologist",
    "Communication Expert (Mistral Model)": "Communication Expert",
    "Manager and Advisor (Qwen Model)": "Manager and Advisor"
}

# utils/config.py

# Dicionário de equivalência para os títulos dos relatórios dos agentes
FIELD_EQUIVALENCE = {
    # Patient Experience Expert
    "Sentiment_Patient_Experience_Expert": "Sentiment",
    "Emotional_Intensity_Patient_Experience_Expert": "Emotional Intensity",
    "Urgency_Level_Patient_Experience_Expert": "Urgency Level",
    "Key_Issues_Patient_Experience_Expert": "Key Issues",

    # Health & IT Process Expert
    "Patient_Journey_Health_IT_Process_Expert": "Patient Journey",
    "Inefficiencies_Healthcare_Process_Health_IT_Process_Expert": "Inefficiencies in Healthcare Process",
    "Improvement_Suggestions_Healthcare_Process_Health_IT_Process_Expert": "Improvement Suggestions",

    # Clinical Psychologist
    "Emotional_State_Clinical_Psychologist": "Emotional State",
    "Support_Strategy_Clinical_Psychologist": "Support Strategy",
    "Suggested_Approach_Clinical_Psychologist": "Suggested Approach",

    # Communication Expert
    "Communication_Quality_Communication_Expert": "Communication Quality",
    "Issues_Identified_Communication_Expert": "Issues Identified",
    "Suggested_Improvements_Communication_Expert": "Suggested Improvements",
    "Final_Recommendation_Communication_Expert": "Final Recommendation",

    # Manager and Advisor
    "Key_Issues_Manager_and_Advisor": "Key Issues",
    "Recommendations_Manager_and_Advisor": "Recommendations"
}

# Outras variáveis de configuração (se houver)


