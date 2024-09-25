import os
import json
import re
import pandas as pd

# Define the field equivalence dictionary
FIELD_EQUIVALENCE = {
    # Patient Experience Expert
    'Sentiment_Patient_Experience_Expert': 'Sentiment',
    'Emotional_Intensity_Patient_Experience_Expert': 'Emotional Intensity',
    'Urgency_Level_Patient_Experience_Expert': 'Urgency Level',
    'Key_Issues_Patient_Experience_Expert': 'Key Issues',
    # Health & IT Process Expert
    'Patient_Journey_Health_IT_Process_Expert': 'Patient Journey',
    'Inefficiencies_Healthcare_Process_Health_IT_Process_Expert': 'Inefficiencies in Healthcare Process',
    'Improvement_Suggestions_Healthcare_Process_Health_IT_Process_Expert': 'Improvement Suggestions',
    # Clinical Psychologist
    'Emotional_State_Clinical_Psychologist': 'Emotional State',
    'Support_Strategy_Clinical_Psychologist': 'Support Strategy',
    'Suggested_Approach_Clinical_Psychologist': 'Suggested Approach',
    # Communication Expert
    'Communication_Quality_Communication_Expert': 'Communication Quality',
    'Issues_Identified_Communication_Expert': 'Issues Identified',
    'Suggested_Improvements_Communication_Expert': 'Suggested Improvements',
    'Final_Recommendation_Communication_Expert': 'Final Recommendation',
    # Manager and Advisor
    'Key_Issues_Manager_and_Advisor': 'Key Issues',
    'Recommendations_Manager_and_Advisor': 'Recommendations'
}

def load_json_files(data_folder):
    data = []
    if not os.path.exists(data_folder):
        return data

    for file_name in os.listdir(data_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data.append({"name": file_name, "content": json.load(f)})
            except (UnicodeDecodeError, json.JSONDecodeError):
                print(f"Error loading file: {file_name}")
    return data

def read_txt_report(report_name):
    txt_file_path = os.path.join('data_reports', f"{report_name}.txt")
    if os.path.exists(txt_file_path):
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "TXT report not found."

def convert_time_to_seconds(time_str):
    minutes = 0
    seconds = 0
    time_parts = re.findall(r'\d+\s+\w+', time_str)
    for part in time_parts:
        value, unit = part.split()
        if 'minute' in unit:
            minutes = int(value)
        elif 'second' in unit:
            seconds = int(value)
    return minutes * 60 + seconds

def get_agent_report(feedback, agent_name):
    return next((agent for agent in feedback['content']['agents'] if agent['agent_name'] == agent_name), None)

def prepare_table_data(data):
    table_data = []
    for feedback in data:
        feedback_name = feedback['name']
        patient_feedback = feedback['content'].get('patient_feedback', 'No feedback available.')
        
        for agent in feedback['content']['agents']:
            agent_name = agent['agent_name']
            display_name = "Health & IT Process Expert" if agent_name.startswith("Health & IT Process Expert") else agent_name
            for key, value in agent['response'].items():
                display_key = FIELD_EQUIVALENCE.get(key, key)
                table_data.append({
                    "Feedback": feedback_name,
                    "Patient Feedback": patient_feedback,
                    "Agent": display_name,
                    "Field": display_key,
                    "Value": value
                })
    return pd.DataFrame(table_data)

class PatientFeedbackAnalyzer:
    def __init__(self, data_folder='data_reports_json'):
        self.data = load_json_files(data_folder)

    def get_feedback_list(self):
        return [file['name'] for file in self.data]

    def get_agent_list(self):
        return list(set([agent['agent_name'] for file in self.data for agent in file['content']['agents']]))

    def get_feedback_data(self, feedback_name):
        return next((file for file in self.data if file['name'] == feedback_name), None)

    def get_agent_reports(self, mode, selected_item):
        if mode == "agent":
            return [
                {
                    "feedback_name": feedback['name'],
                    "agent_report": get_agent_report(feedback, selected_item)
                }
                for feedback in self.data
            ]
        elif mode == "feedback":
            return [
                {
                    "agent_name": agent['agent_name'],
                    "agent_report": agent
                }
                for agent in self.data[selected_item]['content']['agents']
            ]

    def get_table_data(self):
        return prepare_table_data(self.data)

    def get_txt_report(self, report_name):
        return read_txt_report(report_name)

    def get_patient_expert_data(self, agents_data):
        return next((agent for agent in agents_data if agent['agent_name'] == 'Patient Experience Expert'), None)

    def get_kpi_data(self, patient_expert):
        if patient_expert:
            kpi_data = patient_expert['response']
            return {
                'Sentiment': kpi_data.get('Sentiment_Patient_Experience_Expert', 'N/A'),
                'Emotional Intensity': kpi_data.get('Emotional_Intensity_Patient_Experience_Expert', 'N/A'),
                'Urgency Level': kpi_data.get('Urgency_Level_Patient_Experience_Expert', 'N/A')
            }
        return None

    def convert_time_to_seconds(self, time_str):
        return convert_time_to_seconds(time_str)
