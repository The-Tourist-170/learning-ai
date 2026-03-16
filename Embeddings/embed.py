import os
from google import genai
from dotenv import load_dotenv
import chromadb

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="embeddings")

# ----------------------------------------------

# Using different embeddings function model

# from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
# 
# collection = client.create_collection(
    # name="my_collection",
    # embedding_function=OpenAIEmbeddingFunction(
        # model_name="text-embedding-3-small"
    # )
# )

content = [
    "What is the meaning of life?",
    "What is the meaning of love?",
    "What is the meaning of death?",
    "What is the medicine for fever?"
]

# -------------------------------------------

# Creating embeddings using gemini model

doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=content
)

doc_embeddings = [emb.values for emb in doc_result.embeddings]

# --------------------------------------------

# Adding to collection

collection.add(
    ids=["id1", "id2", "id3", "id4"],
    # documents=content,
    embeddings=doc_embeddings
)

# ----------------------------------------------

# Querying the collection

query_text = "What is love?"
query_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query_text
)

query_embedding = query_result.embeddings[0].values

res = collection.query(
    #This will fail because the embedding dimension is different, 
    # because chromadb expects the same dimension 
    # for the embeddings and the query embeddings, 
    # which is 3072 for gemini-embedding-001, 
    # but the query embedding is 384 for chromadb's inbuilt model

    # query_texts=[query_text], 

    query_embeddings=[query_embedding],
    n_results=2
)  

print("\n--- QUERY RESULTS ---")
print(res)

# -------------------------------------------

# Updating the collection

# new_content = "What is the medicine for dry cough?"

# collection.update(
#     ids = ["id1"],
#     documents = [new_content]
# )

# print("\n--- UPDATED COLLECTION ---")
# print(collection.get())

# collection.update(
#     ids = ["id1"],
#     documents = [new_content]
# )

# print("\n--- UPDATED COLLECTION ---")
# print(collection.get())

# --------------------------------------

# Deleting the collection

# print(collection.get())
# collection.delete(
    # ids = ["id4"]
# )
# 
# print("\n--- DELETED COLLECTION ---")
# print(collection.get())

# .delete also supports the where filter. 
# It will delete all items in the collection 
# that match the where filter.