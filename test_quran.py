from agents.quran_agent import QuranAgent

def main():
    agent = QuranAgent()

    question = "guidance"

    print("Question:", question)
    print("\nResults:\n")

    results = agent.answer(question, top_k=5, lang="en")

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
