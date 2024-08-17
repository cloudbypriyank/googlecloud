import csv
import os
from flask import Flask, jsonify, request
from langsmith import traceable
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType

app = Flask(__name__)

load_dotenv()

LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')

#Track langchain response

@app.route('/langchain-response-tracing', methods=['POST'])
@traceable
def langchain_tracing():
    data = request.get_json()
    query = data['query']
    llm = ChatOpenAI()
    response = llm.invoke(query)
    print(response)
    return str(response)

#Email Generator

@app.route('/langchain-Emailgenerator-tracing', methods=['POST'])
@traceable
def langchain_emailgenerator_tracing():
    data = request.get_json()
    question = data['question']
    prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a Email Generator assistant. Please respond to the user's request only based on the given context and give responses in Email format."),
     ("user", "Question: {question}\nContext: {context}")
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo")
    output_parser = StrOutputParser()
    
    chain = prompt | model | output_parser
    context = "Give the response to user queries in JSON Format"

    response = chain.invoke({"context": context, "question": question})
    return str(response)

# Get Questions answer from CSV
@app.route('/langchain-get-questions-answer', methods=['POST'])
@traceable
def langchain_get_questions_answer():
    data = request.get_json()
    question = data['question']
    OPENAI_API_KEY = 'YOUR API KEY'
    file_path= 'YOUR FILE PATH'

    csv_agent= create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=OPENAI_API_KEY),
        file_path, 
        verbose=True,
        stop=["\nObservation:"],
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )

    response = csv_agent.run(question)
    print(response)
    return str(response)


       








if __name__ == '__main__':
    app.run(debug=True)
