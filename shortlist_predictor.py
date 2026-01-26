import pickle
import numpy as np

model = pickle.load(open("shortlist_model.pkl", "rb"))

def predict_shortlist(resume_score, project_score, skills_count, projects_count):
    features = np.array([[
        resume_score,
        project_score,
        skills_count,
        projects_count
    ]])

    probability = model.predict_proba(features)[0][1]
    decision = "SHORTLIST" if probability >= 0.5 else "REJECT"

    return round(probability * 100, 2), decision
