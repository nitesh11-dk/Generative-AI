from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

# Load environment variables (if any)
load_dotenv()

# Initialize the HuggingFace embeddings model
# 'sentence-transformers/all-MiniLM-L6-v2' is a lightweight and efficient model for embedding text
embd = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# List of documents (sentences) to compare against
# These sentences describe the character Thomas Shelby from Peaky Blinders
document = [
    "He is a war veteran who served in World War I and suffers from PTSD.",
    "Known for his sharp mind, he turns a small gang into a powerful business empire.",
    "Despite his ruthless nature, he deeply cares for his family and their legacy.",
    "His iconic style includes a flat cap, tailored suits, and a cigarette in hand.",
    "Thomas Shelby is the ambitious leader of the Peaky Blinders gang.",
]

# Query to search for relevant information
query = 'whose is thomas'

# Compute embeddings for the documents
# This converts each document into a numerical vector representation
doc_emb = embd.embed_documents(document)

# Compute embedding for the query
query_emb = embd.embed_query(query)

# Compute cosine similarity between query embedding and document embeddings
# Cosine similarity measures how similar two vectors are (ranges from -1 to 1)
# We pass the query embedding inside a list because cosine_similarity expects a 2D array
scores = cosine_similarity([query_emb], doc_emb)[0]

# Since cosine_similarity returns a list of scores, we need to find the highest similarity score
# To do this, we enumerate the scores so that each score retains its original document index
# Sorting the list based on similarity scores in ascending order and selecting the last (highest) one
index, value = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Display the most relevant document based on the query
print("+++++++++++++++++++++++++++++++++++")
print(query + "?")
print(document[index])  # The document with the highest similarity score
print("similarity score", value)
