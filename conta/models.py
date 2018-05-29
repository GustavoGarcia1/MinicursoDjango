from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Conta(models.Model):
    ag = models.IntegerField()
    conta = models.IntegerField()
    digito = models.IntegerField(MinValueValidator(MinValueValidator(0), MaxValueValidator(9)))
    saldo = models.DecimalField(max_digits=7, decimal_places=2)

class Titulo(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=50)
    data = models.DateField()
    observacao = models.TextField(null=True, blank=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)


class Titulo_Pagar(Titulo):
    data_vencimento = models.DateField()
    quitado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Titulos A Pagar"

class Titulo_Receber(Titulo):
    data_receber = models.DateField()
    recebido = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Titulos A Receber"
