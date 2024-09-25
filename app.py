import streamlit as st
import fitz  # PyMuPDF
import difflib

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def calculate_similarity(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio()

st.title("ATS System")

uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
job_description = st.text_area("Job Description")

if uploaded_pdf and job_description:
    pdf_text = read_pdf(uploaded_pdf)
    similarity = calculate_similarity(pdf_text, job_description)
    st.write(f"Similarity Score: {similarity:.2f}")
