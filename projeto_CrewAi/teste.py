"""
import os
from litellm import completion
from dotenv import load_dotenv
load_dotenv()

response = completion(
    model="groq/llama3-70b-8192",  # escolhido por que é um modelo aberto e prático.
    messages=[{"role": "user", "content": "Explique quantum computing em 1 frase"}],
    api_key=os.getenv("GROQ_API_KEY")  # Chave gratuita: https://console.groq.com
)

print(response.choices[0].message.content)
"""

from crewai_tools import RagTool
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# A chave da API agora pode ser acessada diretamente
api_key = os.getenv("OPENAI_API_KEY")

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

# Instanciando a ferramenta
tool = WikipediaTool()

# Testando a busca sobre um tópico
topic = "doce"  # Você pode mudar o tópico para testar outros temas

# Chamada direta ao método _run
resultado = tool._run(topic)

# Exibindo o resultado
print(f"Resultado da pesquisa sobre '{topic}':")
print(resultado)
