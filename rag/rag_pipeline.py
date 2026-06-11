from sentence_transformers import SentenceTransformer
import chromadb

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB client
client = chromadb.PersistentClient(path="database/chroma_db")

collection = client.get_or_create_collection(
    name="aura_knowledge"
)

def search_knowledge(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    if results["documents"]:
        return "\n".join(results["documents"][0])

    return "No relevant knowledge found."