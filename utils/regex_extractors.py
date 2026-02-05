import re

def extract_dates(text: str):
    date_patterns = [
        r"\b\d{2}-\d{2}-\d{4}\b",
        r"\b\d{2}/\d{2}/\d{4}\b",
        r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}\b"
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    return list(set(dates))


def extract_amounts(text: str):
    amount_pattern = r"₹\s?\d+(?:,\d+)*(?:\.\d+)?"
    return list(set(re.findall(amount_pattern, text)))


def extract_parties(text: str):
    company = None
    candidate = None

    company_match = re.search(r"([A-Z][a-zA-Z\s]+Pvt\. Ltd\.)", text)
    candidate_match = re.search(r"Dear\s+([A-Z][a-zA-Z\s]+),", text)

    if company_match:
        company = company_match.group(1)

    if candidate_match:
        candidate = candidate_match.group(1)

    return {
        "company": company,
        "candidate": candidate
    }
