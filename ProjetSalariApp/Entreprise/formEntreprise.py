#from django.forms import ModelForm
from django import forms

from .models import Entreprise


#class FormulaireEntreprise1(forms.Form):
    #nomEntreprise = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Entrer le nom de l"entreprise', 'cols': 40, 'rows': 20}))
    #activite = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Entrer l'activité"}))
    #adresse = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Entrer l'adresse"}))
   # anneeCreation = forms.DateField(widget=forms.TextInput(attrs={'placeholder': "Entrer l'année de création"}))
   # effectif = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "Entrer l'effectif"}))
    #capital = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': "Entrer le capital"}))
   # nomDirecteur = forms.CharField( widget=forms.TextInput(attrs={'placeholder': "Entrer le nom du directeur"}))
    #chiffreAffaire = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': "Entrer le chiffre d'affaire"}))
    #numeroContribuable = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "Entrer le numero de contribuable"}))
   # FORMEJURIDIQUE = (('SCS', 'SCS'),
                     # ('SNC', 'SNC'),
                     # ('SARL', 'SARL'),
                      #('SA', 'SA'),
                     # ('SAS', 'SAS'),
                    #  ('GIE', 'GIE'),
                    #  ('SEP', 'SEP'),
                    #  ('SCP', 'SCP'),
                    #  ('SCI', 'SCI'),
                    #  ('SP', 'SP'))
   # formeJuridique = forms.ChoiceField(choices=FORMEJURIDIQUE)


class FormulaireEntreprise(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['activite','adresse','anneeCreation','effectif','capital','nomDirecteur','chiffreAffaire','numeroContribuable','formeJuridique']
