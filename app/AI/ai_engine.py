from ollama import Client
import os

class AI_engine:

    def __init__(self):
        self.host=os.getenv("OLLAMA_HOST")
        self.client=Client(host=self.host)
        self.model="gemma:2b"

    def chat(self,messages:list):
        response=self.client.chat(model=self.model,messages=messages)
        return response["message"]["content"]
    
engine=AI_engine()