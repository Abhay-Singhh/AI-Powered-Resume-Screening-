         
from skills import SKILLS

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    return list({skill for skill in SKILLS if skill in resume_text})