import os
import streamlit as st
from app_core import build_agent, list_sessions, runtime_config

st.set_page_config(page_title="Knowledge Bot", page_icon="🤖", layout="centered")
st.title("🤖 Conversational Knowledge Bot (Groq-powered)")
st.caption("Memory + Tools + Wikipedia + SerpAPI + DDG")

# Sidebar
with st.sidebar:
    st.subheader("⚙️ Settings")

    sessions = list_sessions()
    default = os.getenv("DEFAULT_SESSION_ID", "default")

    if default not in sessions:
        sessions = [default] + sessions

    selected = st.selectbox("Choose session", sessions, key="session_select")

    cfg = runtime_config()
    st.write("### Config")
    st.json(cfg)

# Build agent when session changes
if "agent_loaded_for" not in st.session_state or st.session_state["agent_loaded_for"] != selected:
    agent, memory = build_agent(selected)
    st.session_state.agent = agent
    st.session_state.memory = memory
    st.session_state.messages = []
    st.session_state["agent_loaded_for"] = selected

# Chat UI
for role, text in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(text)

prompt = st.chat_input("Ask anything...")
if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            result = st.session_state.agent.invoke({"input": prompt})
            reply = result.get("output", "")
        except Exception as e:
            reply = f"Error: {e}"

        st.markdown(reply)
        st.session_state.messages.append(("assistant", reply))
