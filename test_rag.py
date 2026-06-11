from rag.rag_pipeline import search_knowledge

query = "healthy protein sources"

result = search_knowledge(query)

print(result)