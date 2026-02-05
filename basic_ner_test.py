import spacy
import json

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

text = """
This Agreement is made on January 12, 2023 between
ABC Technologies Pvt Ltd and XYZ Financial Services.
The total contract value is $250,000.
"""

doc = nlp(text)

# Structured entity output
entities = {
    "dates": [],
    "organizations": [],
    "amounts": []
}

for ent in doc.ents:
    if ent.label_ == "DATE":
        entities["dates"].append(ent.text)
    elif ent.label_ == "ORG":
        entities["organizations"].append(ent.text)
    elif ent.label_ == "MONEY":
        entities["amounts"].append(ent.text)

print("Structured Entity Output:\n")
print(json.dumps(entities, indent=4))
