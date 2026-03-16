This documentation explains how to pop the hood on ChromaDB and tune how it stores and searches your vector embeddings. Out of the box, Chroma is fast, but tweaking these settings helps you perfectly balance **search speed** vs. **accuracy** (recall).

### 1. The Search Engines (Indexes)

Chroma uses different algorithms to group and search vectors depending on your setup:

* **Single Node (Local):** Uses an **HNSW** (Hierarchical Navigable Small World) index. It builds a multi-layered graph of your data, using sparse "highways" at the top to quickly navigate down to the closest matching vectors at the bottom.
* **Distributed / Cloud:** Uses a **SPANN** index. It clusters data so it can completely ignore irrelevant chunks of information, making it highly efficient for massive datasets. *(Note: You cannot manually tune SPANN settings yet).*

### 2. Distance Metrics (`space`)

This defines *how* Chroma calculates the similarity between two vectors. You must choose one that your specific embedding model supports:

| Metric | Parameter | Best For |
| --- | --- | --- |
| **Squared L2** | `l2` | True spatial/geometric proximity (This is Chroma's default). |
| **Inner Product** | `ip` | Recommendation systems where vector magnitude/strength matters. |
| **Cosine** | `cosine` | Text embeddings. It only measures the angle between vectors (ignoring scale). |

### 3. Tuning Speed vs. Accuracy

For local setups using HNSW, you can tweak parameters like `ef_search` (how hard it looks during a query) and `ef_construction` (how carefully it builds the index):

* **Higher values:** Better search accuracy (it checks more potential neighbors), but uses more RAM and slows down search/build times.
* **Lower values:** Blazing fast, but it might occasionally miss the true "best" match.

### 4. Built-in Embedding Functions

Instead of manually generating embeddings and then passing the raw float arrays to Chroma (like we had to do in your previous script), you can bake an embedding model directly into the collection's configuration. If you provide your API key via standard environment variables, Chroma will automatically embed raw text for you behind the scenes.

---