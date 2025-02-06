import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


# 🚀 **Initialize Chat Engine**
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# 🌟 Custom Dark Theme UI
st.set_page_config(page_title="DeepSeek Code Companion", layout="wide")
st.markdown("""
    <style>
        body { background-color: #1a1a1a; color: #ffffff; }
        .stApp { background-color: #1a1a1a; }
        .sidebar .sidebar-content { background-color: #2d2d2d; }
        .stTextInput textarea { color: white !important; background-color: #333 !important; }
        .stSelectbox div[data-baseweb="select"], div[role="listbox"] div {
            background-color: #3d3d3d !important; color: white !important;
        }
        .stChatMessage { padding: 10px; border-radius: 10px; }
        .stChatMessage[data-testid="stChatMessage-user"] { background-color: #444; }
        .stChatMessage[data-testid="stChatMessage-ai"] { background-color: #2d2d2d; }
    </style>
""", unsafe_allow_html=True)

# 🚀 **Title & Sidebar Configuration**
st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")


with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = "deepseek-r1:1.5b"  # Fixed to use locally downloaded model
    st.write(f"🔹 **Using Model:** {selected_model}")

    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert  
    - 🐞 Debugging Assistant  
    - 📝 Code Documentation  
    - 💡 Solution Design  
    """)
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# 🤖 **Initialize Chat Engine**
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3,
    num_threads=4  # Improve performance on multi-core CPUs
)

# 🎯 **System Prompt for AI**
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# 📝 **Session State for Chat History**
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "👋 Hi! I'm DeepSeek. How can I help you code today? 💻"}
    ]

# 🗂️ **Chat Message Display**
chat_container = st.container()


with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 🔍 **Build Prompt Chain**
def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

# 🚀 **Generate AI Response (Streaming - Fixed AIMessageChunk Issue)**
def generate_ai_response(prompt_chain):
    formatted_prompt = prompt_chain.format()  # Convert chain into actual prompt text
    response_stream = llm_engine.stream(formatted_prompt)  # Streaming API for better performance
    response_text = ""

    for chunk in response_stream:
        # Fix: Ensure AIMessageChunk is converted to string properly
        if hasattr(chunk, 'content'):
            response_text += chunk.content  # Extract text content
        else:
            response_text += str(chunk)  # Fallback to string conversion

        yield response_text  # Stream response in real-time

# ✏️ **Chat Input Handling**
user_query = st.chat_input("Type your coding question here...")



if user_query:
    # 📝 Append User Query to Session History
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # 🤖 AI Processing
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response_generator = generate_ai_response(prompt_chain)

        # Display AI response as it's generated
        response_placeholder = st.empty()
        response_text = ""

        for text in ai_response_generator:
            response_text = text
            response_placeholder.markdown(response_text)

        # Append AI response to session history
        st.session_state.message_log.append({"role": "ai", "content": response_text})

    # 🔄 Refresh UI Without Rerunning Everything
    st.rerun()