import os
import sys
from dotenv import load_dotenv
from crewai import Agent

# Verifica se o comando atual é 'migrate' para evitar carregar modelos durante migração
IS_MIGRATE = 'migrate' in sys.argv

if not IS_MIGRATE:
    load_dotenv()

    from langchain_groq import ChatGroq  
    from .wikipedia_tool import WikipediaTool

    def make_llm():
        """
        Cria e retorna uma instância configurada do modelo ChatGroq.

        Returns:
            ChatGroq: Instância configurada do modelo LLM com chave, temperatura e limites definidos.
        """
        return ChatGroq(
            temperature=0.7,
            model_name="groq/llama3-70b-8192",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            max_tokens=2048,
            max_retries=2
        )

    # Ferramenta de busca na Wikipedia usada pelo agente pesquisador
    wiki_tool = WikipediaTool()

    pesquisador = Agent(
        role="Pesquisador de Conteúdo",
        goal="Gerar dados brutos em texto puro (sem formatação), utilizando tools",
        backstory="Especialista em síntese de dados relevantes da Wikipedia.",
        tools=[wiki_tool],
        llm=make_llm(),
        max_iter=2,
        allow_delegation=False,
        memory=True,
    )

    escritor = Agent(
        role="Escritor de Artigos",
        goal="Gerar artigos práticos e concisos, esperando o resultado do pesquisador",
        backstory="Redator técnico com foco em objetividade.",
        llm=make_llm(),
        max_iter=5,
        allow_delegation=False,
        memory=True,
    )
else:
    pesquisador = None
    escritor = None
