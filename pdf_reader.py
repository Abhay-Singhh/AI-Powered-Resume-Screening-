import pdfplumber
import PyPDF2

def extract_pdf_text(pdf_path):
    text = ""

    # -------- Attempt 1: pdfplumber (best for resumes) --------
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text(x_tolerance=2, y_tolerance=2)
                if page_text:
                    text += page_text + "\n"

        # If enough text was extracted, return it
        if len(text.strip()) > 1000:
            return text

    except Exception as e:
        pass  # silently fallback

    # -------- Attempt 2: PyPDF2 fallback --------
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        pass

    return text
