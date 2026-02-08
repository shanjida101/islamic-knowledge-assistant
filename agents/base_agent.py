import json
import numpy as np
import faiss
import streamlit as st
from sentence_transformers import SentenceTransformer


@st.cache_resource(show_spinner=False)
def load_embedding_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


class BaseAgent:
    def __init__(self, json_path, text_fields):
        # Load model ONCE per app lifetime
        self.model = load_embedding_model()

        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.texts = [
            " ".join(str(item.get(f, "")) for f in text_fields)
            for item in self.data
        ]

        # Build embeddings only once per agent instance
        self.embeddings = self.model.encode(
            self.texts,
            convert_to_numpy=True,
            show_progress_bar=True
        ).astype("float32")

        dim = self.embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)
