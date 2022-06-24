from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Entreprise.urls')),
    path('dash', include('Dashbord.urls')),
    path('entreprise', include('Entreprise.urls')),
    path('employé', include('Employé.urls')),
    path('AfficheSalaires', include('Salaire.urls')),
    path('Parametre', include('Entreprise.urls')),
    path('Contact', include('Entreprise.urls')),
    path('Apropos', include('Entreprise.urls')),
    path('Aide', include('Entreprise.urls')),
    path('deco', include('Entreprise.urls'))

]