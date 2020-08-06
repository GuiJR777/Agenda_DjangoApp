#Nosso código Python vai aqui

from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Essa são as funções que renderizam as telas, tambem tratam dados e autenticam
def home(request):
    return render(request, 'home.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username= request.POST.get('username')
        password= request.POST.get('userpassword')
        usuario= authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect ('/agenda/')
        else:
            messages.error(request, 'Usuário ou senha Inválidos')
        
    return redirect('/login/')

@login_required(login_url='/login/')
def agenda(request):
    usuario= request.user
    evento= Evento.objects.filter(usuario=usuario)
    dados= {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def new_event(request):
    return render(request, 'new_event.html')

@login_required(login_url='/login/')
def submit_new_event(request):
    if request.POST:
        titulo= request.POST.get('titulo')
        data_evento= request.POST.get('data')
        descricao= request.POST.get('descricao')
        local= request.POST.get('local')
        usuario= request.user
        Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario, local=local)
    
    return redirect('/agenda/')