from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Entreprise.urls')),
    path('dash', include('Dashbord.urls')),
    path('entreprise', include('Entreprise.urls')),
    path('entreprise', include('Entreprise.urls')),
    path('employé', include('Employé.urls')),
    path('AfficheSalaires', include('Salaire.urls')),
    path('Parametre', include('Entreprise.urls')),
    path('Contact', include('Entreprise.urls')),
    path('monpass', include('Entreprise.urls')),
    path('Apropos', include('Entreprise.urls')),
    path('Aide', include('Entreprise.urls')),
    path('deco', include('Entreprise.urls')),

    path('reset_password', views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]