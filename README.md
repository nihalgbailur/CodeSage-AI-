# ** CodeSage AI 🧙‍♂️💻** 🚀🧠  
*A Streamlit-based AI-powered code assistant using LangChain & Ollama*

---

## **📌 Overview**  
DeepSeek Code Companion is an **AI-powered pair programming assistant** that helps with **debugging, code documentation, and solution design**. It runs **locally** using the **DeepSeek-r1:1.5b** model via **Ollama** and leverages **LangChain** for structured AI interactions.

---

## **⚡ Features**  
✅ **Chat-based AI assistant** for coding help  
✅ **Supports debugging, documentation, and code explanations**  
✅ **Dark-themed UI** with real-time streaming responses  
✅ **Runs locally** using **DeepSeek-r1:1.5b** via Ollama  
✅ **Optimized performance** with `num_threads=4`  
✅ **Persist chat history** with `st.session_state`  

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/GenAIDeepSeek.git
cd GenAIDeepSeek
```

### **2️⃣ Create & Activate Virtual Environment**  
```bash
python3 -m venv myenv  # Create virtual environment
source myenv/bin/activate  # Activate (Mac/Linux)
myenv\Scripts\activate  # Activate (Windows)
```

### **3️⃣ Install Dependencies**  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **4️⃣ Start Ollama Server & Load Model**  
First, make sure **Ollama** is installed:  
```bash
curl -fsSL https://ollama.ai/install.sh | sh  # Install Ollama
```

Then, **start the Ollama server** and **load the DeepSeek model**:
```bash
ollama serve  # Start Ollama
ollama pull deepseek-r1:1.5b  # Load the model
```

### **5️⃣ Run the Application**  
Once Ollama is running, start the Streamlit app:  
```bash
streamlit run app.py
```

Your app should now be accessible at **http://localhost:8501** 🎯

---

## **📁 Project Structure**  
```
GenAIDeepSeek/
│── myenv/                   # Virtual environment (not tracked by Git)
│── .gitignore                # Ignore unnecessary files (myenv, __pycache__, etc.)
│── app.py                    # Main Streamlit application
│── requirements.txt           # Dependencies list
│── README.md                 # Project documentation
```

---

## **📜 Code Breakdown**

### **🔹 `app.py` - Main Application**
#### **1️⃣ Import Required Libraries**
```python
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
```
- **Streamlit** handles the UI.
- **LangChain** manages AI prompts and conversation flow.
- **Ollama** connects the local LLM model.

#### **2️⃣ UI Customization (Dark Mode)**
```python
st.set_page_config(page_title="DeepSeek Code Companion", layout="wide")
st.markdown("""
    <style>
        body { background-color: #1a1a1a; color: #ffffff; }
        .stApp { background-color: #1a1a1a; }
        .sidebar .sidebar-content { background-color: #2d2d2d; }
        .stTextInput textarea { color: white !important; background-color: #333 !important; }
    </style>
""", unsafe_allow_html=True)
```
- **Dark-themed UI** improves visibility and readability.

#### **3️⃣ Sidebar for Model Selection**
```python
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = "deepseek-r1:1.5b"  # Fixed to use locally downloaded model
    st.write(f"🔹 **Using Model:** {selected_model}")
```
- The sidebar allows users to configure AI settings.

#### **4️⃣ Chat Processing & AI Response Handling**
```python
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "👋 Hi! I'm DeepSeek. How can I help you code today? 💻"}
    ]
```
- **Session state** is used to maintain conversation history.

```python
for message in st.session_state.message_log:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```
- **Chat message display** loops through message history.

#### **5️⃣ Streaming AI Responses**
```python
def generate_ai_response(prompt_chain):
    formatted_prompt = prompt_chain.format()
    response_stream = llm_engine.stream(formatted_prompt)
    response_text = ""
    for chunk in response_stream:
        response_text += chunk.content if hasattr(chunk, 'content') else str(chunk)
        yield response_text
```
- **Fix for AIMessageChunk** ensures correct content extraction.
- **Streaming response** improves UX by displaying text in real-time.

#### **6️⃣ Handling User Input & Updating Chat**
```python
user_query = st.chat_input("Type your coding question here...")

if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response_generator = generate_ai_response(prompt_chain)
        response_placeholder = st.empty()
        response_text = ""
        for text in ai_response_generator:
            response_text = text
            response_placeholder.markdown(response_text)
    st.session_state.message_log.append({"role": "ai", "content": response_text})
    st.rerun()
```
- **User input is processed** and added to session state.
- **Spinner UI** indicates processing.
- **Rerun UI update** ensures seamless response display.

---

## **📝 License**  
This project is **open-source** under the **MIT License**.  

---

## **🎯 Contributors**  
👤 **Nihal G Bailur** – *ADAS Engineer, AI Enthusiast*  

💡 Built with **Streamlit**, **LangChain**, and **Ollama** ❤️  

---

🚀 **Enjoy coding with DeepSeek Code Companion!** 🎯

