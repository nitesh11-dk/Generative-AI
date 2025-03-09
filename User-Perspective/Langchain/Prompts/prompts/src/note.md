# LangChain Notes with Code Examples

## 1. Introduction to LangChain

LangChain is a powerful framework that simplifies the development of LLM-based applications. It provides a modular structure to build conversational agents, chatbots, and other AI applications efficiently.

---

## 2. Using `ChatGoogleGenerativeAI` for Summarization

### Code Example 1: Basic Prompt and Model Invocation

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

st.header("Research THE-BRAND")
paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical"])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"])

# Load the prompt template
template = load_prompt('template.json')

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

def main():
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    if st.button("Summarize"):
        res = model.invoke(prompt)
        st.write(res.content)

if __name__ == "__main__":
    main()
```

### Code Example 2: Using Chains for Cleaner Code

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

st.header("Research THE-BRAND")
paper_input = st.selectbox("Select Research Paper Name", [...])
style_input = st.selectbox("Select Explanation Style", [...])
length_input = st.selectbox("Select Explanation Length", [...])

template = load_prompt('template.json')

# Creating a chain for cleaner code
def main():
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    chain = template | model  # Chain simplifies invoking logic
    if st.button("Summarize"):
        res = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })
        st.write(res.content)

if __name__ == "__main__":
    main()
```

---

## 3. Creating Prompt Templates with LangChain

### Code Example 1: PromptTemplate for Research Paper Summaries

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  

1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  

Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')
```

---

## 4. Using Messages with `SystemMessage`, `HumanMessage`, and `AIMessage`

### Code Example: Message-Based Chat Flow

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

chat_history = [SystemMessage(content='You are a helpful assistant')]

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)
```

---

## 5. Using `ChatPromptTemplate` for Dynamic Inputs

### Code Example: Dynamic Chat Template for Customer Support

```python
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms what is {topic}'),
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})
print(prompt)
```

---

## 6. Key Takeaways

- Use `PromptTemplate` for structured prompts with flexible input options.
- Combine `PromptTemplate` with `ChatGoogleGenerativeAI` for efficient chaining.
- Use `SystemMessage`, `HumanMessage`, and `AIMessage` for conversational history.
- Utilize `ChatPromptTemplate` for dynamic input requirements.

These methods provide versatile ways to implement LangChain for both simple and complex AI applications.

s

