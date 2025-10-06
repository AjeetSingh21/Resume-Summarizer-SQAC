import streamlit as st
from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


st.title("Resume Summarizer")


st.write("Upload your resume (.txt) or paste text below")
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
resume_text = ""

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")
else:
    resume_text = st.text_area("Or paste your resume text here:", height=200)


if st.button("Summarize"):
    if resume_text.strip() == "":
        st.warning("Please provide some resume text.")
    else:
        with st.spinner("Summarizing"):
            summary = summarizer(resume_text, max_length=250, min_length=60, do_sample=False)
            st.success("Summary completed:")
            st.write(summary[0]['summary_text'])
