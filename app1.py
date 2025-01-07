import streamlit as st
import cohere
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize Cohere Client with API Key
api_key = "hooAHnPKG0f5R0CagUriMT2iepVpWOzHu6UidksF"  # Replace with your actual Cohere API key
co = cohere.Client(api_key)

# Streamlit UI
st.set_page_config(page_title="AI Document Chatbot", page_icon="🤖", layout="wide")
st.title("📚 Ask Your Document - AI Chatbot 🤖")

# Sidebar for PDF Upload
with st.sidebar:
    st.header("📂 Upload Your Document")
    file = st.file_uploader(
        "Upload a PDF file to extract insights and ask questions",
        type="pdf",
    )
    st.markdown("---")
    st.markdown(
        """
        ### Instructions:
        1. Upload a PDF file.
        2. Enter your question in the input box.
        3. Get answers generated by AI!
        """
    )

# Extract text from PDF
if file is not None:
    st.info("📄 Document uploaded successfully! Extracting text...")

    # Load the PDF and extract text
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Display the document summary
    st.success(f"✅ Text extracted from the uploaded document! Total characters: {len(text)}")

    # Break the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)

    st.subheader("📝 Document Summary")
    st.text_area("Preview of extracted text:", value=text[:1000] + "...", height=200)

    # User input for question
    question = st.text_input("💬 Ask a question about your document:")

    if question:
        with st.spinner("🤔 Thinking..."):
            try:
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
                st.subheader("🧠 AI Answer:")
                st.success(response.generations[0].text.strip())

            except Exception as e:
                st.error(f"❌ Error generating response: {e}")
else:
    st.warning("⚠️ Please upload a PDF file to start.")
