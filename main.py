from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, tool

system_prompt = """
You are a helpful AI agent that solves tasks by writing Python code.

Always structure your responses like this:

Thoughts:
<your reasoning here>

Code:
```python
# Your python code here
```<end_code>

Available tools:
- wiki(query: str) -> str: Returns basic facts about well-known countries.
- duckduckgo_search(query: str) -> str: Searches the web for relevant information.

Important instructions:
- Always use wiki() first when the question is about a country or a capital city.
- Use duckduckgo_search() if wiki is not sufficient.
- Never invent or create new tool names.
- Only call available tools exactly as described above.
- Always produce valid Python code between ```python ...```<end_code> blocks.
"""


@tool
def wiki(query: str) -> str:
    """
    Returns basic facts about well-known countries.

    Args:
        query (str): The name of the country to search for.
    """
    data = {
        "Norway": "The capital of Norway is Oslo.",
        "Brazil": "The capital of Brazil is Brasília.",
        "Japan": "The capital of Japan is Tokyo.",
    }
    return data.get(query, "Sorry, I don't know the answer to this topic.")

# Configure the local model
model = LiteLLMModel(
    model_id="ollama/llama3",
    api_base="http://localhost:11434",
    num_ctx=4096,
    system_prompt=system_prompt,
)

# Add the DuckDuckGoSearchTool and custom tool
agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(), wiki],
    add_base_tools=True,
)

while True:
    question = input("💬 Your question (or type 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        break

    answer = agent.run(question)
    print("🤖", answer)
