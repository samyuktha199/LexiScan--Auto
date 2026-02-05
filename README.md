📄 LexiScan Auto – Legal Document Entity Extraction
📌 Overview

LexiScan Auto is an AI-powered system that automatically extracts structured information from legal and offer documents such as PDFs. It uses OCR, NLP, and a custom-trained NER model to identify key entities like parties, dates, monetary amounts, and termination clauses.

🎯 Objective

Manual review of legal documents is time-consuming and error-prone.
This project automates the process by converting unstructured legal text into structured JSON output for faster analysis.

✨ Key Features

PDF upload support

OCR-based text extraction

Custom-trained SpaCy NER model

Extraction of:

Parties (Company / Candidate)

Dates

Monetary amounts

Termination clauses

REST API using FastAPI

Dockerized for easy deployment

🛠️ Tech Stack

Python

FastAPI

SpaCy (Custom NER)

Tesseract OCR

Docker

Uvicorn

📂 Project Structure (High-Level)
LexiScan-Auto/
│
├── api/            # FastAPI application
├── ner/            # NER training & inference
├── ocr/            # OCR pipeline
├── pipeline/       # End-to-end pipeline
├── models/         # Trained NER model
├── data/           # Training data (CUAD-based)
├── Dockerfile
├── requirements.txt
└── README.md

▶️ Run Using Docker (Recommended)
1️⃣ Build Image
docker build -t lexiscan-auto .

2️⃣ Run Container
docker run -p 8000:8000 lexiscan-auto

3️⃣ Open Swagger UI
http://localhost:8000/docs

▶️ Run Locally (Without Docker)
pip install -r requirements.txt
uvicorn api.app:app --reload


Then open:

http://127.0.0.1:8000/docs

🔌 API Usage
Endpoint
POST /extract

Input

Upload a PDF file
OR

Provide raw text

Output (JSON)
{
  "status": "success",
  "document_type": "Legal / Offer Document",
  "entities": {
    "parties": {
      "company": null,
      "candidate": "Sharon Hanna A"
    },
    "dates": ["04 December 2025", "05-12-2025", "05-03-2026"],
    "amounts": ["₹6,000"],
    "termination_clause": [
      "The company reserves the right to terminate the internship..."
    ]
  }
}

✅ Project Status

Core functionality implemented

API working successfully

Dockerized and tested

Ready for review and submission

👤 Contributors

Sharon Hanna A

Samyuktha Vijayakumar