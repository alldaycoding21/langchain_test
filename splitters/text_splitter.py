from langchain.text_splitter import CharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(documents):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)
