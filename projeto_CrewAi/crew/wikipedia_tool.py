from crewai_tools import RagTool
import requests

class WikipediaTool(RagTool):
    name: str = "WikipediaFetcher"
    description: str = "Busca informações relevantes na Wikipedia em português sobre um determinado assunto."

    def _run(self, topic: str) -> str:
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

        # Verifica se a página não existe
        if "missing" in page:
            return "Tópico não encontrado"

        extract = page.get("extract", "").strip()

        # Verifica se o conteúdo é vazio ou uma página de desambiguação
        if not extract or "pode referir-se a" in extract.lower():
            return "Tópico não encontrado"

        return extract[:3500]