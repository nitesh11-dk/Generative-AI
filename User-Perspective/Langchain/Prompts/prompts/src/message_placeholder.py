from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder # type: ignore


chat_template = ChatPromptTemplate([
    ('system','you are an helpful coustomer support expert'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human',' {query}'),
])


chat_history =[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())


prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my fund'})
    
print(prompt)