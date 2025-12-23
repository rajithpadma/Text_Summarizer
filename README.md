AI-Based Article Summarizer Using NLP (BART Transformer Model)
Project Overview

This project presents an AI-powered text summarization application that enables users to automatically generate concise summaries from lengthy online articles or manually entered text. Reading long articles, research content, or news posts can be time-consuming, and manually summarizing information often leads to fatigue, missed insights, and inconsistent results.

To address this problem, this system integrates Natural Language Processing (NLP) with a Transformer-based Deep Learning model (facebook/bart-large-cnn) to deliver accurate, coherent, and contextually meaningful summaries. The application is implemented using Streamlit, providing users with a simple and interactive experience.

Problem Statement

Extracting key insights from long articles is challenging due to:

Time-consuming manual reading

Cognitive overload and difficulty retaining information

Inconsistent manually written summaries

Lack of automated intelligent summarization tools for everyday use

This project offers an AI-driven solution that automates summarization, improves reading efficiency, and supports users in quickly understanding lengthy textual content.

Key Functionalities
1. URL-Based Article Summarization

Users can paste a webpage link

The system automatically extracts article text

AI generates a meaningful summarized version

2. Manual Text Summarization

Users can paste any long text manually

AI processes and summarizes the content

Both modes store the extracted/pasted content in local text files for processing and then generate a final summarized output.

System Advantages

Powered by BART Transformer model for high-quality summarization

Supports both URL extraction and manual input modes

Handles large textual content by splitting into chunks and summarizing intelligently

Provides a clean and interactive Streamlit interface

Ensures readable and context-preserving summaries

Technology Stack

Programming Language: Python
Framework: Streamlit
NLP Model: facebook/bart-large-cnn (Hugging Face Transformers)
Libraries: Requests, BeautifulSoup, Transformers
Interface: Streamlit Web App

System Workflow

User selects input mode: URL or Manual Text

System extracts or accepts text input

Text is split into manageable chunks

BART Transformer model summarizes each chunk

Combined final summary is generated and displayed

How to Run the Project
Step 1: Clone the Repository
git clone <repository_link>
cd <project_folder>

Step 2: Install Required Libraries
pip install -r requirements.txt


(Ensure transformers, requests, beautifulsoup4, and streamlit are included)

Step 3: Run the Application
streamlit run app.py

How to Use the Application
Option 1 — Summarize via URL

Select “Paste Article URL”

Enter the article webpage link

Click Summarize Article

The system extracts the article and displays its summary

Option 2 — Summarize Manual Text

Select “Paste Text”

Paste any long text or article content

Click Summarize Article

The system processes and displays the summary

Results and Discussion

Provides accurate summaries while retaining key meaning

Efficiently handles long articles by chunking text

Offers clear readability and structured summarized output

Enhances user productivity and comprehension

Conclusion

This AI-powered Article Summarizer delivers a practical, intelligent solution for automatically generating concise and meaningful summaries from lengthy text sources. By leveraging advanced NLP transformers and a user-friendly Streamlit interface, the system improves reading efficiency, supports quick understanding, and demonstrates real-world application of modern AI technologies in information processing.
