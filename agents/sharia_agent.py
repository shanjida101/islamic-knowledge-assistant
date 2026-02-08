import numpy as np
from agents.base_agent import BaseAgent


class ShariaAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "data/sharia_principles.json",
            ["text"]
        )

    def answer(self, question, top_k=3):
        q_emb = np.array(
            self.model.encode([question]),
            dtype="float32"
        )

        _, indices = self.index.search(q_emb, top_k)

        answers = []
        for i in indices[0]:
            entry = self.data[i]
            answers.append(
                f"{entry.get('source', 'Source')} — {entry.get('text')}"
            )

        return answers
