import re
from skills import SKILLS


def extract_skills_from_block(text):
    text = text.lower()
    return list({skill for skill in SKILLS if skill in text})



def get_projects_section(text):
    match = re.search(
        r"\bprojects\b\s*(.*?)(\n\s*(skills|education|experience|academic))",
        text,
        re.I | re.S
    )
    if match:
        return match.group(1)
    return None


def get_projects_window(text, window_size=3500):
    start = re.search(r"\bprojects\b", text, re.I)
    if not start:
        return None
    return text[start.end(): start.end() + window_size]


def parse_projects(block_text):
    projects = []

    chunks = re.split(r"\btools\s*:", block_text, flags=re.I)

    for i in range(1, len(chunks)):
        before = chunks[i - 1].strip()
        after = chunks[i].strip()

        lines = [l.strip() for l in before.split("\n") if l.strip()]
        if not lines:
            continue

        title = lines[-1].replace(":", "").strip()

       
        if len(title) < 4:
            continue

        if title.lower() in {
            "responsibilities",
            "description",
            "overview",
            "project",
            "tools"
        }:
            continue

        full_block = (before + " " + after).lower()
        skills = extract_skills_from_block(full_block)

       
        projects.append({
            "title": title,
            "skills": skills if skills else []
        })

    return projects




def extract_projects(resume_text):
    text = resume_text

   
    block = get_projects_section(text)

    
    if not block:
        block = get_projects_window(text)

    if not block:
        return []

    
    projects = parse_projects(block)

    return projects

