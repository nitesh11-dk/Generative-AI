# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage , HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content='you are an helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms what is {topic}')
# ])

# prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})
# print(prompt)

 # ! this doesn't work 
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system','you are an helpful {domain} expert'),
    ('human','Explain in simple terms what is {topic}'),
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)