from utils.regex_extractors import (
    extract_dates,
    extract_amounts,
    extract_parties
)
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import os
import spacy

from ocr.ocr_pipeline import extract_text_from_pdf
from ner.postprocess import process_entities

app = FastAPI(
    title="LexiScan Auto",
    description="Legal Document Entity Extraction API",
    version="1.0"
)

# Load trained NER model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "legal_ner_model")

nlp = spacy.load(MODEL_PATH)

# Add sentencizer if missing
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")

@app.post("/extract")
async def extract_entities(
    file: UploadFile = File(None),
    text: str = None
):
    try:
        # -------- INPUT HANDLING --------
        if file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(await file.read())
                pdf_path = tmp.name

            extracted_text = extract_text_from_pdf(pdf_path)
            os.remove(pdf_path)

        elif text:
            extracted_text = text

        else:
            return JSONResponse(
                status_code=400,
                content={"error": "Please upload a PDF file or provide text"}
            )

        # -------- NER (ML) --------
        doc = nlp(extracted_text)
        ml_entities = process_entities(doc)

        # -------- RULE-BASED (REGEX) --------
        dates = extract_dates(extracted_text)
        amounts = extract_amounts(extracted_text)
        parties = extract_parties(extracted_text)

        # -------- FINAL STRUCTURED OUTPUT --------
        final_output = {
            "status": "success",
            "document_type": "Legal / Offer Document",
            "entities": {
                "parties": parties,
                "dates": dates,
                "amounts": amounts,
                "termination_clause": ml_entities.get("termination", [])
            }
        }

        return final_output

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
