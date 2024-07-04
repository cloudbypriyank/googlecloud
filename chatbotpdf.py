import json
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.chat_models import ChatOpenAI
import os
import io
import uuid

# Title of the app
st.title('🦜🔗 Get Answer Based on Provided PDF')

# Load environment variables (not recommended to hardcode sensitive info)
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = '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'
os.environ['LANGCHAIN_PROJECT'] = 'pr-indelible-whelp-78'

google_api_key = 'AIzaSyDK1nGKwa9eiwiQ6_VJOQ7eAQHb21Y5UyU'
os.environ["GOOGLE_API_KEY"] = google_api_key

# Function to extract text from PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(io.BytesIO(pdf.read()))
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create a vector store from text chunks and save it
def create_vector_store_and_save(text_chunks, session_id):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(session_id)
    return vector_store

# Function to load conversational AI chain for question answering
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if answer is not available in the provided context just say , "Sorry, I can't answer the question, which is not provided in the context", don't provide wrong answers.
    Context: {context}
    Question: {question}
    Answer Format : intent,entity,sentiment,reponse_text in json object
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to handle user input and provide response
def user_input(user_question, session_id):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local(session_id, embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    context = "\n".join([doc.page_content for doc in docs])
    prompt_template = get_conversational_chain()

    chain = get_conversational_chain()
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True,
    )

    return {"output" : response["output_text"],"response" : json.loads(response["output_text"])  }
    st.write("Reply: ", response["output_text"])
    

# Main function for Streamlit app
def main():
    st.header('Chat PDF')
    st.header("Multi-PDF Chat System")

    pdf_docs = st.file_uploader(
        "Upload your PDF Files and Click on the Submit & Process Button",
        accept_multiple_files=True,
    )

    if pdf_docs:
        user_question = st.text_input("Ask a Question from the PDF Files")
        
        if user_question:
            if st.button("Submit & Process"):
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    session_id = str(uuid.uuid4())
                    create_vector_store_and_save(text_chunks, session_id)
                    response = user_input(user_question, session_id)
                    st.subheader("Response:")
                    st.write(response)

if __name__ == "__main__":
    main()
