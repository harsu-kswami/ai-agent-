project name : -  Vector Database Beginner to Advanced (Optimized RAG System)

This project is a step-by-step implementation of a Retrieval-Augmented Generation (RAG) system.
It is specially optimized for small models (like Flan-T5) that have limited context window size.

The system loads PDFs, cleans the text, creates chunks, builds a vector database, and lets you ask questions with answers generated only from your documents.

 Features

PDF Loader → Upload and process PDF documents.

Smart Text Cleaning → Removes special characters and extra spaces while keeping meaning.

Optimized Chunks → Creates small, meaningful text chunks for better context fitting.

Vector Database with FAISS → Fast, offline, and secure semantic search.

BM25 + FAISS Retriever → Combines keyword and semantic search for best results.

QA Chain → Answers your questions using only the provided context.

Interactive Q&A Session → Chat with your documents in the terminal.



 Project Structure

smart_text_preprocessing → Cleans and normalizes text.

load_and_process_documents → Loads all PDFs from a folder.

create_optimized_chunks → Splits data into smaller chunks.

create_vector_database → Builds FAISS vector DB.

create_retrievers → Creates keyword + semantic retrievers.

create_qa_chain → Builds QA chain with short prompts.

ask → Asks questions and fetches answers.

interactive_session → Runs a live Q&A session in console.

 Requirements

Make sure you install the required libraries:

pip install langchain langchain-community faiss-cpu torch transformers numpy

 step 4

Put your PDF files inside the folder (default: /content/x).

Update the folder path in the code if needed:

PDF_FOLDER = "/content/x"


Run the script:

python vector_database_begineer_to_advanced.py


Start asking questions in the console.
Type quit anytime to exit.

for  Example
Your question: What is reinforcement learning?

 Answer: Reinforcement learning is a machine learning technique where agents learn by trial and error...
 Sources (2 found):
  1. ml_book.pdf (Page 12)
     Reinforcement learning is based on reward signals...

 Use Cases

Study material Q&A

Research paper summarization

Knowledge base search

AI-powered document assistant
