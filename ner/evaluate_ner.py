import spacy
from spacy.training import Example
from spacy.scorer import Scorer

# Load trained NER model
nlp = spacy.load("models/legal_ner_model")

# Sample evaluation text (small is OK for demo)
text = "This agreement shall terminate on 07/09/1999 for $250000."

# Gold annotations (character offsets)
annotations = {
    "entities": [
        (32, 42, "DATE"),
        (47, 54, "MONEY")
    ]
}

# ---- CREATE DOCS ----

# Predicted doc
doc = nlp(text)

# Gold doc (manual, alignment-safe)
gold_doc = nlp.make_doc(text)

valid_ents = []
for start, end, label in annotations["entities"]:
    span = gold_doc.char_span(start, end, label=label)
    if span is not None:      # skip misaligned entities safely
        valid_ents.append(span)

gold_doc.ents = valid_ents

# ---- CREATE EXAMPLE ----
example = Example(doc, gold_doc)

# ---- SCORE ----
scorer = Scorer()
scores = scorer.score([example])
print("NER Evaluation Metrics:")
print(scores)


