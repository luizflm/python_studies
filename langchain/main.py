from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv('./.env')

model = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview'
)

messages = [
    SystemMessage(content="Você é um assistente útil que responde perguntas."),
    HumanMessage(
        content="Olá Bot. Como você está?"),
    AIMessage(content="Estou bem, obrigado. Como posso ajudar?"),
    HumanMessage(
        content="Você pode resumir as novas features da versão 5 do FilamentPHP?")
]

res = model.invoke(messages)
print(res.text)
