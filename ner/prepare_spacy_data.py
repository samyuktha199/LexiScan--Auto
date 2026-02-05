import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "ner_data.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "spacy_train_data.py")

training_data = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if "\t" not in line:
            continue

        text, label = line.strip().split("\t")

        start = 0
        end = len(text)

        training_data.append(
            (text, {"entities": [(start, end, label)]})
        )

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("TRAIN_DATA = ")
    f.write(str(training_data))

print("SpaCy training data created")
print("Saved to:", OUTPUT_FILE)
print("Total samples:", len(training_data))
