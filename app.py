from flask import Flask, request, render_template
import os

from utils.parser import extract_text_from_pdf
from utils.matcher import final_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("resume")
        jd_text = request.form.get("jd", "").lower()

        # 🔒 Safety check (important)
        if not file or file.filename == "":
            return render_template("index.html", result="⚠️ Please upload a resume")

        if jd_text.strip() == "":
            return render_template("index.html", result="⚠️ Please enter Job Description")

        # Save file
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Extract resume text
        resume_text = extract_text_from_pdf(filepath)

        # Get scores
        score, resume_skills, jd_skills, skill_s, semantic_s = final_score(resume_text, jd_text)

        # 🔥 NEW: Matched & Missing Skills
        matched = list(set(resume_skills).intersection(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        # Decision
        if score >= 0.4:
            result = f"✅ Selected (Score: {score:.2f})"
        else:
            result = f"❌ Not Selected (Score: {score:.2f})"

        return render_template(
            "index.html",
            result=result,
            resume_skills=resume_skills,
            jd_skills=jd_skills,
            matched=matched,
            missing=missing,
            skill_score=round(skill_s, 2),
            semantic_score=round(semantic_s, 2)
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)