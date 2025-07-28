def extract_headings(pages):
    font_counter = {}
    for page in pages:
        for text, size in page:
            font_counter[size] = font_counter.get(size, 0) + 1

    sorted_fonts = sorted(font_counter.items(), key=lambda x: x[1], reverse=True)
    size_h1, size_h2, size_h3 = sorted_fonts[:3]
    title_font = sorted_fonts[0][0]

    output = { "title": "", "outline": [] }
    title_found = False

    for page_num, page in enumerate(pages, 1):
        for text, size in page:
            level = None
            if not title_found and size == title_font:
                output["title"] = text
                title_found = True
                continue
            if size == size_h1[0]:
                level = "H1"
            elif size == size_h2[0]:
                level = "H2"
            elif size == size_h3[0]:
                level = "H3"

            if level:
                output["outline"].append({
                    "level": level,
                    "text": text,
                    "page": page_num
                })
    return output
