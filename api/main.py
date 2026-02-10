from fastapi import FastAPI, UploadFile, File, Form
import tempfile
import os
import spacy

from ocr_pipeline import extract_text
from ner.postprocess import process_entities

app = FastAPI(title="LexiScan Auto API")

# Load custom-trained NER model
nlp = spacy.load("models/legal_ner_model")

# Add sentencizer to avoid doc.sents error
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")

@app.post("/extract")
async def extract_entities(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    if not text and not file:
        return {"error": "Provide text or PDF"}

    # If PDF file is uploaded
    if file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            pdf_path = tmp.name

        content = extract_text(pdf_path)  # OCR function
        os.remove(pdf_path)
    else:
        content = text

    # Run NER
    doc = nlp(content)

    # Post-process entities
    result = process_entities(doc)

    # Optionally save JSON output
    with open("final_output.json", "w", encoding="utf-8") as f:
        import json
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result
