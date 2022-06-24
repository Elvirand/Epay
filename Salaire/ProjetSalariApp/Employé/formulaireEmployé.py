from django import forms

from Employé.models import Employé


class FormulaireEmployé(forms.ModelForm):
    class Meta:
        model = Employé
        fields = '__all__'


class RecupereSalaireBase(forms.ModelForm):
    class Meta:
        model = Employé
        fields = ('salaireBase',)