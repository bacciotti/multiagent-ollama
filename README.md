# SmolAgent with Local LLM and Custom Tools

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)


This project demonstrates how to build a Code Agent using [smolagents](https://github.com/smol-ai/smol-agent), connected to a local LLM running through [Ollama](https://ollama.com/).

The agent can:
- Answer simple factual questions using a custom `mini_wikipedia` tool.
- Perform live web searches using `DuckDuckGoSearchTool`.
- Execute reasoning steps by generating and running Python code.

---

## 🚀 Quickstart

### 1. Install `pipenv` (if you don't have it)

```bash
pip install pipenv
```

### 2. Install dependencies

```git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pipenv install
```
### 4. Ensure Ollama is installed and running
```
brew install ollama
ollama pull llama3
```

### 5. Run the agent

```
pipenv run python main.py
```

### 💡 Notes
- This project uses LiteLLMModel to connect to Ollama's OpenAI-compatible local server.
- No Hugging Face API keys are required.
- Works 100% locally once the model is pulled via Ollama.