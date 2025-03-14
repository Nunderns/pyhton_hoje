from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)  # Nome do contato
    telefone = models.CharField(max_length=20)  # Telefone
    email = models.EmailField(unique=True)  # Email único

    def __str__(self):
        return self.nome  # Exibir o nome ao imprimir o objeto
