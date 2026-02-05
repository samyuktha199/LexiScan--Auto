import os
import spacy
import pdfplumber
from ner.postprocess import process_entities

MODEL_PATH = "models/legal_ner_model"

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text
    

def run_pipeline(pdf_path):
    print("Loading NER model...")
    nlp = spacy.load(MODEL_PATH)

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("Running NER...")
    doc = nlp(text)

    print("Post-processing entities...")
    structured_output = process_entities(doc)

    return structured_output


if __name__ == "__main__":
    sample_pdf = "sample_contract.pdf"  # replace with your test PDF
    output = run_pipeline(sample_pdf)

    print("\nFINAL STRUCTURED OUTPUT:\n")
    print(output)
