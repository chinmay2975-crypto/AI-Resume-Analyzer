import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    
    try:
        reader = PyPDF2.PdfReader(file_path)
        
        for page in reader.pages:
            text += page.extract_text()
            
    except Exception as e:
        print("Error reading file:", e)
    
    return text


if __name__ == "__main__":
    file = "sample_resume.pdf"
    content = extract_text_from_pdf(file)
    print(content)
