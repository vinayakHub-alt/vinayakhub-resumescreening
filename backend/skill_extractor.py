from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        text = ""
    return text


def extract_skills_from_text(text):
    skills = []
    keywords = ["Python", "Java", "C++", "SQL", "Flask", "Django", "AI", "ML", "NLP", "Data Science"]
    for kw in keywords:
        if kw.lower() in text.lower():
            skills.append(kw)
    return skills
