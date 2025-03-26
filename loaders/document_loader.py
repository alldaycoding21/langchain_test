from langchain.document_loaders import TextLoader, DirectoryLoader

def load_documents(path="data/raw_docs/"):
    loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()
    return documents
