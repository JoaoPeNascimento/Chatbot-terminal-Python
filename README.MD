# 🤖 Chatbot de Terminal com LangChain e Gemini

Um chatbot de terminal inteligente construído em Python, utilizando a estrutura **LangChain** para orquestração e o modelo **Google Gemini 2.5 Flash** como cérebro. O projeto possui memória de conversação (Context Awareness) e respostas em tempo real (Streaming).

## 🚀 Funcionalidades

* **Integração com LLM:** Utiliza o modelo `gemini-2.5-flash` do Google, otimizado para velocidade e precisão.
* **Memória de Conversação:** O bot lembra do contexto das mensagens anteriores dentro da sessão (utilizando `RunnableWithMessageHistory`).
* **Streaming de Resposta:** As respostas são exibidas no terminal token por token (efeito de "digitação"), melhorando a experiência do usuário.
* **Segurança:** Gerenciamento de chaves de API via variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas

* [Python 3.8+](https://www.python.org/)
* [LangChain](https://www.langchain.com/) (Core, Community, Google GenAI)
* [Google Gemini API](https://ai.google.dev/)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)

## 📦 Pré-requisitos

Antes de começar, você precisará de:

1.  Ter o **Python** instalado na sua máquina.
2.  Uma **API Key** do Google AI Studio. Você pode obter uma gratuitamente [aqui](https://aistudio.google.com/).

## ⚙️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clone o repositório
```bash
git clone [https://github.com/JoaoPeNascimento/Chatbot-terminal-Python](https://github.com/JoaoPeNascimento/Chatbot-terminal-Python)
cd chatbot-terminal-python
```

### 2. Crie um ambiente Virtual

É altamente recomendável usar um ambiente virtual para não conflitar bibliotecas.

- windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

- Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install langchain-google-genai langchain-community python-dotenv
```

### 4. Configura variáveis de ambiente
Crie um arquivo chamado `.env` na raiz do projeto (mesmo nível do `bot.py`). Este arquivo é ignorado pelo Git para sua segurança.

Adicione sua chave de API nele:
```Snippet de código
GOOGLE_API_KEY=sua_chave_do_google_aqui
```

## Como usar
Com o ambiente configurado e ativado, basta rodar o script principal:
```bash
python bot.py
```
*Comandos*:
 - Digite sua pergunta e aperte `Enter`.

 - Para sair, digite `sair`, `exit` ou `fui`.

## 📁 Estrutura do projeto

```chatbot-terminal-python/
│
├── bot.py           # Código principal da aplicação
├── .env             # Arquivo de configuração (NÃO COMITAR)
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Documentação do projeto
```

## 🧠 Como funciona (Deep Dive)
O código utiliza o conceito de *LCEL (LangChain Expression Language)*:

Prompt: Define a personalidade do bot ("Especialista em Python") e reserva um espaço (`MessagesPlaceholder`) para o histórico.

Modelo: Conecta ao `gemini-2.5-flash`.

Memória: A classe `RunnableWithMessageHistory` intercepta a mensagem do usuário, busca o histórico salvo na variável `store` (em memória RAM), injeta no prompt e envia para o modelo.

Streaming: O loop de resposta utiliza `.stream()` para imprimir os caracteres assim que são gerados pela API.
