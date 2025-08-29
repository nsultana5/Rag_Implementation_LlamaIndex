from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def create_index(data_folder="data"):
    documents = SimpleDirectoryReader(data_folder).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()
