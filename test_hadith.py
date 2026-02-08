from agents.hadith_agent import HadithAgent

agent = HadithAgent()

q = "intention"
answers = agent.answer(q)

for a in answers:
    print(a)
