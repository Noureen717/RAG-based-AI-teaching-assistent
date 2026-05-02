# 📘 RAG-Based AI Teaching Assistant

## 🚀 Overview
The RAG-Based AI Teaching Assistant is an AI-powered system that uses **Retrieval-Augmented Generation (RAG)** to answer course-related queries with high accuracy.

The system retrieves relevant information from processed educational content and generates **context-aware responses** using a local Large Language Model (LLM). It is designed to simulate an intelligent teaching assistant for students.

---

## 🧠 Key Features
- 🔍 Semantic search using embeddings (BGE-M3)
- 📚 Top-K relevant content retrieval using cosine similarity
- 🤖 Context-aware response generation using LLaMA3 (Ollama)
- ⚡ Fast and efficient local inference (no external APIs)
- 🧩 Modular RAG pipeline implementation

---

## 🏗️ System Architecture
User Query
↓
Embedding Generation
↓
Vector Similarity Search
↓
Top-K Retrieval (k=5)
↓
Context Injection
↓
LLM (LLaMA3 via Ollama)
↓
Generated Answer


---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Embeddings:** BGE-M3  
- **LLM:** LLaMA3 (via Ollama)  
- **Storage:** Joblib  
- **Backend:** REST API  

---

## ⚙️ How It Works
1. User inputs a query  
2. Query is converted into vector embeddings  
3. System computes cosine similarity with stored embeddings  
4. Retrieves top 5 most relevant content chunks  
5. Injects retrieved context into the LLM  
6. Generates an accurate, context-aware response  

---
## Project Structure
rag-ai-teaching-assistant/
│── app.py
│── embeddings.py
│── retriever.py
│── generator.py
│── requirements.txt
│── README.md


## ⚠️ Note on Large Files

Large files such as:

audio files
video files
embeddings (.joblib)
datasets

are not included in this repository due to size constraints.

👉 Instructions to regenerate them can be added if needed

## 🎯 Applications
AI Teaching Assistant
Educational Chatbot
Student Doubt Solver
EdTech Platforms

## 🚧 Future Improvements
Streamlit / Web UI integration
Hybrid search (BM25 + embeddings)
Multi-subject support
Voice-based interaction
Cloud deployment

## 👩‍💻 Author
Noureen Fatima
B.Tech CSE (AI/ML)

## ⭐ Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.
