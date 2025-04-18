import os
import sys
from dotenv import load_dotenv
from crewai import Agent

IS_MIGRATE = 'migrate' in sys.argv

if not IS_MIGRATE:
    load_dotenv()
    from langchain_groq import ChatGroq  
    from .wikipedia_tool import WikipediaTool

    def make_llm():
        return ChatGroq(
            temperature=0.7,
            model_name="groq/llama3-70b-8192",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            max_tokens=2048,  # Limite por resposta do LLM
            max_retries=2  # Reduz tentativas de reprocessamento
        )


    wiki_tool = WikipediaTool()

    pesquisador = Agent(
        role="Pesquisador de Conteúdo",
        goal="Gerar dados brutos em texto puro (sem formatação)",
        backstory="Especialista em síntese de dados relevantes da Wikipedia.",
        tools=[wiki_tool],
        llm=make_llm(),
        max_iter=2,  # Limita etapas de processamento
        allow_delegation=False,  # Força conclusão completa da pesquisa
        memory=True,  # Mantém histórico do processo
    )

    escritor = Agent(
        role="Escritor de Artigos",
        goal="Gerar artigos práticos e concisos, esperando o resultado do pesquisador",
        backstory="Redator técnico com foco em objetividade.",
        llm=make_llm(),
        max_iter=3,
        allow_delegation=False,  # Força conclusão completa da pesquisa
        memory=True,  # Mantém histórico do processo 
    )
else:
    pesquisador = None
    escritor = None
