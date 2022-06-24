from django import forms

from .models import Salaire


class RecupereIndemnites(forms.ModelForm):
    class Meta:
        model = Salaire
        fields = ['indemniteTransport', 'indemniteRepresentation', 'aCompte']


class FormulaireSalaires(forms.ModelForm):
    class Meta:
        model = Salaire
        fields = '__all__'