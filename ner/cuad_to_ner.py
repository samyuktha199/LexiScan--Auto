import os
import json

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct paths
INPUT_PATH = os.path.join(BASE_DIR, "data", "CUAD_v1", "CUAD_v1.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "ner_data.txt")

def get_label(question):
    q = question.lower()
    if "party" in q:
        return "PARTY"
    if "effective date" in q or "date" in q:
        return "DATE"
    if "terminate" in q or "termination" in q:
        return "TERMINATION"
    if "dollar" in q or "$" in q or "payment" in q:
        return "MONEY"
    return None

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    cuad = json.load(f)

ner_samples = []

for doc in cuad["data"]:
    paragraph = doc["paragraphs"][0]

    for qa in paragraph["qas"]:
        label = get_label(qa["question"])
        if label is None:
            continue

        for ans in qa["answers"]:
            text = ans["text"].strip()
            if text:
                ner_samples.append(text + "\t" + label)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for line in ner_samples:
        f.write(line + "\n")

print("NER samples created:", len(ner_samples))
print("Saved to:", OUTPUT_PATH)
