import json
import os
from fpdf import FPDF

# Define paths (Updated)
INKS_JSON_PATH = "json_data/inks.json"
PENS_JSON_PATH = "json_data/pens.json"
COLLECTIONS_DIR = "collections" # Renamed

# Output paths for the different reports (Updated)
INKS_COLLECTION_PATH = os.path.join(COLLECTIONS_DIR, "inks_collection.pdf")
PENS_COLLECTION_PATH = os.path.join(COLLECTIONS_DIR, "pens_collection.pdf")
COMBINED_COLLECTION_PATH = "inks_and_pens_collection.pdf" # Renamed

def load_json_data(file_path):
    """Loads JSON data from a file."""
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return []

def format_ink_data(ink):
    """Formats a single ink entry into a human-readable string, skipping empty fields."""
    lines = []

    def add_line(label, value):
        if value is not None and value != '' and value != [] and value != {}:
            if isinstance(value, bool):
                lines.append(f"  {label}: {'Yes' if value else 'No'}")
            else:
                lines.append(f"  {label}: {value}")

    lines.append(f"Ink Name: {ink.get('name', 'N/A')}")
    add_line("Brand", ink.get('brand'))
    add_line("Color", ink.get('color'))
    add_line("Shading", ink.get('shading'))
    add_line("Sheen", ink.get('sheen'))
    add_line("Shimmer", ink.get('shimmer'))
    add_line("Water Resistance", ink.get('waterResistance'))
    add_line("Flow", ink.get('flow'))
    add_line("Notes", ink.get('notes'))
    add_line("Credit", ink.get('credit'))
    add_line("Purchase Link", ink.get('purchase link'))

    return "\n".join(lines) + "\n\n"

def format_pen_data(pen):
    """Formats a single pen entry into a human-readable string, skipping empty fields."""
    lines = []

    def add_line(label, value):
        if value is not None and value != '' and value != [] and value != {}:
            if isinstance(value, bool):
                lines.append(f"  {label}: {'Yes' if value else 'No'}")
            else:
                lines.append(f"  {label}: {value}")

    lines.append(f"Pen Name: {pen.get('name', 'N/A')}")
    add_line("Brand", pen.get('brand'))

    return "\n".join(lines) + "\n\n"

def create_pdf_document(title):
    """Helper function to create a basic PDF document."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    return pdf

def add_entries_to_pdf(pdf, data, title, formatter_func):
    """Adds formatted entries to the PDF."""
    if data:
        pdf.set_font("Arial", "B", size=14)
        pdf.cell(200, 10, txt=title, ln=True, align="L")
        pdf.set_font("Arial", size=10)
        for entry in data:
            text = formatter_func(entry)
            pdf.multi_cell(0, 5, text)
            pdf.ln(5)

def generate_inks_collection(inks_data, output_path): # Renamed
    """Generates a PDF collection for inks only.""" # Renamed
    if not inks_data:
        print(f"No ink data found to generate inks collection at {output_path}.") # Renamed
        return

    os.makedirs(COLLECTIONS_DIR, exist_ok=True)
    pdf = create_pdf_document("Inkwell Inks Collection") # Renamed
    add_entries_to_pdf(pdf, inks_data, "Inks", format_ink_data)
    pdf.output(output_path)
    print(f"Inks collection generated at {output_path}") # Renamed

def generate_pens_collection(pens_data, output_path): # Renamed
    """Generates a PDF collection for pens only.""" # Renamed
    if not pens_data:
        print(f"No pen data found to generate pens collection at {output_path}.") # Renamed
        return

    os.makedirs(COLLECTIONS_DIR, exist_ok=True)
    pdf = create_pdf_document("Inkwell Pens Collection") # Renamed
    add_entries_to_pdf(pdf, pens_data, "Pens", format_pen_data)
    pdf.output(output_path)
    print(f"Pens collection generated at {output_path}") # Renamed

def generate_combined_collection(inks_data, pens_data, output_path): # Renamed
    """Generates a combined PDF collection for inks and pens.""" # Renamed
    if not inks_data and not pens_data:
        print(f"No ink or pen data found to generate combined collection at {output_path}.") # Renamed
        return

    pdf = create_pdf_document("Inkwell Combined Collection") # Renamed

    if inks_data:
        add_entries_to_pdf(pdf, inks_data, "Inks", format_ink_data)
        if pens_data:
            pdf.add_page()

    if pens_data:
        add_entries_to_pdf(pdf, pens_data, "Pens", format_pen_data)

    pdf.output(output_path)
    print(f"Combined collection generated at {output_path}") # Renamed

def main():
    """Loads data and generates all specified PDF collections.""" # Renamed
    inks_data = load_json_data(INKS_JSON_PATH)
    pens_data = load_json_data(PENS_JSON_PATH)

    generate_inks_collection(inks_data, INKS_COLLECTION_PATH) # Renamed
    generate_pens_collection(pens_data, PENS_COLLECTION_PATH) # Renamed
    generate_combined_collection(inks_data, pens_data, COMBINED_COLLECTION_PATH) # Renamed

if __name__ == "__main__":
    main()