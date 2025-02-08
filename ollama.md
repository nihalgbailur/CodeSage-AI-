# Running Ollama with DeepSeek-R1 1.5B in Terminal

## 📌 Prerequisites
Before running Ollama with DeepSeek-R1 1.5B, ensure you have:
- A **Linux, macOS, or Windows** machine.
- Installed **Ollama** (follow the installation steps below if not installed).

---

## 🚀 Installation Steps

### 1️⃣ Install Ollama
Run the following command to install **Ollama**:

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

For **Windows**, download and install Ollama from the official site:  
🔗 [https://ollama.com/download](https://ollama.com/download)

Verify installation:
```sh
ollama --version
```

---

### 2️⃣ Download DeepSeek-R1 1.5B Model
Run the following command to pull the **DeepSeek-R1 1.5B** model:

```sh
ollama pull deepseek-r1:1.5b
```

Check if the model is downloaded:

```sh
ollama list
```

You should see `deepseek-r1:1.5b` in the output.

---

### 3️⃣ Running the DeepSeek-R1 1.5B Model

#### ✅ **Interactive Mode**
To chat with DeepSeek-R1 1.5B interactively, run:

```sh
ollama run deepseek-r1:1.5b
```

#### ✅ **One-Time Query**
To ask a single question and get a response:

```sh
ollama run deepseek-r1:1.5b "What is the theory of relativity?"
```

#### ✅ **Using Ollama as an API**
Start the API server (optional if already running):

```sh
ollama serve
```

Then send a request:

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:1.5b",
  "prompt": "Explain quantum mechanics in simple terms."
}'
```

#### ✅ **Run in Background**
To keep the model running in the background:

```sh
nohup ollama run deepseek-r1:1.5b > output.log 2>&1 &
```

---

## 🔍 **Checking Model Location**
Ollama stores models in:

- **Linux/macOS:** `~/.ollama/models`
- **Windows:** `C:\Users\YourUsername\.ollama\models`

To list stored models:

```sh
ls ~/.ollama/models  # Linux/macOS
dir C:\Users\YourUsername\.ollama\models  # Windows
```

---

## ✅ **Uninstall Ollama**
If you need to remove Ollama:

- **Linux/macOS:**
  ```sh
  rm -rf ~/.ollama
  ```

- **Windows:**  
  Delete `C:\Users\YourUsername\.ollama\`

---

## 🎯 **Troubleshooting**

1. **"Command not found" error?**  
   → Ensure Ollama is installed and added to the system PATH.

2. **"Model not found" error?**  
   → Make sure you ran `ollama pull deepseek-r1:1.5b`.

3. **Ollama crashes on large queries?**  
   → Try increasing system memory or use a smaller model.

---

## 🔹 **Ollama Terminal Commands**

| Command         | Description |
|----------------|-------------|
| `/set`         | Set session variables |
| `/show`        | Show model information |
| `/load <model>` | Load a session or model |
| `/save <model>` | Save your current session |
| `/clear`       | Clear session context |
| `/bye`         | Exit |
| `/?`, `/help`  | Help for a command |
| `/? shortcuts` | Help for keyboard shortcuts |

---

## 🎉 **Enjoy Chatting with DeepSeek-R1 1.5B!** 🚀

