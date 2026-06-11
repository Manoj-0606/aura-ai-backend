import os
import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="database/chroma_db"
)

collection = client.get_or_create_collection(
    name="aura_knowledge"
)


def load_knowledge():

    base_path = "../knowledge_base"

    doc_id = 1

    for root, dirs, files in os.walk(base_path):

        for file in files:

            if file.endswith(".txt"):

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:

                    content = f.read()

                embedding = model.encode(content).tolist()

                collection.add(
                    ids=[str(doc_id)],
                    documents=[content],
                    embeddings=[embedding]
                )

                doc_id += 1

    print("Knowledge Base Loaded!")