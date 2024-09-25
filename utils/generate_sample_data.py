import os
from config import DATA_DIR

def generate_sample_data():
    print(f"Full path of DATA_DIR: {os.path.abspath(DATA_DIR)}")
    
    if not os.path.exists(DATA_DIR):
        print(f"Creating {DATA_DIR} directory")
        os.makedirs(DATA_DIR)

    print("Files in DATA_DIR before sample data generation:")
    files_before = os.listdir(DATA_DIR)
    print(files_before)

    # Rename existing report_*.txt files to feedback_*.txt
    for file in files_before:
        if file.startswith("report_") and file.endswith(".txt"):
            old_path = os.path.join(DATA_DIR, file)
            new_path = os.path.join(DATA_DIR, f"feedback_{file[7:]}")
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")

    # Generate new feedback files if they don't exist
    for i in range(1, 6):
        file_path = os.path.join(DATA_DIR, f"feedback_{i}.txt")
        if not os.path.exists(file_path):
            print(f"Creating file: {os.path.abspath(file_path)}")
            content = f"""Feedback {i}

Agent: Patient Experience Expert
This is a sample report for feedback {i} from the Patient Experience Expert.

Agent: Health & IT Process Expert
This is a sample report for feedback {i} from the Health & IT Process Expert.

Agent: Clinical Psychologist
This is a sample report for feedback {i} from the Clinical Psychologist.

Agent: Communication Expert
This is a sample report for feedback {i} from the Communication Expert.

Agent: Manager and Advisor
This is a sample report for feedback {i} from the Manager and Advisor.

Agent: Data Analyst
This is a sample report for feedback {i} from the Data Analyst.
"""
            with open(file_path, "w") as f:
                f.write(content)
            
            # Verification step
            if os.path.exists(file_path):
                print(f"File {file_path} created successfully.")
                print("File contents:")
                with open(file_path, "r") as f:
                    print(f.read())
            else:
                print(f"Error: Failed to create file {file_path}")
            
            print("--------------------")
    
    print("Files in DATA_DIR after sample data generation:")
    files_after = os.listdir(DATA_DIR)
    print(files_after)

if __name__ == "__main__":
    generate_sample_data()
