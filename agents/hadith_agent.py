import numpy as np
from agents.base_agent import BaseAgent

class HadithAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "data/hadith.json",
            ["text_en"]
        )

    def answer(self, question, top_k=3):
        # 1. Create query embedding (THIS LINE WAS BROKEN BEFORE)
        q_emb = np.array(
            self.model.encode([question]),
            dtype="float32"
        )

        # 2. FAISS search
        distances, indices = self.index.search(q_emb, top_k)

        # 3. Format answers
        answers = []
        for i in indices[0]:
            h = self.data[i]
            answers.append(
                f"{h['collection']} #{h['hadith_number']} — {h['text_en']}"
            )

        return answers
