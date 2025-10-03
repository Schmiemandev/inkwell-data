# Inkwell Data

This repository serves as the public, community-driven database for the Inkwell mobile app. It contains a curated collection of fountain pen and ink data, which is utilized by the Inkwell app to provide users with a comprehensive and up-to-date resource for tracking their collections.

<!-- LEADERBOARD_START -->

### Top 10 Contributors

| Rank | Contributor | Inks Added |
|---|---|---|
| 1 | John Doe | 1 |


<!-- LEADERBOARD_END -->

## Purpose

The main goal of this repository is to:
- **Centralize Ink Data:** Provide a single, accessible source for fountain pen ink information.
- **Support the Inkwell App:** Enable the Inkwell mobile application to fetch and display a wide range of ink details, enhancing the user experience.
- **Foster Community Contribution:** Allow enthusiasts to contribute new ink data, corrections, and updates, ensuring the database remains current and accurate.

## Data Structure

The data is stored as individual JSON files within the json_data/inks/ and json_data/pens/ directories. Each file
represents a single ink or pen object.

On every change to the main branch, a GitHub Action automatically compiles these individual files into
json_data/inks.json and json_data/pens.json. The Inkwell app consumes these compiled files.

### Example Entry

An individual file, like json_data/inks/diamine-writers-blood.json, contains a single object:

```json
{
  "id": "some-uuid-provided-by-app",
  "name": "Writer's Blood",
  "brand": "Diamine",
  "color": "#5a0000",
  "shading": true,
  "sheen": false,
  "shimmer": null,
  "waterResistance": true,
  "flow": "Wet",
  "notes": "A very dark red ink with high saturation.",
  "credit": "Jane Doe",
  "purchase link": "testlink2.com"
}
```

## Contributing

I welcome contributions from the fountain pen community! Please download the app on the Play Store to contribute to this database with your own collection.

Please ensure your contributions are accurate and well-researched. All submissions will be reviewed before being merged.

## Scripts

This repository includes a `scripts` directory containing utility scripts:

- `validate_json.py`: This script validates all the individual JSON files in the `json_data/inks` and `json_data/pens` directories.
- `validate_compiled_json.py`: This script validates the final `json_data/inks.json` and `json_data/pens.json` files to ensure they are well-formed.
- `generate_leaderboard.py`: This script reads the local ink data and updates the contributor leaderboard in this `README.md`.

## Usage in Inkwell App

The Inkwell mobile application fetches the compiled `json_data/inks.json` and `json_data/pens.json` files from this repository on startup. This allows the app to stay updated with the latest data without requiring app updates.
