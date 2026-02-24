from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv
load_dotenv('./.env')

model = ChatOpenAI(model="gpt-4.1")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = InMemoryVectorStore(embeddings)

bs4_strainer = bs4.SoupStrainer(
    class_=("post-title", "post-header", "post-content"))
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs={"parse_only": bs4_strainer},
)
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True,
)
all_splits = text_splitter.split_documents(docs)

document_ids = vector_store.add_documents(documents=all_splits)

# LLM Agent (multiple searches)
# @tool(response_format="content_and_artifact")
# def retrieve_context(query: str):
#     retrieved_docs = vector_store.similarity_search(query, k=2)
#     serialized = "\n\n".join(
#         (f"Source: {doc.metadata}\nContent: {doc.page_content}")
#         for doc in retrieved_docs
#     )
#     return serialized, retrieved_docs


# tools = [retrieve_context]
# prompt = (
#     "You have access to a tool that retrieves context from a blog post. "
#     "Use the tool to help answer user queries."
# )
# agent = create_agent(model, tools, system_prompt=prompt)

# query = (
#     "What is the standard method for Task Decomposition?\n\n"
#     "Once you get the answer, look up common extensions of that method."
# )

# for event in agent.stream(
#     {"messages": [{"role": "user", "content": query}]},
#     stream_mode="values",
# ):
#     event["messages"][-1].pretty_print()


# LLM chains (only one search using the user prompt and the content from the retrieved context)
@dynamic_prompt
def prompt_with_context(request: ModelRequest) -> str:
    """Inject context into state messages."""
    last_query = request.state["messages"][-1].text
    retrieved_docs = vector_store.similarity_search(last_query)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    system_message = (
        "You are a helpful assistant. Use the following context in your response:"
        f"\n\n{docs_content}"
    )

    return system_message


agent = create_agent(model, tools=[], middleware=[prompt_with_context])

query = "What is task decomposition?"
for step in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
