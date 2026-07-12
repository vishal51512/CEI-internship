from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

def split_pages(pages, filename):
    chunks = []

    for page in pages:
        texts = splitter.split_text(page["text"])

        for chunk in texts:
            chunks.append({
                "text": chunk,
                "page": page["page"],
                "source": filename
            })

    return chunks