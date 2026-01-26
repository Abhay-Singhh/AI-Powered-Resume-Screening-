import re
from skills import SKILLS

# ------------------------------------------------
# Helper: extract skills from a block of text
# ------------------------------------------------
def extract_skills_from_block(text):
    text = text.lower()
    return list({skill for skill in SKILLS if skill in text})


# ------------------------------------------------
# Step 1: Try clean section-based extraction
# ------------------------------------------------
def get_projects_section(text):
    match = re.search(
        r"\bprojects\b\s*(.*?)(\n\s*(skills|education|experience|academic))",
        text,
        re.I | re.S
    )
    if match:
        return match.group(1)
    return None


# ------------------------------------------------
# Step 2: Fallback – window after "projects"
# ------------------------------------------------
def get_projects_window(text, window_size=3500):
    start = re.search(r"\bprojects\b", text, re.I)
    if not start:
        return None
    return text[start.end(): start.end() + window_size]


# ------------------------------------------------
# Step 3: Parse individual projects (anchor-based)
# ------------------------------------------------
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

        # ---- NEW SAFETY FILTERS (VERY IMPORTANT) ----
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

        # ---- ENSURE DICT CONSISTENCY ----
        projects.append({
            "title": title,
            "skills": skills if skills else []
        })

    return projects



# ------------------------------------------------
# MAIN ENTRY FUNCTION
# ------------------------------------------------
def extract_projects(resume_text):
    text = resume_text

    # Step 1
    block = get_projects_section(text)

    # Step 2 fallback
    if not block:
        block = get_projects_window(text)

    if not block:
        return []

    # Step 3
    projects = parse_projects(block)

    return projects
