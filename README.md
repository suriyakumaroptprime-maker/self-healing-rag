# Self-Healing Multi-Agent RAG System

A production-inspired Retrieval-Augmented Generation (RAG) system designed to improve answer accuracy, reliability, and transparency through a multi-agent architecture.

The system supports document ingestion from PDF, CSV, and Excel files, converts documents into vector embeddings, stores them in ChromaDB, and retrieves relevant context using a hybrid retrieval strategy that combines Dense Retrieval, BM25, and Reciprocal Rank Fusion (RRF).

Unlike traditional RAG systems, this project incorporates specialized agents for query understanding, memory management, retrieval planning, answer generation, evaluation, query repair, and citation generation. The self-healing mechanism automatically rewrites user queries and re-executes retrieval when answer confidence falls below a predefined threshold.

Key Features:

* Multi-Agent Architecture
* Hybrid Retrieval (Dense + BM25 + RRF)
* ChromaDB Vector Database
* Long-Term Conversation Memory
* Query Planning and Intent Detection
* Self-Healing Query Rewriting
* Citation-Aware Responses
* FastAPI Backend
* Streamlit User Interface
* Groq LLM Integration
