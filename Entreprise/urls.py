from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.Login, name='login'),
    path('valid', views.Valid, name='valid'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('ok', views.Valid, name='ok'),
    path('Entre', views.Entreprisek, name='Entre'),
    path('Ajout', views.AjoutEntrepise, name='Ajout'),
    path('modifier/<int:entreprise_id>', views.modifientreprise, name='modifientreprise'),
    path('Info', views.Info_Entreprise, name='entreprise'),
    path('nom', views.AfficheNomEntreprise, name='nom'),
    path('Inscrit', views.Inscription, name='inscrit'),
    path('Finish', views.Finish, name='Finish'),
    path('Para', views.Parametre),
    path('Cont', views.Contact),
    path('Apro', views.Apropos),
    path('Aide', views.Aide)


]
