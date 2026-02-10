📄 LexiScan-Auto — Intelligent Legal Document Processing System

LexiScan-Auto is an end-to-end Intelligent Document Processing (IDP) system designed to extract structured legal information from scanned or digital contract PDFs using OCR + NLP + custom-trained Legal NER models, exposed through a FastAPI service and deployable via Docker.

🚀 Key Features

📑 PDF Ingestion (Scanned & Digital Contracts)

🔍 OCR-based Text Extraction using Tesseract

🧠 Custom Legal Named Entity Recognition (NER)

Trained on the CUAD (Contract Understanding Atticus Dataset)

📊 Structured JSON Output

Parties

Dates

Monetary Amounts

⚡ FastAPI-based REST API

🐳 Fully Dockerized for Deployment

🧠 System Architecture
PDF Document
     ↓
OCR (Tesseract)
     ↓
Text Preprocessing
     ↓
Custom Legal NER (spaCy)
     ↓
Post-processing + Regex Extraction
     ↓
Structured JSON Output (FastAPI)

🛠️ Tech Stack

Python

spaCy (Custom-trained Legal NER model)

FastAPI (API Layer)

Tesseract OCR

Docker

CUAD Dataset

📂 Project Structure
LexiScan-Auto/
├── api/                 # FastAPI application
├── ocr/                 # OCR pipeline
├── ner/                 # NER training & inference
├── pipeline/            # End-to-end pipeline runner
├── models/              # Trained spaCy NER model
├── utils/               # Regex-based extractors
├── data/                # (Ignored) datasets
├── Dockerfile
├── requirements.txt
├── README.md
├── sample_contract.pdf
├── sample_output.json

▶️ Run Locally (Without Docker)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start the API server
uvicorn api.app:app --reload

3️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🐳 Run with Docker
1️⃣ Build Docker image
docker build -t lexiscan-auto .

2️⃣ Run container
docker run -p 8000:8000 lexiscan-auto

3️⃣ Access API
http://localhost:8000/docs

📥 API Usage
Endpoint
POST /extract

Input Options

Upload a PDF file

OR provide raw text

Example Response
{
  "status": "success",
  "entities": {
    "PARTY": ["Company A", "Company B"],
    "DATE": ["12 March 2022"],
    "AMOUNT": ["$500,000"]
  }
}

📌 Sample Files

sample_contract.pdf — Example legal contract

sample_output.json — Example extracted entities

🎯 Use Cases

Legal contract analysis

Compliance automation

Due diligence support

Enterprise document intelligence

AI-powered legal assistants

🔮 Future Enhancements

Support for additional legal entity types

Improved OCR accuracy for scanned documents

Database integration

Frontend dashboard

Cloud deployment (AWS/GCP)

## 👩‍💻 Contributors

**Sharon Hanna**  
B.Tech — Artificial Intelligence & Data Science  

**Samyuktha Vijayakumar**  
Project Contributor

# LexiScan Auto

## Screenshots

### API Response
![API Response](screenshots/api_response.jpeg)

### Docker Running
![Docker Running](screenshots/docker_running.jpeg)

### Swagger UI
![Swagger UI](screenshots/swagger_ui.jpeg)
## Model Evaluation (F1-Score)

The Legal NER model was evaluated using a validation sample.
Performance metrics include Precision, Recall, and F1-score.

- Precision: ~0.78
- Recall: ~0.75
- F1-score: ~0.76

F1-score is used as the primary metric due to entity class imbalance
and the importance of balanced extraction accuracy in legal documents.
## 👩‍💻 Contribution – Samyuktha

- Implemented OCR pipeline for PDF → text extraction  
- Integrated OCR output with trained Legal NER model  
- Built REST API for document entity extraction  
- Generated structured JSON output for legal contracts  
- Assisted in deployment, testing, and documentation  
