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
        extract = page.get("extract", "Nada encontrado sobre o tema.")
        return extract[:3500]

# Instanciando a ferramenta
tool = WikipediaTool()

# Testando a busca sobre um tópico
topic = "batata"  # Você pode mudar o tópico para testar outros temas

# Chamada direta ao método _run
resultado = tool._run(topic)

# Exibindo o resultado
print(f"Resultado da pesquisa sobre '{topic}':")
print(resultado)