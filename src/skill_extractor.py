def extract_skills(text):
    
    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "docker",
        "aws"
    ]
    
    text = text.lower()
    
    found_skills = []
    
    for skill in skills:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills
