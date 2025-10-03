import json
import os
from collections import Counter

README_PATH = "README.md"
LEADERBOARD_START_MARKER = "<!-- LEADERBOARD_START -->"
LEADERBOARD_END_MARKER = "<!-- LEADERBOARD_END -->"
INKS_DIR = "json_data/inks"

def load_local_inks_data():
    """Loads all individual ink JSON files from the local directory."""
    inks_data = []
    if not os.path.exists(INKS_DIR):
        print(f"Error: Inks directory not found at {INKS_DIR}")
        return None

    for filename in os.listdir(INKS_DIR):
        if filename.endswith('.json'):
            file_path = os.path.join(INKS_DIR, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    inks_data.append(json.load(f))
            except Exception as e:
                print(f"Error reading or parsing {file_path}: {e}")
    return inks_data

def generate_leaderboard(inks_data):
    # This function's logic remains the same
    if not inks_data:
        return "No ink data available to generate leaderboard."
    credits = [ink.get("credit", "").strip() for ink in inks_data if ink.get("credit")]
    if not credits:
        return "No credit information found in inks data."
    credit_counts = Counter(credits)
    top_10 = credit_counts.most_common(10)
    leaderboard_markdown = "### Top 10 Contributors\n\n"
    leaderboard_markdown += "| Rank | Contributor | Inks Added |\n"
    leaderboard_markdown += "|---|---|---|
"
"
    for i, (contributor, count) in enumerate(top_10):
        leaderboard_markdown += f"| {i + 1} | {contributor} | {count} |\n"
    return leaderboard_markdown

def update_readme(leaderboard_content):
    # This function's logic remains the same
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()
        start_index = readme_content.find(LEADERBOARD_START_MARKER)
        end_index = readme_content.find(LEADERBOARD_END_MARKER)
        if start_index == -1 or end_index == -1:
            print("Error: Leaderboard markers not found in README.md.")
            return
        start_index += len(LEADERBOARD_START_MARKER)
        new_readme_content = (
            readme_content[:start_index] + "\n\n" + leaderboard_content + "\n\n" + readme_content[end_index:]
        )
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme_content)
        print("Successfully updated README.md with the new leaderboard.")
    except Exception as e:
        print(f"Error updating README.md: {e}")

def main():
    inks_data = load_local_inks_data()
    if inks_data:
        leaderboard = generate_leaderboard(inks_data)
        update_readme(leaderboard)

if __name__ == "__main__":
    main()