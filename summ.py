import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import io

# Title of the app
st.title('🦜🔗 Earnings Transcript Summarizer App')

# OpenAI API key input
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to generate a summary for a chunk
def generate_summary_chunk(chunk):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    summary_prompt = f"Summarize the following earnings transcript:\n\n{chunk}\n\nSummary:"
    summary = llm(summary_prompt)
    return summary

# Function to extract text from a PDF file
def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(io.BytesIO(pdf_file))
    for page in pdf_reader.pages:
        text += page.extract_text() or ''  # Handle cases where extract_text() might return None
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    return chunks

# Upload the earnings transcript
uploaded_file = st.file_uploader("Upload an earnings transcript (PDF)", type="pdf")

# Display a form to submit the transcript for summarization
if uploaded_file:
    # Read the uploaded file and extract text
    transcript_text = get_pdf_text(uploaded_file.read())
    
    with st.form('summarizer_form'):
        st.text_area("Transcript", transcript_text, height=300)
        submitted = st.form_submit_button('Generate Summary')
        
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        
        if submitted and openai_api_key:
            # Split text into chunks
            text_chunks = get_text_chunks(transcript_text)
            
            # Generate and display summaries for each chunk
            st.subheader("Summary")
            final_summary = ""
            for i, chunk in enumerate(text_chunks):
                st.write(f"Chunk {i + 1}/{len(text_chunks)}:")
                chunk_summary = generate_summary_chunk(chunk)
                final_summary += chunk_summary + " "
                st.write(chunk_summary)
            
            # Display the final combined summary
            st.write("Final Summary:")
            st.write(final_summary)
