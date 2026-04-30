from sentence_transformers import SentenceTransformer, util
import re

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 🌍 UNIVERSAL SKILL DICTIONARY
SKILL_DB = [
    # Programming
    "python", "java", "c++", "sql",

    # Web / Software
    "html", "css", "javascript", "react", "node", "flask", "django",

    # AI / ML / Data Science
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "matplotlib", "scikit-learn", "tensorflow", "pytorch",

    # ECE / Embedded / VLSI
    "embedded systems", "vlsi", "verilog", "vhdl",
    "fpga", "arduino", "microcontroller", "rtl design",
    "digital electronics", "analog electronics",

    # Mechanical
    "autocad", "solidworks", "catia", "thermodynamics",

    # Civil
    "staad pro", "etabs", "surveying", "construction",

    # Electrical
    "power systems", "control systems", "electrical machines",

    # Tools
    "matlab", "simulink"
]


# ✅ FIXED FUNCTION (IMPORTANT)
def extract_skills(text):
    if not text:
        return []

    text = text.lower()
    found = []

    for skill in SKILL_DB:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)

    return list(set(found))   # 🔥 IMPORTANT RETURN


# ✅ SKILL MATCHING
def skill_score(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    # safety check
    if not jd_skills:
        return 0, resume_skills, jd_skills

    matched = set(resume_skills).intersection(jd_skills)

    score = len(matched) / len(jd_skills)

    return score, resume_skills, jd_skills


# ✅ SEMANTIC MATCHING
def semantic_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0.0

    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)

    return float(util.cos_sim(emb1, emb2))


# ✅ FINAL SCORE
def final_score(resume_text, jd_text):
    skill, resume_skills, jd_skills = skill_score(resume_text, jd_text)
    semantic = semantic_score(resume_text, jd_text)

    final = (0.7 * skill) + (0.3 * semantic)

    return final, resume_skills, jd_skills, skill, semantic