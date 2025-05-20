import streamlit as st
from backend.extractor import extract_text_from_pdf
from backend.analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer & Enhancer", layout="centered")

st.title("📄 Resume Analyzer & Enhancer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste target job/internship description", height=200)

if uploaded_file and job_description:
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            analysis = analyze_resume(resume_text, job_description)
            st.subheader("🔍 Analysis Results")
            st.markdown(analysis)
