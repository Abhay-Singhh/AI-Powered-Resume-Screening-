import pickle
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import clean_text

tfidf = pickle.load(open("Vectors.pkl", "rb"))

def match_resume_job(resume_text, job_description):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    vectors = tfidf.transform([resume_clean, job_clean])
    similarity = cosine_similarity(vectors[0], vectors[1])

    return round(similarity[0][0] * 100, 2)
