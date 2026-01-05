import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def iniciar_chatbot():
    print("Iniciando o chatbot... (digite 'sair' para encerrar)")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente virtual útil."),
        ("system", "Responda de forma concisa em português."),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ])

    parser = StrOutputParser()

    chain = prompt | llm | parser

    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    session_id = "sessao_usuario_1"

    while True:
        try:
            user_input = input("\nVocê: ")
            
            if user_input.lower() in ["sair", "exit", "fui"]:
                print("Bot: Até mais!")
                break

            print("Gemini: ", end="", flush=True)
            
            for chunk in chain_with_history.stream(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            ):
                print(chunk, end="", flush=True)
            print()

        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    iniciar_chatbot()
