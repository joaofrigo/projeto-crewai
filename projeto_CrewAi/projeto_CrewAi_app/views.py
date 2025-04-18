from django.shortcuts import render
from django.http import HttpResponse
from crew.executar_crew import gerar_artigo_completo


def home_view(request):
    """
    View home do site, com a opção de receber o tema do artigo e depois processa-lo
    """

    if request.method == 'POST':
        topico = request.POST.get('topico')
        artigo = gerar_artigo_completo(topico)
        return render(request, 'artigo.html', {'artigo': artigo, 'topico': topico})
    return render(request, 'artigo.html')


