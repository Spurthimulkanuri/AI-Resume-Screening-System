# 🤖 AI Resume Screening System

An AI-powered web application that analyzes resumes and matches them with job descriptions using **skill-based matching** and **semantic similarity (NLP)**.

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 🔍 Extract text automatically
- 🧠 Extract skills from resume & job description
- 🎯 Compare resume with JD
- 📊 Calculate:
  - Skill Match Score
  - Semantic Similarity Score
- ✅ Decision: Selected / Not Selected
- 🟢 Matched Skills
- 🔴 Missing Skills
- 💡 Explainable results

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Sentence Transformers (BERT)**
- **HTML + CSS**
- **Regex (for skill extraction)**

---

## ⚙️ How It Works

1. User uploads resume (PDF)
2. System extracts text from resume
3. Extracts skills from:
   - Resume
   - Job Description
4. Computes:
   - **Skill Score** → based on matching skills  
   - **Semantic Score** → using NLP (BERT embeddings)
5. Final Score:
