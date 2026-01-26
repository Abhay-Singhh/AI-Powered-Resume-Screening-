"This repository contains an end-to-end resume screening pipeline that simulates ATS behavior using NLP and ML"

Resume Screening System (ATS Simulation)

This project implements an NLP-based resume screening pipeline that simulates basic Applicant Tracking System (ATS) functionality. It extracts relevant information from resumes, compares candidate profiles with job descriptions, computes relevance scores, and produces an automated shortlisting decision.

# Features

Extracts skills, projects, and keywords from resumes

Matches candidate skills with job description requirements

Computes resume relevance score using TF-IDF similarity + structured features

Generates final Shortlisted / Not Shortlisted verdict

Trains a Logistic Regression classifier for resume classification

# Approach

Text preprocessing (cleaning, tokenization, normalization)

TF-IDF vectorization for textual similarity

Skill matching via keyword comparison

Project relevance scoring

Logistic Regression for classification

# Results

Achieved ~88–92% accuracy on resume classification

Successfully automated end-to-end ATS-style screening pipeline

🛠 Tech Stack

Python, TF-IDF, Scikit-learn, Logistic Regression, Pandas, NumPy
