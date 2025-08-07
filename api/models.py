from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nasc = models.DateField(null=True, blank=True)
    nascion = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True) # TextField não tem tamanho definito

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

