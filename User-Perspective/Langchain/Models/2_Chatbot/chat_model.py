from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4',temperature=0.3,max_completion_tokens=10) # temp == 0 to 2 , creativeness

result = model.invoke("what is the captial of india ?")

# print(result)
print(result.content)
#  ! yaha jo result milta hai , vo yak json form me hota hai with much more details 