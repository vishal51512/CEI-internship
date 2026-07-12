import fitz

def load_pdf(path):
    doc = fitz.open(path)

    pages = []

    for page_number, page in enumerate(doc):
        text = page.get_text()

        if text.strip():
            pages.append({
                "page": page_number + 1,
                "text": text
            })

    return pages