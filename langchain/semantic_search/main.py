from langchain_core.runnables import chain
from langchain_core.documents import Document
from typing import List
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv('./.env')

file_path = "./example_data/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_1 = embeddings.embed_query(all_splits[0].page_content)
vector_2 = embeddings.embed_query(all_splits[1].page_content)

vector_store = InMemoryVectorStore(embeddings)

ids = vector_store.add_documents(documents=all_splits)


@chain
def retriever(query: str) -> List[Document]:
    return vector_store.similarity_search(query, k=1)


# retriever = vector_store.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 1},
# )

results = retriever.batch(
    [
        "How many distribution centers does Nike have in the US?",
        "When was Nike incorporated?",
    ],
)

print(results[0][0].page_content)
