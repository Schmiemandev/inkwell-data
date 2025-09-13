
import json
import sys

def validate_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {file_path}: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)
    print(f"{file_path} is a valid JSON file.")

if __name__ == "__main__":
    validate_json('json_data/inks.json')
