#ocr_pipeline.py
import pdfplumber
from PIL import Image
import pytesseract
import os

# Windows Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {i} ---\n{page_text}"
    return text

def ocr_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def ocr_scanned_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            im = page.to_image(resolution=300).original
            page_text = pytesseract.image_to_string(im)
            text += f"\n--- Page {i} ---\n{page_text}"
    return text

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                print("Digital PDF detected...")
                return extract_text_from_pdf(pdf_path)
    print("Scanned PDF detected...")
    return ocr_scanned_pdf(pdf_path)

if __name__ == "__main__":
    print("OCR pipeline ready! Place your PDF or image files in this folder and call the functions.")
