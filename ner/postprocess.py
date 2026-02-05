import re
import spacy

# ---------- EXTRACTION FUNCTIONS ----------

def extract_dates(text):
    """
    Extract dates like 07/09/1999
    """
    date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(date_pattern, text)


def extract_money(text):
    """
    Extract money like $250000, $250,000.00
    """
    money_pattern = r"\$\d+(?:,\d{3})*(?:\.\d+)?"
    return re.findall(money_pattern, text)


def extract_parties(doc):
    """
    Extract parties using NER (best-effort)
    """
    parties = []
    for ent in doc.ents:
        if ent.label_ == "PARTY":
            parties.append(ent.text.strip())
    return parties


def extract_termination(doc):
    """
    Extract termination-related sentences (rule-based)
    """
    keywords = ["terminate", "termination", "terminated"]
    termination_clauses = []

    for sent in doc.sents:
        if any(k in sent.text.lower() for k in keywords):
            termination_clauses.append(sent.text.strip())

    return termination_clauses


# ---------- MAIN POST-PROCESS FUNCTION ----------

def process_entities(doc):
    """
    Takes SpaCy doc and returns structured JSON output
    """
    text = doc.text

    output = {
        "dates": extract_dates(text),
        "parties": extract_parties(doc),
        "amounts": extract_money(text),
        "termination": extract_termination(doc)
    }

    return output
