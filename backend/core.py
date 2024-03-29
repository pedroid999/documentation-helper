import os
from typing import Any
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone

from dotenv import load_dotenv
from typing import Any, Dict, List

# Load environment variables from .env file
load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT"],
)


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
    )
    chat = ChatOpenAI(verbose=True, temperature=0)

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat,
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )

    return qa({"question": query, "chat_history": chat_history})


if __name__ == "__main__":
    print(run_llm("What is LangChain?"))
