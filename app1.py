import streamlit as st
import cohere
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize Cohere Client with API Key
api_key = ""  # Replace with your actual Cohere API key
co = cohere.Client(api_key)

# Streamlit UI
st.header("My First Chatbot")

# Sidebar for PDF Upload
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract text from PDF
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Break the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)

    # User input for question
    question = st.text_input("Ask a question about your document:")

    if question:
        # Combine document chunks and user question into a prompt
        prompt = (
            f"The following are excerpts from a document:\n{chunks[:3]}\n"
            f"Answer the following question based on the text above:\n{question}"
        )

        # Use Cohere for text generation
        response = co.generate(
            model="command-xlarge-nightly",  # Use an appropriate Cohere model
            prompt=prompt,
            max_tokens=300,
            temperature=0.5,
        )

        # Display the response
        st.subheader("Answer:")
        st.write(response.generations[0].text.strip())
