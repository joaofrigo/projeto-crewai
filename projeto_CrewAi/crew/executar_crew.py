from crewai import Task, Crew
from .agentes import pesquisador, escritor
from .wikipedia_tool import WikipediaTool

def gerar_artigo_completo(topico: str) -> str:
    """
    Gera um artigo completo com base em um tópico. Primeiro, pesquisa o tópico na Wikipedia e depois escreve o artigo com base nos dados obtidos.

    Args:
        topico (str): O tema da pesquisa.

    Returns:
        str: Artigo gerado ou mensagem de erro se o tópico não for encontrado.
    """
    
    # Verifica se o conteúdo do tópico existe na Wikipedia
    wikipedia_tool = WikipediaTool()
    conteudo_wiki = wikipedia_tool._run(topico)

    if conteudo_wiki == "Tópico não encontrado":
        return "Tópico não encontrado"
    
    # Tarefa de Pesquisa: Pesquisar sobre o tópico usando o WikipediaTool
    tarefa_pesquisa = Task(
        description=f"Pesquisar sobre o tema '{topico}' utilizando a Wikipedia e o WikipediaTool",
        expected_output="Resumo informativo com detalhes importantes",
        agent=pesquisador,
        tools=[WikipediaTool()]  # O pesquisador usa o WikipediaTool
    )

    # Tarefa de Escrita: Gerar o artigo baseado na pesquisa anterior
    tarefa_escrita = Task(
        description=(
            "Escrever um artigo com no mínimo 300 palavras baseado nas informações da tarefa anterior. "
            "O artigo deve seguir a estrutura abaixo:\n\n"
            "1. Introdução: Apresente o tema do artigo, explicando brevemente sobre o que será discutido.\n"
            "2. Desenvolvimento: Apresente as informações mais detalhadas, argumente sobre o tema, desenvolva ideias principais e secundárias.\n"
            "3. Conclusão: Resuma os pontos abordados, fornecendo uma reflexão final sobre o tema.\n\n"
            "A conclusão deve trazer um fechamento claro e relacionado ao tema discutido. Escreva o artigo em português." \
            "é de suma importância e o ponto mais relevante, que para o resultado seja adequado, use o context da tarefa_pesquisa" \
            "\n Pode e deve esperar até a pesquisa terminar, nunca poderá enviar apenas: I now can give a great answer"
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

    # Retorna o resultado das tarefas
    resultado = crew.kickoff()
    return resultado
