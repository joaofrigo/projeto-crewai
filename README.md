# Gerador de Artigos com CrewAI

Site com objetivo de criar artigos com tópicos específicos utilizando integração com CrewAi, Django e com deploy no plano free do Koyeb.

**Link para acesso ao site:**  
https://significant-roadrunner-sou-aluno-415f8e70.koyeb.app  
*(O site é extremamente instável considerando o uso excessivo de memória para um plano free)*

> Não tem nenhuma necessidade de qualquer coisa além de colocar um tópico e esperar as IAs gerarem respostas de acordo com o tópico.

![Demonstração do site](./Gif_site.gif)

## Tecnologias utilizadas

- HTML  
- JavaScript  
- Django  
- CSS  
- Python  
- VS Code (com extensões para facilitar o trabalho)  
- Uso de `.env` para as variáveis de ambiente  
- Uso de `Procfile`  
- Gunicorn (pro ambiente de produção do Koyeb, que é Linux, mesmo que eu esteja fazendo código no Windows)  
- Agentes LLM usando o modelo `"groq/llama3-70b-8192"`  
- API da Wikipedia  
- Koyeb  
- CrewAI  
- CrewAI Tools  

## Como rodar localmente

Se precisar desse código, só precisa rodar o seguinte comando na pasta raiz (rodar localmente):

```bash
python manage.py runserver
```
Mas se quiser rodar ele em um servidor, provavalmente só ira precisar ajustar o runtime e o Procfile.
