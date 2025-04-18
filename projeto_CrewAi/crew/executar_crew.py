from crewai import Task, Crew
from .agentes import pesquisador, escritor
from .wikipedia_tool import WikipediaTool

def gerar_artigo_completo(topico: str) -> str:

    # Verifica em primeiro lugar se o output do wikipediatool é correto para evitar erros. Se não, volta com "tópico não encontrado" pra view
    wikipedia_tool = WikipediaTool()
    conteudo_wiki = wikipedia_tool._run(topico)

    if conteudo_wiki == "Tópico não encontrado":
        return "Tópico não encontrado"
    
    # Tarefa de Pesquisa
    tarefa_pesquisa = Task(
        description=f"Pesquisar sobre o tema '{topico}' utilizando a Wikipedia",
        expected_output="Resumo informativo com detalhes importantes",
        agent=pesquisador,
        tools=[WikipediaTool()]  # O pesquisador usa o WikipediaTool
    )

    # Tarefa de Escrita
    tarefa_escrita = Task(
    description=(
        "Escrever um artigo com no mínimo 300 palavras baseado nas informações da tarefa anterior. "
        "O artigo deve seguir a estrutura abaixo:\n\n"
        "1. Introdução: Apresente o tema do artigo, explicando brevemente sobre o que será discutido.\n"
        "2. Desenvolvimento: Apresente as informações mais detalhadas, argumente sobre o tema, desenvolva ideias principais e secundárias.\n"
        "3. Conclusão: Resuma os pontos abordados, fornecendo uma reflexão final sobre o tema.\n\n"
        "A conclusão deve trazer um fechamento claro e relacionado ao tema discutido. Escreva o artigo em português."
    ),
    expected_output="Artigo com introdução, desenvolvimento e conclusão, contendo no mínimo 300 palavras.",
    agent=escritor,
    context=[tarefa_pesquisa]  # O escritor recebe o resumo do pesquisador
)
    # Executa as tarefas com os agentes
    crew = Crew(
        agents=[pesquisador, escritor],
        tasks=[tarefa_pesquisa, tarefa_escrita],
        verbose=True
    )

    # Inicia as tarefas
    resultado = crew.kickoff()
    return resultado
