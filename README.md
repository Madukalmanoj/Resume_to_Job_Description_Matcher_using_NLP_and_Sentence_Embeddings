# 💼 Resume to Job Description Matcher (NLP + Sentence Embeddings)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![NLP](https://img.shields.io/badge/Category-NLP-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

> An interactive **Streamlit** application that compares a candidate's resume with a job description using **Sentence Transformers** and semantic similarity scoring.

---

## 📌 Features
- 📄 **Resume & Job Description Upload** – Supports `.docx` and `.txt` files.
- 🧹 **Text Preprocessing** – Cleans and removes stopwords for better matching.
- 🧠 **Semantic Matching** – Uses `all-MiniLM-L6-v2` from `SentenceTransformers` for embeddings.
- 📊 **Match Percentage** – Computes cosine similarity to produce a match score.
- 🎯 **Match Insights** – Highlights whether the match is Excellent, Moderate, or Low.

---

## 📂 Project Structure
``` bash
Resume_to_Job_Description_Matcher/
│── app.py # Main Streamlit application
│── requirements.txt # Python dependencies
│── README.md # Project documentation
```

---

## 🛠 Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/Resume_to_Job_Description_Matcher.git
cd Resume_to_Job_Description_Matcher
```
## 🚀 Usage

Run the app with:

streamlit run app.py

## 📤 Upload Inputs:

Resume (.docx or .txt)

Job Description (.docx or .txt)

The app will:

Extract and preprocess text.

Generate embeddings using Sentence Transformers.

Calculate cosine similarity.

Display a match score with insights.

## ⚙️ How It Works

Text Extraction
Uses docx2txt or file reading for .txt files.

Preprocessing

Removes special characters.

Converts text to lowercase.

Removes stopwords (nltk).

Embedding & Similarity

Embeds both texts using all-MiniLM-L6-v2.

Uses cosine similarity to measure closeness.

Scoring

75% → Excellent Match ✅

50-75% → Moderate Mat

## 📦 Requirements
``` bash
streamlit
sentence-transformers
docx2txt
nltk
```
## 📜 License

This project is licensed under the MIT License – free to use and modify.

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub!

