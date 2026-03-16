### Phase 1: The "Under the Hood" Search (Embeddings & Vector DBs)

Before using fancy frameworks, you need to understand how AI actually "reads" data. You will build a simple semantic search engine (e.g., searching a list of movies by "vibe" instead of exact title).

* **The Concept to Learn:** Text Embeddings (turning words into numbers) and Vector Search (finding similar numbers).
* **The Build:** A simple script that takes a list of text strings, converts them to embeddings using an API, stores them locally, and lets you search them.
* **The Free Text Resources:** * **OpenAI or Google Gemini API Docs:** Read their guides specifically on "Embeddings."
* **ChromaDB Docs:** Chroma is a free, open-source vector database that runs locally. Read their "Getting Started" page to learn how to store and query those embeddings.



### Phase 2: The "Chat with my Data" App (Naive RAG)

Now you will build the classic AI project: Retrieval-Augmented Generation (RAG). You will build an app where you upload a PDF, and the AI can answer questions about it without hallucinating.

* **The Concept to Learn:** Document chunking, context windows, and prompting with retrieved data.
* **The Build:** An API endpoint where a user asks a question, your system searches ChromaDB for the relevant paragraphs from the PDF, and sends those paragraphs to the LLM to formulate an answer.
* **The Free Text Resources:**
* **LlamaIndex Documentation:** LlamaIndex is a framework specifically built for connecting LLMs to data. Their text tutorials are fantastic. Go straight to their "High-Level Concepts" and then the "Starter Tutorial."



### Phase 3: The "Database Analyst" Bot (Agents & Tool Use)

AI Engineers don't just make chatbots; they make systems that *do* things. You will build an AI agent that can write and execute SQL queries to answer questions about a database.

* **The Concept to Learn:** LLM Tool Calling (giving the AI the ability to run external code) and Agentic Workflows (letting the AI decide which tool to use).
* **The Build:** Connect an LLM to a local PostgreSQL database. When you ask, "Who are our top 5 users?", the AI should write the SQL, run it against Postgres, and return the answer in plain English.
* **The Free Text Resources:**
* **LangChain Documentation:** LangChain is the industry standard for orchestration. Read their conceptual guide on "Agents" and follow their specific use-case tutorial on "Q&A over SQL + CSV."



### Phase 4: The Production API (LLMOps & Tracing)

A project isn't an engineering feat until it's observable and deployed. You will take the Agent from Phase 3, track its performance, and put it live.

* **The Concept to Learn:** LLM Observability (tracking token costs, latency, and where the AI messes up) and deployment.
* **The Build:** Wrap your AI agent in a proper API backend, connect it to an observability tool, and deploy it live.
* **The Free Text Resources:**
* **LangSmith or Helicone Docs:** Both have generous free tiers. Read their quickstarts to learn how to trace your LangChain calls so you can see exactly what the LLM is thinking at every step.

---