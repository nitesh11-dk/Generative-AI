from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


documents = [
    "delhi is the capital of india",
    "kolkata is captial of west bengal"
]

emb =OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

# res = emb.embed_query("Delhi is the capital of India")
res = emb.embed_documents(documents)

print(str(res))