from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('Salaire/<int:pk>/<int:it>/<int:ip>/<int:a>', views.Sal, name='sal'),
    path('Indemnites/<int:pk>', views.Indemnites, name='idem'),
    path('AfficheSalaires', views.Affiche_Salaire, name='Asals')

]
