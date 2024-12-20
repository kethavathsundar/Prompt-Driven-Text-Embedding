# Prompt-Driven-Text-Embedding

# My First Chatbot

This application uses Streamlit to create a chatbot that answers questions based on uploaded PDF documents. The Cohere API is used for generating responses.

## Features
- Upload a PDF document.
- Ask questions based on the uploaded document.
- Get answers powered by Cohere's AI.

## Requirements
- Python 3.8 or later
- The following Python libraries:
  - streamlit
  - cohere
  - PyPDF2
  - langchain
  - faiss-cpu or faiss-gpu

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>


## Running the Application

1. Start the Streamlit server:
  - streamlit run app1.py

2. Use a local tunnel to expose your app (for Google Colab users):
  - npx localtunnel --port 8501
3. To retrieve your IP address:
  - wget -q -O - ipv4.icanhazip.com

## Notes

- If running on VS Code or locally, the localtunnel step is unnecessary.
