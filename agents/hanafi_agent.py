import numpy as np
from agents.base_agent import BaseAgent


class HanafiAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "data/hanafi_fiqh.json",
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
                f"""
                <strong>📘 Source:</strong> {entry.get('source', 'Al-Hidayah (Hanafi fiqh)')}<br><br>
                <strong>Hanafi Text:</strong><br>
                {entry.get('text')}
                """
            )

        return answers
