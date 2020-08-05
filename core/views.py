#Nosso código Python vai aqui

from django.shortcuts import render, HttpResponse
from core.models import Evento


# Create your views here.
def agenda(request):
    evento= Evento.objects.all
    dados= {'eventos':evento}
    return render(request, 'agenda.html', dados)