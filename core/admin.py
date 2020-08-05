#Arquivo de Administração

from django.contrib import admin
from core.models import Evento

# Mudando a visualização da tela de Admin
class EventoAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'data_evento', 'data_criacao')
    list_filter= ('usuario',)

# Registrando meu modelo de banco de dados
admin.site.register(Evento, EventoAdmin)
