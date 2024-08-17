import os
import csv
import streamlit as st
from dotenv import load_dotenv
from langsmith import traceable
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType

# Load environment variables
load_dotenv()

LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')

# Streamlit app title
st.title("Langchain Integrations")

# Langchain Response Tracing
st.header("Langchain Response Tracing")
query = st.text_input("Enter your query:")
if st.button("Trace Response"):
        llm = ChatOpenAI()
        response = llm.invoke(query)
        st.write(f"Response: {response}")

# Email Generator
st.header("Email Generator")
question = st.text_input("Enter your email question:")
if st.button("Generate Email"):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an Email Generator assistant. Please respond to the user's request only based on the given context and give responses in Email format."),
            ("user", "Question: {question}\nContext: {context}")
        ])
        model = ChatOpenAI(model="gpt-3.5-turbo")
        output_parser = StrOutputParser()
        
        chain = prompt | model | output_parser
        context = "Give the response to user queries in JSON Format"
        
        response = chain.invoke({"context": context, "question": question})
        st.write(f"Generated Email: {response}")

# Get Questions Answer from CSV
st.header("Get Answers from CSV")
OPENAI_API_KEY = st.text_input("Enter your OpenAI API key:")
file_path = st.file_uploader("Upload your CSV file", type=["csv"])
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if OPENAI_API_KEY and file_path:
        with traceable():
            csv_agent = create_csv_agent(
                ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=OPENAI_API_KEY),
                file_path, 
                verbose=True,
                stop=["\nObservation:"],
                agent_type=AgentType.OPENAI_FUNCTIONS,
                handle_parsing_errors=True,
                allow_dangerous_code=True
            )
            response = csv_agent.run(question)
            st.write(f"Answer: {response}")
    else:
        st.error("Please provide both API key and a CSV file.")

