from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from similarity_model import calculate_similarity

# Step 1: Load Resume
resume_path = "../dataset/sample_resume.pdf"
resume_text = extract_text_from_pdf(resume_path)

# Step 2: Job Description
job_description = """
Looking for a Python developer with experience in
machine learning, SQL, deep learning, and cloud platforms.
Knowledge of Docker and AWS is a plus.
"""

# Step 3: Extract Skills
skills = extract_skills(resume_text)

# Step 4: Calculate Match Score
score = calculate_similarity(resume_text, job_description)

# Step 5: Missing Skills
required_skills = [
    "python",
    "machine learning",
    "sql",
    "deep learning",
    "docker",
    "aws"
]

missing_skills = [skill for skill in required_skills if skill not in skills]

# Step 6: Output
print("\n===== AI Resume Analysis =====")
print("Match Score:", round(score, 2), "%")
print("Skills Found:", skills)
print("Missing Skills:", missing_skills)
