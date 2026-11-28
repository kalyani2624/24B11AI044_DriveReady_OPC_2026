# Day 5 — AutoMate AI: Thread Memory and RAG

Day 5 applies the 27 November class to the dealership assistant. The lesson covered three kinds of memory, LangGraph thread IDs and checkpointers, embeddings, Chroma DB, chunking, similarity search, and Retrieval Augmented Generation (RAG).

## What this task builds

1. **Conversation memory:** a separate conversation state for each thread ID, using LangGraph `InMemorySaver`.
2. **Knowledge retrieval:** read approved dealership PDFs, split them into chunks, create embeddings, and store the vectors in Chroma.
3. **RAG tool:** retrieve up to three relevant chunks and pass evidence to the LLM.
4. **Grounded answers:** answer from uploaded documents only; when relevant evidence is missing, tell the user it is unavailable rather than inventing a policy.
5. **Source references:** show the source PDF filename and page with retrieved evidence.

## Three memory categories from class

| Memory type | What it stores | AutoMate AI example |
|---|---|---|
| Conversation / short-term | Current thread messages | Which vehicle the buyer asked about a moment ago |
| Customer / long-term | Useful customer facts across separate chats | A buyer's preferred fuel or transmission, only with consent and a proper secure store |
| Knowledge | Business documents and policies until they change | Warranty, delivery, inspection and service policies |

This Day 5 exercise implements thread-level conversation memory and document knowledge retrieval. It does **not** implement a durable customer-profile store. Do not confuse a thread checkpointer with long-term customer memory.

## Run in Google Colab

1. Open `task.py` in a Colab notebook or upload it to Colab.
2. Install the packages:

```bash
pip install -U langchain langchain-groq langgraph langchain-chroma chromadb langchain-huggingface sentence-transformers langchain-community langchain-text-splitters pypdf
```

3. Add `GROQ_API_KEY` under Colab Secrets and enable notebook access.
4. Run the script and upload one or more approved, non-sensitive dealership PDFs.
5. Ask questions that are answered in the PDFs and questions that are not covered.
6. Use the thread memory demonstration to verify that one conversation does not receive another thread's name.
7. Run the test scenarios in `test.csv`.

## Embedding and RAG flow

**Indexing flow**

PDF → text extraction → chunking → embedding model → Chroma vector store.

The exercise uses `sentence-transformers/all-MiniLM-L6-v2`. The same embedding model must be used for indexing and query retrieval. Chunks use a size of 800 characters and an overlap of 100 characters.

**Query flow**

User question → query embedding → Chroma similarity search → top 3 relevant chunks → LLM prompt with retrieved evidence → grounded answer.

The relevance threshold is a prototype setting and should be evaluated against the actual dealership documents. Similarity is not proof that a source fully answers the question; review the retrieved excerpts and final answer.

## Important memory limitations

- `InMemorySaver` is for learning/testing. It stores checkpoints in RAM and loses them when the Python process or Colab runtime restarts.
- A thread ID isolates conversations; it is not an authentication mechanism. A real application must validate the user's identity and authorise thread access.
- The local Chroma persistence directory may survive a cell rerun in the same runtime, but Colab storage is not a guaranteed production database.
- Production should use a persistent checkpointer/database and an access-controlled vector store, with backup, retention, and deletion policies.

## Privacy and document handling

Upload only documents you are authorised to use. For this dealership project, use business-owned FAQs, policies, warranties, inspection checklists, and service documents. Do not upload customer IDs, certificates, bank statements, or private personal records into this prototype. Do not commit PDFs or private customer data to GitHub.

## Day 5 scope

This task adds thread memory and dealership-document RAG. It does not connect live inventory, WhatsApp, email, booking, or payment systems. RAG answers only from the uploaded documents and cannot independently verify real-world vehicle condition, legal status, or current market pricing.

## OPC submission files

- `task.py` — Python source code.
- `README.md` — implementation and setup details.
- `test.csv` — manual evaluation scenarios.
