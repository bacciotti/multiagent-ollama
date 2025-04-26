from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, tool

@tool
def mini_wikipedia(query: str) -> str:
    """
    Returns basic facts about well-known countries.
    """
    data = {
        "Norway": "The capital of Norway is Oslo.",
        "Brazil": "The capital of Brazil is Brasília.",
        "Japan": "The capital of Japan is Tokyo.",
    }
    return data.get(query, "Sorry, I don't know the answer to this topic.")

# Configure the local model
model = LiteLLMModel(
    model_id="ollama/codellama:latest",
    api_base="http://localhost:11434",
    num_ctx=4096,
)

# Add the DuckDuckGoSearchTool and custom tool
agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(), mini_wikipedia],
    add_base_tools=True,
)

while True:
    question = input("💬 Your question (or type 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        break

    answer = agent.run(question)
    print("🤖", answer)
