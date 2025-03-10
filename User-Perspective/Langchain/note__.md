# LangChain Models Mind Map

## LangChain
LangChain is a framework for developing applications powered by large language models (LLMs). It provides several components to interact with AI models efficiently.

### 1. Models
Models are the core interface through which you interact with AI models in LangChain.
- **Language Model:** LLMs handle text-to-text requests and responses.
- **Embedding Model:** Converts text into vectors for semantic search.

### 2. Prompts
Prompts are the inputs provided to the LLM to generate responses.

### 3. Chains
Chains allow combining multiple components (models, prompts, and memory) to create more complex workflows.

### 4. Memory
- Memory helps retain context across interactions.
- LLM API calls are stateless, but memory can store previous interactions.

### 5. Indexes
Indexes connect your application to external knowledge sources like PDFs, websites, or databases.
- **Components of Indexes:**
  - Doc Loader
  - Text Splitter
  - Vector Store/Database
  - Retrievals

### 6. AI Agents
AI agents have:
- **Reasoning capability**
- **Tools** to perform actions based on prompts and external data sources.

---
