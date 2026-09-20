<div align="center">

# 🤖 OpenChat

**A privacy-first, local AI chatbot powered by Ollama**

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Chat with powerful AI models running **entirely on your machine** — no API keys, no cloud, no data leaving your device.

[Getting Started](#-getting-started) · [Features](#-features) · [Usage](#-usage) · [Troubleshooting](#-troubleshooting)

</div>

---

## ✨ Features

- 🔒 **100% Private** — All conversations stay on your local machine. No data is ever sent to external servers.
- ⚡ **Real-Time Streaming** — Responses are streamed token-by-token for a fluid, ChatGPT-like experience.
- 🌐 **Two Interfaces** — Choose between a sleek **Streamlit Web UI** or a lightweight **CLI** for the terminal.
- 🔄 **Conversation Memory** — Full multi-turn chat history so the model understands context across messages.
- 🎛️ **Configurable Models** — Swap models on the fly from the sidebar — use any model available in Ollama.
- 🧹 **Clear Chat History** — One-click button to reset the conversation and start fresh.
- 🚀 **Zero Cloud Dependencies** — No API keys required. Works offline after initial model download.

---

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

| Requirement | Version | Description |
|---|---|---|
| [Python](https://www.python.org/downloads/) | 3.14+ | Runtime environment |
| [Ollama](https://ollama.com/download) | Latest | Local LLM inference engine |
| [uv](https://docs.astral.sh/uv/) *(recommended)* | Latest | Fast Python package manager |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/openchat.git
cd openchat
```

### 2. Install Dependencies

<details>
<summary><b>Option A: Using uv (Recommended)</b></summary>

```bash
# Create virtual environment and install dependencies
uv sync
```

</details>

<details>
<summary><b>Option B: Using pip</b></summary>

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

</details>

### 3. Set Up Ollama

```bash
# Install the default model (Qwen 2.5 3B)
ollama pull qwen2.5:3b
```

> [!TIP]
> You can use any model supported by Ollama. Browse available models at [ollama.com/library](https://ollama.com/library).
>
> Popular choices:
> ```bash
> ollama pull llama3.2        # Meta Llama 3.2
> ollama pull mistral         # Mistral 7B
> ollama pull gemma2          # Google Gemma 2
> ollama pull phi3            # Microsoft Phi-3
> ```

### 4. Make Sure Ollama Is Running

Ollama must be running in the background before starting OpenChat. Launch the Ollama desktop app, or run:

```bash
ollama serve
```

---

## 💬 Usage

### Web UI (Streamlit)

Launch the interactive web interface:

```bash
streamlit run app.py
```

This opens a browser window at `http://localhost:8501` with:

- 💬 A clean chat interface with message history
- ⚙️ A sidebar to change the model name and clear chat history
- ⚡ Real-time streaming responses with a typing indicator

#### Web UI Walkthrough

1. **Start chatting** — Type your message in the input box at the bottom and press Enter.
2. **Change the model** — Enter a different model name in the sidebar (e.g., `llama3.2`).
3. **Clear history** — Click the "Clear Chat History" button in the sidebar to reset.

---

### CLI (Terminal)

For a lightweight terminal experience:

```bash
python main.py
```

- Type your messages and press Enter to chat.
- The model remembers the full conversation context.
- Type `exit` or `quit` to end the session.

#### Example Session

```
Chat with Qwen (type 'exit' to quit)
You: What is the capital of France?
Qwen: The capital of France is Paris. It is the largest city in France and serves
as the country's political, economic, and cultural center.

You: What is it known for?
Qwen: Paris is known for many things, including the Eiffel Tower, the Louvre Museum,
Notre-Dame Cathedral, its café culture, and world-renowned cuisine.

You: exit
```

---

## 📁 Project Structure

```
openchat/
├── app.py                # Streamlit web UI application
├── main.py               # CLI chatbot interface
├── src/
│   └── openchat/
│       └── __init__.py   # Package entry point
├── pyproject.toml        # Project metadata & dependencies (uv/PEP 621)
├── requirements.txt      # Pip-compatible dependency list
├── uv.lock               # uv lockfile for reproducible installs
├── .python-version       # Python version specification
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## ⚙️ Configuration

### Changing the Default Model

**Web UI:** Update the model name in the sidebar text input.

**CLI:** Edit the `model` parameter in [main.py](main.py):

```python
response = chat(model='your-model-name', messages=messages)
```

### Supported Models

Any model available through Ollama can be used. Some popular options:

| Model | Size | Command | Best For |
|---|---|---|---|
| `qwen2.5:3b` | ~2 GB | `ollama pull qwen2.5:3b` | Default, fast & lightweight |
| `llama3.2` | ~4.7 GB | `ollama pull llama3.2` | General purpose |
| `mistral` | ~4.1 GB | `ollama pull mistral` | Reasoning & instruction following |
| `gemma2` | ~5.4 GB | `ollama pull gemma2` | Balanced performance |
| `codellama` | ~3.8 GB | `ollama pull codellama` | Code generation |

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ Connection Error / "Ollama is not running"</b></summary>

Make sure the Ollama service is running:

```bash
ollama serve
```

Or launch the Ollama desktop application.

</details>

<details>
<summary><b>❌ Model not found</b></summary>

Pull the model first:

```bash
ollama pull qwen2.5:3b
```

Verify installed models:

```bash
ollama list
```

</details>

<details>
<summary><b>❌ Streamlit not found</b></summary>

Make sure dependencies are installed and your virtual environment is activated:

```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

</details>

<details>
<summary><b>❌ Slow responses</b></summary>

- Use a smaller model (e.g., `qwen2.5:3b` instead of a 70B model).
- Ensure no other heavy processes are consuming CPU/GPU resources.
- If you have a compatible NVIDIA GPU, Ollama will automatically use it for faster inference.

</details>

---

## 🧗 Challenges Faced

Building OpenChat came with several real-world challenges that provided valuable learning opportunities:

### 1. Streaming Responses in Streamlit
Streamlit re-runs the entire script on every interaction, which made implementing real-time token-by-token streaming tricky. The solution involved using `st.empty()` as a placeholder and appending each incoming chunk to build the response progressively — simulating a live typing effect without breaking Streamlit's execution model.

### 2. Managing Conversation State
Since Streamlit is stateless by default, preserving chat history across reruns required careful use of `st.session_state`. Ensuring messages persisted correctly — and that the UI re-rendered the full history on each rerun — took deliberate state management.

### 3. Ollama Connection & Model Availability
Handling cases where Ollama isn't running or the requested model isn't downloaded required robust error handling. Users can easily forget to start the Ollama service or pull a model beforehand, so clear error messages and in-app setup instructions were essential for a smooth experience.

### 4. Choosing the Right Default Model
Balancing model quality vs. hardware requirements was a key decision. Larger models produce better responses but are slow on consumer hardware. The `qwen2.5:3b` model was chosen as the default for its strong balance of quality, speed, and low resource usage (~2 GB).

### 5. Keeping Both Interfaces in Sync
Maintaining two separate interfaces (Streamlit Web UI and CLI) that behave consistently required careful code organization. Each interface handles the Ollama API differently — the CLI uses synchronous calls while the Web UI uses streaming — which meant duplicated logic had to stay aligned.

---

## 🛣️ Roadmap

- [ ] Add system prompt customization
- [ ] Support for image-based models (multimodal)
- [ ] Export chat history to file
- [ ] Multiple conversation sessions
- [ ] Dark/Light theme toggle for Web UI
- [ ] Docker support

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add your feature"`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Abdullah Ahmed**
- 📧 Email: abd1962964@gmail.com
- 🐙 GitHub: [@AbdullahAhmed922](https://github.com/AbdullahAhmed922)

---

<div align="center">

**If you found this project useful, give it a ⭐!**

</div>
