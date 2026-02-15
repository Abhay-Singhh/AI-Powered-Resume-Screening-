import streamlit as st
from pdf_reader import extract_pdf_text
from skills_extractor import extract_skills
from projects_extractor import extract_projects
from resume_job_matcher import match_resume_job
from project_score import calculate_project_scores
from shortlist_predictor import predict_shortlist
import tempfile
import os

st.set_page_config(page_title="AI Resume Screening", layout="centered")
st.title("AI Resume Screening")
st.write("Upload your resume")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_pdf_path = temp_file.name

    st.success("PDF Uploaded Successfully")

    resume_text = extract_pdf_text(temp_pdf_path)

    overall_skills = extract_skills(resume_text)
    st.subheader(" Overall Skills Found")

    if overall_skills:
        st.write(", ".join(overall_skills))
    else:
        st.warning("No skills were confidently extracted")

    st.subheader("📄 Job Description (Optional)")
    job_description = st.text_area(
        "Paste the job description here to get a match score",
        height=200
    )

    projects = extract_projects(resume_text)

    project_results = []
    final_project_score = 0.0

    if projects and job_description:
        project_results, final_project_score = calculate_project_scores(
            projects,
            job_description
        )

    st.subheader(" Extracted Projects")

    if projects:
        for i, project in enumerate(projects, start=1):
            if not isinstance(project, dict):
                continue
            st.markdown(f"### Project {i}: {project['title']}")
            st.write("**Skills Used:**", ", ".join(project["skills"]))

            if job_description and project_results:
                score = project_results[i - 1]["score"]
                st.write("**Project Match Score:**")
                st.progress(score)
                st.write(f"**{round(score * 100, 2)}%**")

            st.markdown("---")
    else:
        st.warning("Projects could not be confidently extracted")

    if job_description and project_results:
        st.subheader(" Overall Project Relevance")
        st.progress(final_project_score)
        st.write(f"**Overall Project Relevance:** {round(final_project_score * 100, 2)}%")

    if job_description:
        resume_score = match_resume_job(resume_text, job_description)
        st.subheader(" Resume–Job Match Score")
        st.progress(resume_score / 100)
        st.write(f"**Match Percentage:** {resume_score}%")

        skills_count = len(overall_skills)
        projects_count = len(projects)

        probability, decision = predict_shortlist(
            resume_score / 100,
            final_project_score,
            skills_count,
            projects_count
        )

        st.subheader(" Final Shortlisting Decision")
        st.write(f"**Shortlisting Probability:** {probability}%")

        if decision == "SHORTLIST":
            st.success("✅ SHORTLISTED")
        else:
            st.error("❌ NOT SHORTLISTED")

    os.remove(temp_pdf_path)

