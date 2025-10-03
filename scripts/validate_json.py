import json
import sys
import os

def validate_json_file(file_path):
    """Validates a single JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"OK: {file_path} is valid.")
        return True
    except json.JSONDecodeError as e:
        print(f"ERROR in {file_path}: {e}")
        return False
    except FileNotFoundError:
        print(f"ERROR: {file_path} not found.")
        return False

def main():
    """Validates all JSON files in the data directories."""
    has_error = False
    data_dirs = ['json_data/inks', 'json_data/pens']

    for data_dir in data_dirs:
        if not os.path.exists(data_dir):
            print(f"Warning: Directory not found, skipping: {data_dir}")
            continue

        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                if not validate_json_file(file_path):
                    has_error = True

    if has_error:
        print("\nValidation failed for one or more files.")
        sys.exit(1)
    else:
        print("\nAll JSON files validated successfully.")

if __name__ == "__main__":
    main()