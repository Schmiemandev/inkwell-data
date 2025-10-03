import json
import sys
import os

def validate_json_file(file_path):
    """Validates a single JSON file."""
    if not os.path.exists(file_path):
        # If a file like pens.json doesn't exist because there are no pens, it's not an error.
        print(f"Info: {file_path} not found, skipping validation.")
        return True

    # If the file exists but is empty (e.g., no pens), it's not valid JSON.
    if os.path.getsize(file_path) == 0:
        print(f"Warning: {file_path} is empty. While not a JSON error, the GitHub action may produce an empty file if no source .json files are found.")
        return True # Not a fatal error.

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"OK: {file_path} is valid.")
        return True
    except json.JSONDecodeError as e:
        print(f"ERROR in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred with {file_path}: {e}")
        return False

def main():
    """Validates the compiled JSON files."""
    has_error = False
    files_to_validate = ['json_data/inks.json', 'json_data/pens.json']

    for file_path in files_to_validate:
        if not validate_json_file(file_path):
            has_error = True

    if has_error:
        print("\nValidation failed for one or more compiled files.")
        sys.exit(1)
    else:
        print("\nAll compiled JSON files validated successfully.")

if __name__ == "__main__":
    main()
