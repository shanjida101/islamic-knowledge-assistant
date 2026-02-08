from agents.sharia_agent import ShariaAgent

agent = ShariaAgent()

print("Total entries loaded:", len(agent.data))

question = "hardship"
results = agent.answer(question, top_k=5)

print("Results count:", len(results))

for r in results:
    print(r)
