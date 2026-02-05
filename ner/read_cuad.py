# read_cuad.py
import os
import json

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct path to CUAD dataset
cuad_path = os.path.join(BASE_DIR, "data", "CUAD_v1", "CUAD_v1.json")

# Load CUAD JSON
with open(cuad_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Basic verification prints
print("Keys:", data.keys())
print("Number of contracts:", len(data["data"]))

sample = data["data"][0]
print("\nSample contract title:")
print(sample["title"])
