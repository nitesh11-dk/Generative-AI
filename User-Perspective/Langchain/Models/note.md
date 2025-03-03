## OpenAI API Key Configuration
- The API key must be set either by passing `api_key` to the client or by setting the `OPENAI_API_KEY` environment variable.
- The environment variable must be named exactly `OPENAI_API_KEY` for `load_dotenv()` to detect it correctly.
- Similar rules apply for Anthropic API keys.

## Temperature Parameter
- Controls the randomness of a language model's output.
- Lower values (0 to 0.3): More deterministic and predictable.
- Higher values (0.7 to 1.5): More random, creative, and diverse.
- Temperature is the value that control the output value based on input 
- If temperature is = 0 ,  then output will same for me same input , it will not change 
- IF temperature is > 0 , then output will different form the same input , it wil change

## Max Completion Tokens
- Defines the maximum number of tokens the model can generate in a response.
- Tokens are not just words; they can be parts of words or punctuation.

## Gemini API
- The Gemini API is free for a limited time.
- Currently working fine but subject to change.

## Open-Source Models
- Available on platforms like Hugging Face.
- Various models can be found based on use cases like text generation, vision, and reinforcement learning.



### **Conclusion**  
- `enumerate(scores)` creates an iterator that pairs each element in `scores` with its index.  
- It does **not** directly print values; you need to loop through it or convert it into a list.  
- Useful when you need both **index and value** while iterating.  
- Example output: `[(0, 85), (1, 90), (2, 78), (3, 92), (4, 88)]` when converted to a list.  

Let me know if you need further explanation! 🚀