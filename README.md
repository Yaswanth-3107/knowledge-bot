# knowledge-

# Conversational Knowledge Bot  
LangChain + Groq + Streamlit + Wikipedia + SerpAPI + DuckDuckGo + Memory

(This README was generated for you. Everything is included: setup, install, flowchart, troubleshooting.)

---

## ✅ Overview
This project implements a conversational knowledge assistant with:

- Conversational memory  
- ReAct agent  
- Wikipedia search  
- DuckDuckGo search  
- SerpAPI (optional)  
- Groq LLaMA backend (fast + free + no VRAM needed)  
- Streamlit chat UI  
- Persistent sessions  

---

## ✅ Requirements

- Python 3.10 or 3.11  
- pip  
- Groq API key  
- SerpAPI key (optional)

---

## ✅ Installation

```
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ✅ .env Setup

```
APP_MODE=streamlit

MODEL_BACKEND=groq
GROQ_API_KEY=PUT_YOUR_GROQ_API_KEY_HERE
GROQ_MODEL=llama-3.1-8b-instant

USE_SERPAPI=true
SERPAPI_API_KEY=PUT_YOUR_SERPAPI_KEY_HERE

MEMORY_BACKEND=file
DEFAULT_SESSION_ID=default
SQLITE_PATH=data/memory.sqlite
```

---

## ✅ Run the App

```
streamlit run app_streamlit.py
```

---

## ✅ Architecture Flowchart (ASCII)

User → Streamlit UI → LangChain Agent → Tools (Wikipedia, DuckDuckGo, SerpAPI) → Groq LLM → Streamlit output

---

## ✅ Troubleshooting

- Import errors → use correct `app_core.py`
- OpenAI rate limits → switch to Groq (MODEL_BACKEND=groq)
- Ollama memory errors → don’t use Ollama on low-RAM systems
- SerpAPI empty → add SERPAPI_API_KEY

---

## ✅ Folder Structure

```
project/
│ app_core.py
│ app_streamlit.py
│ requirements.txt
│ .env
│ README.md
│ data/
```

---

## ✅ Notes

This project is optimized for:
✅ Zero GPU machines  
✅ Fast inference  
✅ Minimal errors  
✅ Interview-ready demonstration

[https://github.com/Yaswanth-3107/knowledge-bot/blob/main/Screenshot%202025-11-09%20235549.png]

