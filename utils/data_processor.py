import os
import pandas as pd
import json
from utils.config import DATA_DIR

def normalize_column_names(data):
    normalized_data = {}
    for key, value in data.items():
        normalized_key = key.lower().replace(' ', '_')
        normalized_data[normalized_key] = value
    return normalized_data

def cleanup_data_directory():
    import os
    from utils.config import DATA_DIR
    
    print(f"Cleaning up {DATA_DIR}...")
    for filename in os.listdir(DATA_DIR):
        if not filename.endswith('.json'):
            file_path = os.path.join(DATA_DIR, filename)
            try:
                os.remove(file_path)
                print(f"Removed: {filename}")
            except Exception as e:
                print(f"Error removing {filename}: {str(e)}")
    
    print("Cleanup completed.")

def extract_and_stack_data():
    print(f"Starting extract_and_stack_data function")
    print(f"Full path of DATA_DIR: {os.path.abspath(DATA_DIR)}")
    
    cleanup_data_directory()  # Call the cleanup function before processing
    
    if not os.path.exists(DATA_DIR):
        print(f"Error: {DATA_DIR} does not exist")
        return pd.DataFrame()
    
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    if not files:
        print(f"Error: No feedback files found in {DATA_DIR}")
        return pd.DataFrame()
    
    print(f"Found {len(files)} feedback files")

    data = []
    for file in files:
        file_path = os.path.join(DATA_DIR, file)
        print(f"Processing file: {os.path.abspath(file_path)}")
        try:
            with open(file_path, "r") as f:
                feedback_data = json.load(f)
            feedback_data = normalize_column_names(feedback_data)
            feedback_data['feedback_id'] = os.path.splitext(file)[0]
            data.append(feedback_data)
            print(f"Processed feedback {feedback_data['feedback_id']}")
        except Exception as e:
            print(f"Error processing file {file}: {str(e)}")
    
    print(f"Total extracted data entries: {len(data)}")
    
    if not data:
        print("Error: No data extracted from files")
        return pd.DataFrame()
    
    df = pd.DataFrame(data)
    
    # Print column names and first few rows
    print("DEBUG: DataFrame columns:")
    print(df.columns)
    print("DEBUG: First few rows of the DataFrame:")
    print(df.head())
    
    if df.empty:
        print("Error: DataFrame is empty")
    else:
        print(f"Created DataFrame with shape: {df.shape}")
    
    df.to_csv("stacked_data.csv", index=False)
    print("Saved data to stacked_data.csv")
    print("First 5 lines of stacked_data.csv:")
    with open("stacked_data.csv", "r") as f:
        print(f.read(500))  # Print first 500 characters
    return df

def read_feedback_data(feedback_id):
    file_path = os.path.join(DATA_DIR, f"{feedback_id}.json")
    try:
        with open(file_path, "r") as f:
            feedback_data = json.load(f)
        feedback_data = normalize_column_names(feedback_data)
        print(f"DEBUG: Feedback data for {feedback_id}:")
        print(json.dumps(feedback_data, indent=2))
        
        # Check for required keys
        required_keys = ["patient_feedback", "feedback"]
        if not any(key in feedback_data for key in required_keys):
            print(f"WARNING: None of the required keys {required_keys} found in the feedback data.")
            return {"error": f"Invalid feedback data structure for {feedback_id}."}
        
        return feedback_data
    except FileNotFoundError:
        print(f"ERROR: Feedback file not found: {file_path}")
        return {"error": f"Feedback {feedback_id} not found."}
    except json.JSONDecodeError:
        print(f"ERROR: Error decoding JSON in file: {file_path}")
        return {"error": f"Error reading feedback {feedback_id}. Invalid JSON format."}
    except Exception as e:
        print(f"ERROR: Unexpected error reading feedback data: {str(e)}")
        return {"error": f"Unexpected error reading feedback {feedback_id}."}
