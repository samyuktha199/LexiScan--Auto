import spacy
import random
import os
import sys
from spacy.training import Example

# -------------------------------
# Load training data
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from data.spacy_train_data import TRAIN_DATA

# -------------------------------
# Create blank English model
# -------------------------------
nlp = spacy.blank("en")

# -------------------------------
# Add NER pipeline safely
# -------------------------------
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# -------------------------------
# Add entity labels
# -------------------------------
for _, annotations in TRAIN_DATA:
    for start, end, label in annotations.get("entities", []):
        ner.add_label(label)

# -------------------------------
# Initialize pipeline
# -------------------------------
nlp.initialize()

# -------------------------------
# Training loop
# -------------------------------
EPOCHS = 10

for epoch in range(EPOCHS):
    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update(
            [example],
            drop=0.3,
            losses=losses
        )

    print(f"Epoch {epoch + 1}/{EPOCHS} - Losses: {losses}")

# -------------------------------
# Save model
# -------------------------------
model_dir = os.path.join(BASE_DIR, "models", "legal_ner_model")
os.makedirs(model_dir, exist_ok=True)
nlp.to_disk(model_dir)

print("\n✅ Training complete")
print("📁 Model saved at:", model_dir)
