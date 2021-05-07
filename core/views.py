from django.shortcuts import render, HttpResponse
from core.models import Evento

def lista_eventos (request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'evento': evento}
    print(evento)
    return render (request, 'agenda.html', dados )

