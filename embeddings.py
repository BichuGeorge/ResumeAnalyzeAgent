import requests
from tqdm import tqdm
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


class EuriaiEmbeddings(Embeddings):
    """Custom embedding class to use Euriai for FAISS queries."""
    def __init__(self, api_key, model="text-embedding-3-small"):
        self.api_key = api_key
        self.model = model
        self.url = "https://api.euron.one/api/v1/euri/embeddings"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def embed_documents(self, texts):
        """Embed a list of texts (for retriever queries)."""
        embeddings = []
        for text in texts:
            payload = {"input": text, "model": self.model}
            response = requests.post(self.url, headers=self.headers, json=payload)
            response.raise_for_status()
            emb_response = response.json()
            embeddings.append(emb_response["data"][0]["embedding"])
        return embeddings

    def embed_query(self, text):
        """Embed a single query."""
        return self.embed_documents([text])[0]


