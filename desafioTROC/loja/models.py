from django.db import models


class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class CupomFixo(models.Model):
    desconto_fixo = models.DecimalField(max_digits=6, decimal_places=2)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class CupomPercentual(models.Model):
    desconto_percentual = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
