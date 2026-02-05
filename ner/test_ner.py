from postprocess import process_entities
import spacy
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "legal_ner_model")

print("Loading model from:", MODEL_PATH)

nlp = spacy.load(MODEL_PATH)

# Add sentence boundary detection if missing
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")


test_text="""
This Agreement is made on 12/01/2021 between Alpha Corp and Beta LLC.
The total consideration is $1,200,000.
This Agreement may be terminated with 30 days notice.
"""


doc = nlp(test_text)

print("\nDetected Entities:\n")
for ent in doc.ents:
    structured_output = process_entities(doc)

print("\nStructured JSON Output:\n")
print(structured_output)

import json

with open("sample_output.json", "w", encoding="utf-8") as f:
    json.dump(structured_output, f, indent=4)

print("✅ Saved output to sample_output.json")
