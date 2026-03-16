from google import genai
import chromadb
import os
from dotenv import load_dotenv

content = [
    "The cat sat on the mat", 
    "I love eating pizza", 
    "Felines prefer to rest on rugs",
    "The dog chased the ball",
    "My favourite day in gym is chest day."
] 

load_dotenv()
ai_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
client = chromadb.Client()

collection = client.create_collection(name="test1")

def embedding_model(content):
    res = ai_client.models.embed_content(
        model="gemini-embedding-001",
        contents=content    
    )
    return res

res = embedding_model(content)
em_doc = [emb.values for emb in res.embeddings]

collection.add(
    ids=["1", "2", "3", "4", "5"],
    embeddings=em_doc,
)

q_text = "Have you ever thought about your fitness?"
q_em  = embedding_model(q_text)

q_val = q_em.embeddings[0].values

q_res = collection.query(
    query_embeddings=[q_val],
    n_results=1
)

print("----------Result----------")
print(q_res)