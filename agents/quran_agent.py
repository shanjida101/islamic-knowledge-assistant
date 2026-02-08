import numpy as np
from agents.base_agent import BaseAgent

class QuranAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            "data/quran.json",
            ["translation_en", "translation_bn"]
        )

    def answer(self, question, top_k=3, lang="en"):
        # 1️⃣ Create query embedding (variable MUST be q_emb)
        q_emb = np.array(
            self.model.encode([question]),
            dtype="float32"
        )

        # 2️⃣ FAISS search (returns distances, indices)
        distances, indices = self.index.search(q_emb, top_k)

        # 3️⃣ Build answers
        answers = []
        for i in indices[0]:
            v = self.data[i]
            text = v["translation_bn"] if lang == "bn" else v["translation_en"]
            answers.append(f"{v['surah']}:{v['ayah']} — {text}")

        return answers
