import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import os

# Function to fetch article from URL
def url_fun(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    title = soup.find('title').get_text()
    text = ' '.join([para.get_text() for para in paragraphs])
    
    with open("article_1.txt", "w") as article_txt:
        pass
    with open("article_1.txt", "a") as article_txt_1:
        article_txt_1.write("\n")
        article_txt_1.write(title)
    with open("article_1.txt", "a") as article_txt_1:
        article_txt_1.write("\n")
        article_txt_1.write(text)
    st.write("Article text saved to article_1.txt")
    return title

# Function to paste the article text directly
def text_fun(text):
    with open("article_2.txt", "w") as article_txt:
        pass
    with open("article_2.txt", "a") as article_txt_2:
        article_txt_2.write(text)
    st.write("Article text saved to article_2.txt")

# Function to split text into chunks
def split_text(text, max_words=512):
    words = text.split()
    return [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

# Function to summarize text
def summarize_text(file_path, max_length=225, min_length=70, chunk_size=512):
    try:
        # Load the summarization pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        with open(file_path, "r") as file:
            text = file.read()
        
        # Split text into chunks
        chunks = split_text(text, max_words=chunk_size)
        summaries = []

        # Summarize each chunk
        for i, chunk in enumerate(chunks):
            st.write(f"Processing chunk {i + 1}/{len(chunks)}...")
            summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # Combine all summaries
        final_summary = ' '.join(summaries)
        st.write("Summary: ")
        st.write(final_summary)
        return final_summary

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Article Summarizer")

# Choose between URL input or pasting text
opt_1 = st.selectbox("Choose input method:", options=["Paste Article URL", "Paste Text"])

if opt_1 == "Paste Article URL":
    url_input = st.text_input("Enter the URL of the article:")
    if st.button("Summarize Article"):
        if url_input:
            title_1 = url_fun(url_input)
            st.write("Title: ", title_1)
            st.write("Summarizing the article...")
            summarize_text("article_1.txt")
        else:
            st.error("Please enter a valid URL.")
            
elif opt_1 == "Paste Text":
    text_input = st.text_area("Paste the text of the article:")
    if st.button("Summarize Article"):
        if text_input:
            text_fun(text_input)
            st.write("Summarizing the article...")
            summarize_text("article_2.txt")
        else:
            st.error("Please paste the text of the article.")

# To ensure that the source code and text files are saved in the same location, we check if the script is running locally
if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)  # Change working directory to the location of the script
