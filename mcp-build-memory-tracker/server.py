from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

VECTOR_STORE_NAME = "MEMORIES"

mcp = FastMCP('Memories')

def get_or_create_vector_store():
    # Try to find existing vector store, else create a new one
    stores = client.vector_stores.list()
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_store.create(name=VECTOR_STORE_NAME)


@mcp.tool()
def search_memory(query: str):
    """Searches memories in the vector store and return relevant chunks."""
    vector_store = get_or_create_vector_store()
    results = client.vector_stores.search(
        vector_store_id=vector_store.id,
        query=query
    )

    content_texts = [
        content.text
        for item in results.data
        for content in item.content
        if content.type == 'text'
    ]
    return {"results": content_texts}


@mcp.tool()
def save_memory(memory: str):
    """Saves a memory to the vector store."""
    vector_store = get_or_create_vector_store()
    # Save memory to a temp file or upload
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as temp_file:
        temp_file.write(memory)
        temp_file.flush()
        client.vector_stores.files.upload_and_poll(
            vector_store_id=vector_store.id,
            file=open(temp_file.name, 'rb')
        )
    return {"status": "Memory saved successfully.", "vector_store_id": vector_store.id}

if __name__ == "__main__":
    mcp.run(transport="stdio")