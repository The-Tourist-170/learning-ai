# Applied AI Engineering: Zero to Production

This repository documents my comprehensive transition into Applied Artificial Intelligence and LLMOps. It serves as both a theoretical knowledge base and a practical workspace for building end-to-end, production-ready AI systems.

Leveraging a strong foundation in structured backend systems and frontend architecture (Java, React, PostgreSQL), this project series focuses strictly on **AI Engineering**—bridging the gap between raw Large Language Models and actual, deployable software products.

## 🎯 The Philosophy: Proof Over Pedigree
The core strategy of this repository is focused on building functional, observable, and deeply integrated AI applications rather than theoretical model training. The learning approach heavily favors text-based documentation and immediate implementation over passive video tutorials. 

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **AI/Orchestration Frameworks:** LlamaIndex, LangChain
* **Vector Databases:** ChromaDB
* **Models:** Google Gemini (Embeddings & Generation)
* **API Infrastructure:** FastAPI
* **Data Processing:** PyPDF

---

## 🗺️ The Engineering Roadmap

This repository is structured into progressive phases, moving from the fundamental math of how AI reads text, up to deploying agentic workflows. Each phase folder contains both **Text-Based Theory Notes** and the **Implementation Code**.

### Phase 1: The "Under the Hood" Mechanics (Embeddings & Vector Search)
* **Concepts Mastered:** High-dimensional vector spaces, Tokenization, Cosine Similarity, Semantic vs. Lexical Search.
* **The Build:** A local Python engine that generates text embeddings via the Gemini API and stores them in a local ChromaDB instance to perform semantic similarity matching without relying on keyword overlap.

### Phase 2: "Chat With My Data" (Retrieval-Augmented Generation)
* **Concepts Mastered:** Context window limitations, Document ingestion, Sentence chunking (Nodes), Naive RAG prompting.
* **The Build:** An automated pipeline utilizing `LlamaIndex` to ingest dense PDF documents, chunk the text, store the vectors in Chroma, and expose a `FastAPI` endpoint that allows an LLM to answer user questions strictly based on the retrieved context.

### Phase 3: The Database Analyst Bot (Agents & Tool Use)
* **Concepts Mastered:** LLM Tool Calling, Agentic reasoning loops, Text-to-SQL logic.
* **The Build:** Connecting an LLM to a relational database, allowing the AI to autonomously write, execute, and analyze SQL queries to answer natural language questions about the data.

### Phase 4: Production API & LLMOps
* **Concepts Mastered:** AI Observability, Tracing, Prompt versioning, Cloud deployment.
* **The Build:** Integrating LangSmith/Helicone to track token costs and latency, wrapping the AI agents in a robust backend architecture, and deploying the system to a live cloud environment.

---

## 🚀 How to get Locally

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/applied-ai-engineering.git](https://github.com/yourusername/applied-ai-engineering.git)
cd applied-ai-engineering