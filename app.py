import streamlit as st
from sentence_transformers import SentenceTransformer, util
import docx2txt
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

st.set_page_config(page_title="Resume to Job Matcher", layout="wide")
st.title("💼 Resume to Job Description Matcher")

st.markdown("""
Upload a resume and a job description. This app will analyze and compute a semantic similarity score between the two.
""")

# Sidebar for inputs
st.sidebar.header("Upload Files")
resume_file = st.sidebar.file_uploader("Upload Resume (DOCX or TXT)", type=['docx', 'txt'])
jd_file = st.sidebar.file_uploader("Upload Job Description (DOCX or TXT)", type=['docx', 'txt'])

# Function to clean and preprocess text
def preprocess(text):
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    tokens = text.lower().split()
    filtered = [w for w in tokens if w not in stop_words]
    return ' '.join(filtered)

# Function to extract text from docx or txt
def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".docx"):
        return docx2txt.process(uploaded_file)
    else:
        return uploaded_file.read().decode("utf-8")

if resume_file and jd_file:
    resume_text = extract_text(resume_file)
    jd_text = extract_text(jd_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume", resume_text, height=150)

    st.subheader("Extracted Job Description Text")
    st.text_area("Job Description", jd_text, height=150)

    # Preprocess
    resume_clean = preprocess(resume_text)
    jd_clean = preprocess(jd_text)

    # Embed
    resume_embedding = model.encode(resume_clean, convert_to_tensor=True)
    jd_embedding = model.encode(jd_clean, convert_to_tensor=True)

    # Similarity
    similarity_score = util.pytorch_cos_sim(resume_embedding, jd_embedding).item()
    match_percentage = round(similarity_score * 100, 2)

    st.markdown("## 🌟 Match Score: {}%".format(match_percentage))

    if match_percentage > 75:
        st.success("Excellent match! The resume aligns well with the job description.")
    elif match_percentage > 50:
        st.info("Moderate match. Some alignment detected.")
    else:
        st.warning("Low match. The resume and job description may not be closely related.")

else:
    st.info("Please upload both the resume and job description files to get started.")
