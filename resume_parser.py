import pdfplumber
import docx
import re

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def parse_resume(file_path):
    text = extract_text(file_path)
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    exp_match = re.findall(r'(\d+)\s+years', text, re.I)
    skills_found = set(re.findall(r'\b(Python|Java|C\+\+|AWS|SQL|ML)\b', text, re.I))

    return {
        "Name": text.split("\n")[0].strip() if text else "Unknown",
        "Email": email[0] if email else "",
        "Phone": phone[0] if phone else "",
        "Skills": ", ".join(skills_found),
        "Experience": int(exp_match[0]) if exp_match else 0,
        "Resume File": file_path
    }
