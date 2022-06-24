from django.db import models
#from Salaire.models import Salaire

# Create your models here.
class Employé(models.Model):
    NATIONALITE = (('Allemande','Allemande'),
                   ('Algérien','Algérien'),
                   ('Angolais','Angolais'),
                   ('Argentin','Argentin'),
                   ('Américaine','Américaine'),
                   ('Anglaise','Anglaise'),
                   ('Australien','Australien'),
                   ('Autrichien','Autrichien'),
                   ('Bahamien','Bahamien'),
                   ('Belge','Belge'),
                   ('Béninois','Béninois'),
                   ('Bisseau-Guinéen','Bisseau-Guinéen'),
                   ('Brésilien','Brésilien'),
                   ('Burkinabé','Burkinabé'),
                   ('Burundi','Burundi'),
                   ('Camerounaise','Camerounaise'),
                   ('Canadienne','Canadienne'),
                   ('cap-verdien','cap-verdien'),
                   ('Chilien','Chilien'),
                   ('Chinois','Chinois'),
                   ('Colombien','Colombien'),
                   ('Congolais', 'Congolais'),
                   ('Corée du sud', 'Corée du sud'),
                   ('Coréen','Coréen'),
                   ('Cubain','Cubain'),
                   ('Danois', 'Danois'),
                   ('Egyptien','Egyptien'),
                   ('Equatorien','Equatorien'),
                   ('Espagnole','Espagnole'),
                   ('Estonien','Estonien'),
                   ('Etyiopien','Etyiopien'),
                   ('Finlandais','Finlandais'),
                   ('Française', 'Française'),
                   ('Gabonais','Gabonais'),
                   ('gambien','gambien'),
                   ('ghanéen','ghanéen'),
                   ('Grec','Grec'),
                   ('Guinéenne','Guinéenne'),
                   ('Haïtien','Haïtien'),
                   ('Hongrois','Hongrois'),
                   ('Indien','Indien'),
                   ('Indonésien','Indonésien'),
                   ('Irlandais', 'Irlandais'),
                   ('Islandais','Islandais'),
                   ('Israélien','Israélien'),
                   ('Italien','Italien'),
                   ('Ivoirien','Ivoirien'),
                   ('Jamaïquain','Jamaïquain'),
                   ('Japonais','Japonais'),
                   ('Jordanien','Jordanien'),
                   ('Kényen','Kényen'),
                   ('Libye','Libye'),
                   ('Marocain','Marocain'),
                   ('Mexicain','Mexicain'),
                   ('Motswanan','Motswanan'),
                   ('Mozambique','Mozambique'),
                   ('Namibie','Namibie'),
                   ('Nigeria','Nigeria'),
                   ('Nigérien','Nigérien'),
                   ('Norvégien','Norvégien'),
                   ('Pakistanais','Pakistanais'),
                   ('Palestinien','Palestinien'),
                   ('Péruvien','Péruvien'),
                   ('Philippin','Philippin'),
                   ('Polonais','Polonais'),
                   ('Portugais','Portugais'),
                   ('Québécois','Québécois'),
                   ('Roumain','Roumain'),
                   ('Russe','Russe'),
                   ('Sénégalais','Sénégalais'),
                   ('Suédois','Suédois'),
                   ('Tchadien','Tchadien'),
                   ('Tchèque','Tchèque'),
                   ('Tunisienne','Tunisienne'),
                   ('Vietnamienne','Vietnamienne'),
                   ('Zambien','Zambien'),
                   ('Zimbabwéen','Zimbabwéen'))
    STATUSMATRIMONIAL = (('Marié(e)', 'Marié(e)'),
                      ('Célibataire', 'Célibataire'),
                      ('Divorsé(e)', 'Divorsé(e)'))
    TYPECONTRAT = (('Durée déterminée', 'Durée déterminée'),
                         ('Durée indéterminée', 'Durée indéterminée'))
    SEXE = (('Maxculin','Maxculin'),
            ('Féminin','Féminin'))

    nomEmploye = models.CharField(max_length=50, null=True)
    prenomEmploye = models.CharField(max_length=50, null=True)
    dateNaissance = models.DateField(null=True)
    lieuNaissance = models.CharField(max_length=50, null=True)
    nationalite = models.CharField(max_length=50, null=True, choices=NATIONALITE)
    statusMatrimonial = models.CharField(max_length=50, null=True, choices=STATUSMATRIMONIAL)
    fonction = models.CharField(max_length=50, null=True)
    typeContrat = models.CharField(max_length=50, null=True, choices=TYPECONTRAT)
    dateRecrutement = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    salaireBase = models.IntegerField(null=True)
    salaireNet = models.IntegerField(null=True)
    #Salaire = models.ManyToOneRel(Salaire, to=salaireBase,field_name='salaireBase')
    sexe = models.CharField(max_length=10, null=True, choices=SEXE)

    def __str__(self):
        return self.nomEmploye





