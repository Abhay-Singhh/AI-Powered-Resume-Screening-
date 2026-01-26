def calculate_project_scores(projects, job_description):
    """
    Returns:
    - list of per-project scores
    - final averaged project score
    """

    if not projects or not job_description:
        return [], 0.0

    job_text = job_description.lower()
    project_results = []

    for project in projects:
        skills = project.get("skills", [])

        if not skills:
            score = 0.0
        else:
            overlap = sum(1 for skill in skills if skill in job_text)
            score = round(overlap / len(skills), 2)

        project_results.append({
            "title": project["title"],
            "score": score
        })

    final_score = round(
        sum(p["score"] for p in project_results) / len(project_results),
        2
    )

    return project_results, final_score
