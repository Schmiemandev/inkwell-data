import json
import requests
from collections import Counter
import os

# URL to the raw inks.json file
INKS_JSON_URL = "https://raw.githubusercontent.com/Schmiemandev/inkwell-data/main/inks.json"
README_PATH = "README.md"
LEADERBOARD_START_MARKER = "<!-- LEADERBOARD_START -->"
LEADERBOARD_END_MARKER = "<!-- LEADERBOARD_END -->"

def fetch_inks_data(url):
    """Fetches the inks.json data from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching inks data: {e}")
        return None

def generate_leaderboard(inks_data):
    """Generates a top 10 leaderboard from the inks data."""
    if not inks_data:
        return "No ink data available to generate leaderboard."

    credits = []
    for ink in inks_data:
        credit = ink.get("credit")
        if credit and isinstance(credit, str):
            credits.append(credit.strip())

    if not credits:
        return "No credit information found in inks data."

    credit_counts = Counter(credits)
    top_10 = credit_counts.most_common(10)

    leaderboard_markdown = "### Top 10 Contributors\n\n"
    leaderboard_markdown += "| Rank | Contributor | Inks Added |\n"
    leaderboard_markdown += "|---|---|---|\n"
    for i, (contributor, count) in enumerate(top_10):
        leaderboard_markdown += f"| {i + 1} | {contributor} | {count} |\n"

    return leaderboard_markdown

def update_readme(leaderboard_content):
    """Updates the README.md file with the new leaderboard content."""
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()

        start_index = readme_content.find(LEADERBOARD_START_MARKER)
        end_index = readme_content.find(LEADERBOARD_END_MARKER)

        if start_index == -1 or end_index == -1:
            print(f"Error: Leaderboard markers not found in {README_PATH}.")
            print("Please ensure '<!-- LEADERBOARD_START -->' and '<!-- LEADERBOARD_END -->' are present.")
            return False

        # Adjust start_index to include the start marker
        start_index += len(LEADERBOARD_START_MARKER)

        new_readme_content = (
            readme_content[:start_index]
            + "\n\n"
            + leaderboard_content
            + "\n\n"
            + readme_content[end_index:]
        )

        if new_readme_content == readme_content:
            print("README.md content is already up to date. No changes needed.")
            return False

        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme_content)
        print(f"Successfully updated {README_PATH} with the new leaderboard.")
        return True

    except Exception as e:
        print(f"Error updating README.md: {e}")
        return False

def main():
    inks_data = fetch_inks_data(INKS_JSON_URL)
    if inks_data:
        leaderboard = generate_leaderboard(inks_data)
        update_readme(leaderboard)

if __name__ == "__main__":
    main()
