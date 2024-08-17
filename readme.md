# Langchain Integrations

This repository demonstrates several integrations with Langchain, using API keys for various functionalities.

## 1) Langchain Response Tracing

This integration traces your outputs and metadata directly into the Langsmith website, where you can review them. To enable this, you'll need to obtain the necessary credentials from the Langsmith website.

Set the following environment variables in your `.env` file:

```bash
LANGCHAIN_TRACING_V2=<your_value_here>
LANGCHAIN_ENDPOINT=<your_value_here>
LANGCHAIN_API_KEY=<your_value_here>
LANGCHAIN_PROJECT=<your_value_here>
```

## 2) Email Generator

This module generates emails with the assistance of GPT. To use it, provide the file path and your OpenAPI key.

## 3) Question Answering from CSV

This feature allows you to extract and answer questions from an uploaded CSV file using a Langchain agent. It requires an API key to generate responses.
