from django.db import models

# Create your models here.

class Entreprise(models.Model):
    FORMEJURIDIQUE = (('SCS','SCS'),
                      ('SNC','SNC'),
                      ('SARL', 'SARL'),
                      ('SA','SA'),
                      ('SAS', 'SAS'),
                      ('GIE', 'GIE'),
                      ('SEP', 'SEP'),
                      ('SCP', 'SCP'),
                      ('SCI', 'SCI'),
                      ('SP','SP'))
    nomEntreprise = models.CharField(default='Entreprise', max_length=50, null=True, blank=True)
    adresse = models.CharField(default='Entreprise@gmail.com', max_length=50, null=True, blank=True)
    #MDP = models.CharField(max_length=100, null=True)
    #ConfirmMDP = models.CharField(max_length=100, null=True)
    anneeCreation = models.IntegerField(default=2000, null=True, blank=True)
    activite = models.CharField(default='Activité', max_length=100, null=True, blank=True)
    effectif = models.IntegerField(default=1, null=True, blank=True)
    capital = models.IntegerField(default=10000, null=True, blank=True)
    nomDirecteur = models.CharField(default='Directeur', max_length=50, null=True, blank=True)
    numeroContribuable = models.IntegerField(default=1, null=True, blank=True)
    formeJuridique = models.CharField(default='SP', max_length=50, null=True, choices=FORMEJURIDIQUE, blank=True)
    chiffreAffaire =models.IntegerField(default=10000, null=True, blank=True)


    def __str__(self):
        return self.nomEntreprise