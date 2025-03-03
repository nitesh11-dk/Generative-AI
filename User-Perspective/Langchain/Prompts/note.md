Types of prompts 

text-based prompts 
Multi-model prompts --> image ,video , or sound 

### Prompts are the input instruction or queries given to a model to  guide its output
- Dynamic prompt 
- Static Prompt 


<!-- agar tum load evn use karre ho aur like same like keys ka hona chhaiye deafult wale agar nahi hai to we can use os module to get the key and then pass it to the model -->
<!--  ex : GOOGLE_API_KEY   agar ye key ka nam hoga to load env  hume function run karn  padega and vo drrect google ke api ke y me chalal jayega -->
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from prompts!")
    gi()

def gi():
    # Initialize the model with the API key
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    res = model.invoke("What is the capital of India?")
    print(res.content)

if __name__ == "__main__":
    main()
 ```
<!--  ex : GEMINIE_API_KEY or different naame hai to  vo drrect google ke api ke  me nahi  chalal jayega we have to first get that key theen pass it to model -->
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os  # Required to check if the env variable is loaded

# Load environment variables
load_dotenv()

def main():
    print("Hello from prompts!")
    gi()

def gi():
    # Ensure the environment variable is loaded
    api_key = os.getenv("GEMINI_API_KEY")  # This confirms it's correctly loaded
    
    if not api_key:
        print("Error: GEMINI_API_KEY is not set or loaded!")
        return

    # Initialize the model with the API key
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', google_api_key=api_key)
    
    res = model.invoke("What is the capital of India?")
    print(res.content)

if __name__ == "__main__":
    main()

```
### **🤔 Kaun Responsible Hota Hai?**
| Scenario | Responsible for API Key Injection |
|----------|-----------------------------------|
| ✅ **Name is `GOOGLE_API_KEY`** | `ChatGoogleGenerativeAI` automatically reads it from environment |
| ❌ **Name is different (e.g., `GEMINI_API_KEY`)** | We need to use `os.getenv()` and pass manually |

---

### **💡 Best Practice**
Agar **default (`GOOGLE_API_KEY`)** kaam kar raha hai, toh **directly use kar lo**.  
Agar **custom name hai (`GEMINI_API_KEY`)**, toh **manually pass karo**.  


## StreamLit 
 - to run go in .venv where streamlit is installed and use the strreamlit commands

 ## Prompts 
 