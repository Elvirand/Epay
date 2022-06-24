from django import forms
from django.contrib.auth.forms import PasswordResetForm

from .models import Entreprise

class forgotPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-user'}))