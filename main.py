from pdf_reader import extract_pdf_text
from projects_extractor import extract_projects

pdf_path = "resume.pdf"
resume_text = extract_pdf_text(pdf_path)
projects = extract_projects(resume_text)
print(projects)