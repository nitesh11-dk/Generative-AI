from langchain_huggingface import HuggingFaceEmbeddings

embd = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "delhi is the capital of india"
vector = embd.embed_query(text)
print(str(vector))