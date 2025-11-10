# 🚀 Conversational Knowledge Bot  
### LangChain + Groq + Wikipedia + DuckDuckGo + SerpAPI + Memory + Streamlit

A blazing-fast, multi-tool conversational knowledge assistant built for real-world productivity, AI agent workflows, and interview-ready demos.

It combines:  
✅ LLM reasoning (ReAct)  
✅ Search tools  
✅ Wikipedia  
✅ Persistent memory  
✅ Session management  
✅ Groq ultra-fast inference  
✅ Streamlit chat interface  

---





---

## ✅ Features

- 🧠 **Conversational Memory**  
  Remembers discussion context across multiple turns and sessions.

- 🔍 **Multi-Tool Search System**  
  Wikipedia + DuckDuckGo + SerpAPI for deep, multi-source knowledge retrieval.

- 🤖 **ReAct Agent Architecture**  
  Enables reasoning + tool calling for accurate answers.

- ⚡ **Groq-powered LLaMA 3.1 (8B Instant)**  
  Ultra-fast inference, zero GPU required.

- 🖥️ **Streamlit Chat UI**  
  Clean, simple, real-time web interface.

- 📂 **File-based or SQLite Memory**  
  Works on all systems without complex setup.

- ✅ **Interview-Ready Project**  
  Perfect for showcasing agent design + tool integration.

---

## 🏗️ System Architecture

User → Streamlit → ReAct Agent → Tools → Groq LLM → Output

<p align="center">
  <img src="https://github.com/Yaswanth-3107/knowledge-bot/blob/main/architecture.png" width="80%" />
</p>


---

## 📁 Project Structure

knowledge-bot/
│ app_core.py
│ app_streamlit.py
│ requirements.txt
│ .env
│ README.md
│ data/
      memory.sqlite

---

## ⚙️ Requirements

- Python 3.10 or 3.11  
- Groq API Key  
- SerpAPI Key (optional)  
- Streamlit  
- LangChain 0.2+  

---

## 📦 Installation

python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

---

## 🔐 .env Setup

- APP_MODE=streamlit
- MODEL_BACKEND=groq
- GROQ_API_KEY=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
- GROQ_MODEL=llama-3.1-8b-instant
- USE_SERPAPI=true
- SERPAPI_API_KEY=2882a1496509b001a2052523ffddee2f38fb16a2e7a752bfad9d6bd8284d4046
- MEMORY_BACKEND=file
- DEFAULT_SESSION_ID=default
- SQLITE_PATH=data/memory.sqlite

---

## ▶️ Run the App

streamlit run app_streamlit.py

##  Screenshots of chat
<p align="center">
  <img src="https://raw.githubusercontent.com/Yaswanth-3107/knowledge-bot/main/Screenshot%202025-11-09%20235100.png" width="80%" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Yaswanth-3107/knowledge-bot/main/Screenshot%202025-11-09%20235549.png" width="80%" />
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/Yaswanth-3107/knowledge-bot/main/Screenshot%202025-11-10%20000353.png" width="80%" />
</p>


---

## ✅ Why This Project Stands Out

- Real agent system  
- Multi-search integration  
- Persistent memory  
- Extremely fast  
- Clean UI  
- Production-ready demo  

---

## 📜 License

MIT License

---

## 🙌 Author

Yaswanth  
Open-source builder and AI systems enthusiast.
