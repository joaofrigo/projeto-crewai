from django.shortcuts import render
from django.http import HttpResponse
from crew.executar_crew import gerar_artigo_completo


def home_view(request):
    if request.method == 'POST':
        topico = request.POST.get('topico')
        artigo = gerar_artigo_completo(topico)
        return render(request, 'artigo.html', {'artigo': artigo, 'topico': topico})
    return render(request, 'artigo.html')

def exemplo_view(request):
    return HttpResponse("Essa é a view de exemplo") # retorna uma resposta em html

#def gerar_artigo_view(request):
    if request.method == 'POST':
        topico = request.POST.get('topico')
        artigo = gerar_artigo_completo(topico)
        return render(request, 'artigo.html', {'artigo': artigo, 'topico': topico})
    return render(request, 'artigo.html')
