import os
import glob
from dotenv import load_dotenv
from dataclasses import dataclass

from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq

load_dotenv()
os.makedirs("data", exist_ok=True)


@dataclass
class ModelConfig:
    backend: str
    groq_model: str


def choose_llm(cfg: ModelConfig):
    backend = cfg.backend.lower()

    if backend == "groq":
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("Missing GROQ_API_KEY")
        return ChatGroq(
            model=cfg.groq_model,
            groq_api_key=key,
            temperature=0
        )

    raise RuntimeError(f"Unknown backend: {backend}")


def build_memory(session_id):
    history = FileChatMessageHistory(f"data/{session_id}.json")
    return ConversationBufferMemory(
        chat_memory=history,
        memory_key="chat_history",
        return_messages=True,
    )


def build_tools():
    tools = []

    # DuckDuckGo Search
    ddg = DuckDuckGoSearchRun()
    tools.append(Tool(
        name="duckduckgo",
        func=ddg.run,
        description="DuckDuckGo web search"
    ))

    # Wikipedia
    wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    tools.append(Tool(
        name="wikipedia",
        func=wiki.run,
        description="Wikipedia search"
    ))

    # SerpAPI (optional)
    if os.getenv("USE_SERPAPI") == "true":
        from langchain_community.utilities import SerpAPIWrapper
        serp = SerpAPIWrapper()
        tools.append(Tool(
            name="serpapi",
            func=serp.run,
            description="Google results via SerpAPI"
        ))

    return tools


def build_agent(session_id):
    cfg = ModelConfig(
        backend=os.getenv("MODEL_BACKEND", "groq"),
        groq_model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
    )

    llm = choose_llm(cfg)
    memory = build_memory(session_id)
    tools = build_tools()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        handle_parsing_errors=True,
        verbose=False
    )
    return agent, memory


def list_sessions():
    files = glob.glob("data/*.json")
    return sorted([os.path.splitext(os.path.basename(f))[0] for f in files])


def runtime_config():
    """Used by Streamlit sidebar for display only."""
    return {
        "backend": os.getenv("MODEL_BACKEND", "groq"),
        "model": os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
        "serpapi": "enabled" if os.getenv("USE_SERPAPI", "false") == "true" else "disabled",
        "memory_backend": os.getenv("MEMORY_BACKEND", "file")
    }
