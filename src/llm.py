from langchain_ollama import OllamaLLM

class LLMmodel:
    def __init__(self):
        self.llm=OllamaLLM(
            model="gemma3:4b",
            temperature=0
        )
    
    def generate_response(self, prompt):
        response=self.llm.invoke(prompt)
        return response
    
# llm=LLMmodel()
# print(llm.generate_response("hi"))