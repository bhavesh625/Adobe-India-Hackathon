from pathlib import Path
from pdf_processor.reader import load_pdf
from pdf_processor.extractor import extract_headings
from pdf_processor.writer import save_output

INPUT_DIR = Path("/app/input")
OUTPUT_DIR = Path("/app/output")

def process_all_pdfs():
    for pdf_path in INPUT_DIR.glob("*.pdf"):
        layout_data = load_pdf(pdf_path)
        result_json = extract_headings(layout_data)
        save_output(result_json, OUTPUT_DIR / f"{pdf_path.stem}.json")

if __name__ == "__main__":
    process_all_pdfs()
