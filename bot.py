from ast import parse
from html import parser
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def iniciar_chatbot():
    print("Iniciando o chatbot... (digite 'sair' para encerrar)")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente virtual útil. Responda apenas em português."),
        ("user", "{input}")
    ])

    parser = StrOutputParser()

    chain = prompt | llm | parser

    while True:
        try:
            user_input = input("\nVocê: ")
            
            if user_input.lower() in ["sair", "exit", "fui"]:
                print("Bot: Até mais!")
                break

            print("Gemini: ", end="", flush=True)
            
            # O streaming também funciona nativamente
            for chunk in chain.stream({"input": user_input}):
                print(chunk, end="", flush=True)
            print()

        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    iniciar_chatbot()
