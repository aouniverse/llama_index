import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
os.environ["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"] = os.getenv("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")
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
