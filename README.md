# Resume-Summarizer-SQAC
This project is a simple AI-based Resume Summarizer tool built using Streamlit and Hugging Face Transformers. It takes a resume in text format and generates a short, meaningful summary highlighting the main professional details.

How It Works
The app uses the “facebook/bart-large-cnn” model from the Transformers library for summarization. When a resume is uploaded or pasted as text, the model processes it and provides a concise version of the content that retains key information such as experience, achievements, and roles.

Features
Upload a .txt resume file or paste text directly into the app.
Generates a professional summary within seconds.
Clean and interactive user interface built with Streamlit.

Installation
To run this project locally:
Clone or download this repository.
Open a terminal in the project directory.
Install the required dependencies:
pip install streamlit transformers torch


Run the Streamlit app:
streamlit run app.py
After running, the app will open automatically in your browser at:
http://localhost:8501
Files
app.py – Main Streamlit application file.
requirements.txt – Lists the dependencies needed to run the project.

Deployment
The app can be deployed on Streamlit Cloud by uploading the same files and linking your GitHub repository.

Output
The output is a summarized version of the uploaded resume text. It focuses on the main achievements and job responsibilities, reducing redundancy and length.

Acknowledgment
This project uses the pre-trained BART model from Hugging Face Transformers for text summarization.
