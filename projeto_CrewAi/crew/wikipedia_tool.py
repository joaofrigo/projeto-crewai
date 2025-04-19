from crewai_tools import RagTool
import requests

class WikipediaTool(RagTool):
    """
    Ferramenta que busca resumos informativos de tópicos na Wikipedia em português.
    Utiliza a API pública da Wikipedia para retornar texto puro sobre um determinado assunto.
    """
    name: str = "WikipediaFetcher"
    description: str = "Busca informações relevantes na Wikipedia em português sobre um determinado assunto."

    def _run(self, topic: str) -> str:
        """
        Consulta a Wikipedia sobre um tópico específico.

        Args:
            topic (str): O tema a ser pesquisado.

        Returns:
            str: Texto extraído da Wikipedia ou mensagem de erro se o tópico for inválido.
        """
        url = "https://pt.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": "1",
            "explaintext": "1",
            "titles": topic,
            "format": "json",
            "utf8": "1",
            "redirects": "1"
        }

        response = requests.get(url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))

        # Página não encontrada
        if "missing" in page:
            return "Tópico não encontrado"

        extract = page.get("extract", "").strip()

        # Conteúdo vazio ou desambiguação
        if not extract or "pode referir-se a" in extract.lower():
            return "Tópico não encontrado"

        return extract[:3500]  # Limita o conteúdo retornado para evitar sobrecarregar o servidor free
