from django.db import models
from Employé.models import Employé



# Create your models here.
class Salaire(models.Model):
    salaireBase = models.IntegerField(null=True)
    salaireBrut = models.IntegerField(null=True)
    salaireNet = models.FloatField(null=True)
    salaireNet1 = models.FloatField(null=True)
    aCompte = models.IntegerField(null=True)
    salaireCotisable = models.IntegerField(null=True)
    salaireTaxable = models.IntegerField(null=True)
    irpp = models.FloatField(null=True)
    cnps = models.FloatField(null=True)
    cac = models.FloatField(null=True)
    cfc = models.FloatField(null=True)
    crtv = models.FloatField(null=True)
    tc = models.FloatField(null=True)
    totalRetenus = models.FloatField(null=True)
    indemniteRepresentation = models.IntegerField(null=True)
    indemniteTransport = models.IntegerField(null=True)
    Employé = models.ForeignKey(Employé, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
