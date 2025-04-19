Site com objetivo de criar artigos com tópicos específicos utilizando integração com CrewAi, Django e com deploy no plano free do Koyeb

Link para acesso ao site: https://significant-roadrunner-sou-aluno-415f8e70.koyeb.app
(O site é extremamente instável considerando o uso excessivo de memória para um plano free)

Não tem nenhuma necessidade de qualquer coisa além de colocar um tópico e esperar as IAS gerarem respostas de acordo com o tópico.

![Demonstração do site](./Gif_site.gif)

Tecnologias utilizadas:
HTML
JavaScript
Django
CSS
Python
VS code (com extensões para facilitar o trabalho)
Uso de .env para as variáveis de ambiente
Uso de Procfile
Gunicorn (pro ambiente de produção do Koyeb, que é linux, mesmo que eu esteja fazendo código no windows)
Agentes llm usando o modelo "groq/llama3-70b-8192"
API da wikipedia
Koyeb
CrewAI
CrewAI tools

Se precisar desse código, só precisa rodar "Python manage.py runserver" na pasta raiz, para ter o código localmente.
Se quiser desse código não localmente e não for diretamente utilizando o Koyeb para hostea-lo, acredito que precisará fazer mais mudanças, provavelmente só no Procfile porém.
