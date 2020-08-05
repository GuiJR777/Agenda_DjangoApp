from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo= models.CharField(max_length=100)
    descricao= models.TextField(blank=True, null=True)
    data_evento= models.DateTimeField()
    data_criacao= models.DateTimeField(auto_now=True)
    local= models.CharField(max_length=250, blank=True, null=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table= 'evento'

    def __str__(self):
        return self.titulo 

    def converte_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %Hh%M')