from agents.hanafi_agent import HanafiAgent

def main():
    agent = HanafiAgent()

    question = "intention in prayer"

    print("Question:", question)
    print("\nResults:\n")

    results = agent.answer(question, top_k=5)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
