from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('Info', views.Liste_Employe, name='InfoE'),
    path('Ajout', views.Ajoute_Employe),
    path('<int:employe_id>', views.Supprime_Employe, name='supp'),
    path('modifier/<int:employe_id>', views.modifiemploye, name='modifiemploye'),
    path('Menu', views.Menu)

]
