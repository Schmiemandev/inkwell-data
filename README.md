# Inkwell Data

This repository serves as the public, community-driven database for the Inkwell mobile app. It contains a curated collection of fountain pen ink data, primarily in the `inks.json` file, which is utilized by the Inkwell app to provide users with a comprehensive and up-to-date resource for tracking their ink collections.

<!-- LEADERBOARD_START -->

### Top 10 Contributors

| Rank | Contributor | Inks Added |
|---|---|---|
| 1 | Your Name Here | 1 |


<!-- LEADERBOARD_END -->

## Purpose

The main goal of this repository is to:
- **Centralize Ink Data:** Provide a single, accessible source for fountain pen ink information.
- **Support the Inkwell App:** Enable the Inkwell mobile application to fetch and display a wide range of ink details, enhancing the user experience.
- **Foster Community Contribution:** Allow enthusiasts to contribute new ink data, corrections, and updates, ensuring the database remains current and accurate.

## Data Structure

The core data is stored in `inks.json`. This file is structured as an array of ink objects, with each object containing properties such as:
- `name`: The name of the ink.
- `brand`: The brand of the ink.
- `color`: The color description of the ink.
- `shading`: (Optional) Boolean indicating if the ink exhibits shading.
- `sheen`: (Optional) Boolean indicating if the ink exhibits sheen.
- `shimmer`: (Optional) Boolean indicating if the ink exhibits shimmer.
- `waterResistance`: (Optional) Boolean indicating if the ink has water resistance.
- `flow`: (Optional) String indicating the flow (e.g., "Dry", "Medium", "Wet").
- `notes`: (Optional) Any additional notes about the ink.
- `credit`: (Optional) Name of the contributor.

Example entry in `inks.json`:
```json
[
  {
    "name": "Kon-Peki",
    "brand": "Pilot Iroshizuku",
    "color": "Blue",
    "shading": true,
    "sheen": false,
    "shimmer": false,
    "waterResistance": false,
    "flow": "Wet",
    "notes": "A vibrant sky blue.",
    "credit": "John Doe"
  }
]
```

## Contributing

I welcome contributions from the fountain pen community! To add new inks or update existing entries

Please ensure your contributions are accurate and well-researched. All submissions will be reviewed before being merged.

## Usage in Inkwell App

The Inkwell mobile application fetches the `inks.json` file from this repository on startup to provide users with a comprehensive list of inks for their collection tracking. This allows the app to stay updated with the latest ink data without requiring app updates.
