from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def load_pdf(path):
    content = []
    for page_layout in extract_pages(path):
        page_text = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    font_sizes = []
                    text = text_line.get_text().strip()
                    if not text: continue
                    for char in text_line:
                        if isinstance(char, LTChar):
                            font_sizes.append(round(char.size, 1))
                    if font_sizes:
                        avg_font = sum(font_sizes) / len(font_sizes)
                        page_text.append((text, avg_font))
        content.append(page_text)
    return content
