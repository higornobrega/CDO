from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    apelido =models.CharField(max_length=100, null=True, blank=True)
    graduacao = models.CharField(max_length=100, null=True, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=3)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    def __str__(self):
        return self.nome + ' ( ' + self.apelido + ' )'