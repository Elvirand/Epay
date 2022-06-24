from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from .formModif import FormulaireEntrepriseM
from .models import Entreprise
from .formEntreprise import FormulaireEntreprise
from django.contrib.auth.models import User
from django.contrib import messages
from ProjetSalariApp import settings
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.urls import path


# Create your views here.

def Valid(request):
    return render(request, 'Entreprise/Validation.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        context = {'uidb64': uidb64, 'token': token}
        return redirect('valid')
    else:
        return render(request, 'activation_failed.html')


def Ok(request):
    return render(request, 'Entreprise/ok.html')


def Inscription(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(fname=fname):
        # messages.error(request, "Cette entreprise exite déjà, veillez reéssayez avec un autre nom d'entreprise'il vous plaît")
        # return redirect('Inscrit')

        if User.objects.filter(email=email):
            messages.error(request, "Cette Email exite déjà, veillez reéssayez avec un autre Email s'il vous plaît")
            return redirect('ok')

        if pass1 != pass2:
            messages.error(request, "Les deux mot de passe doivent être identique!")
            return redirect('ok')

        if not fname.isalnum():
            messages.error(request, "Le nom de l'entreprise doit comporter les caractères alpha-Numerique!")
            return redirect('ok')

        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit comporter les caractères alpha-Numerique!")
            return redirect('ok')

        myuser = User.objects.create_superuser(username, email, pass1)
        myuser.first_name = fname
        myuser.is_active = False
        myuser.save()

        messages.success(request,
                         "Votre compte a été crée avec succès. Un message de confirmation a été envoyé dans votre boite Email, veillez le confirmer pour activer votre compte")

        # Bienvynue Email

        subject = "Bienvenue dans Epay !!"
        message = "Salut !" + myuser.first_name + "!! \n" + "Merci pour avoir choisi notre l' application Epay pour la gestion de vos salaire \n Ceci est un message de confirmation, veillez le confirmer pour activer votre compte. \n\n\n Merci \n Epay  "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        uid = urlsafe_base64_encode(force_bytes(myuser.pk))
        print(uid)

        token = generate_token.make_token(myuser)
        print(token)

        current_site = get_current_site(request)
        email_subject = "confirmer son adresse mail"
        message2 = render_to_string("Entreprise/email_confirmation.html", {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, 'Entreprise/Inscription.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if pass1 != pass2:
            messages.error(request, "Erreur de mot de passe!")
            return redirect('login')

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "Dashbord/Dashbord.html", {'fname': fname})
        else:
            messages.error(request, "Erreur de connexion, veillez entrer les informations correctes")
            return redirect('login')

    return render(request, "Entreprise/Login.html")


@login_required
def AjoutEntrepise(request):
    monformEntreprise = FormulaireEntreprise()
    if request.method == 'POST':
        monformEntreprise = FormulaireEntreprise(request.POST)
        print(1)
        if monformEntreprise.is_valid():
            print(2)
            user = request.user
            nomEntreprise = user.first_name
            # nomEntreprise = monformEntreprise.cleaned_data.get('fname')
            activite = monformEntreprise.cleaned_data.get('activite')
            adresse = monformEntreprise.cleaned_data.get('adresse')
            anneeCreation = monformEntreprise.cleaned_data.get('anneeCreation')
            effectif = monformEntreprise.cleaned_data.get('effectif')
            capital = monformEntreprise.cleaned_data.get('capital')
            chiffreAffaire = monformEntreprise.cleaned_data.get('chiffreAffaire')
            nomDirecteur = monformEntreprise.cleaned_data.get('nomDirecteur')
            numeroContribuable = monformEntreprise.cleaned_data.get('numeroContribuable')
            formeJuridique = monformEntreprise.cleaned_data.get('formeJuridique')

            Entreprisef = Entreprise(nomEntreprise=nomEntreprise, activite=activite, adresse=adresse,
                                     anneeCreation=anneeCreation,
                                     effectif=effectif, capital=capital, chiffreAffaire=chiffreAffaire,
                                     nomDirecteur=nomDirecteur,
                                     numeroContribuable=numeroContribuable, formeJuridique=formeJuridique)
            print(3)
            Entreprisef.save()
            print(4)
            return redirect('Entre')
        print(5)
    context = {'monformEntreprise': monformEntreprise, }
    return render(request, 'Entreprise/AjoutEntre.html', context)


@login_required
def modifientreprise(request, entreprise_id):
    entreprise = get_object_or_404(Entreprise, id=entreprise_id)
    dic = {'nomEntreprise': entreprise.nomEntreprise,
           'adresse': entreprise.adresse,
           'anneeCreation': entreprise.anneeCreation,
           'activite': entreprise.activite,
           'effectif': entreprise.effectif,
           'capital': entreprise.capital,
           'nomDirecteur': entreprise.nomDirecteur,
           'numeroContribuable': entreprise.numeroContribuable,
           'formeJuridique': entreprise.formeJuridique,
           'chiffreAffaire': entreprise.chiffreAffaire}

    form_em = FormulaireEntrepriseM(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEntrepriseM(request.POST, instance=entreprise)
        if form_em.is_valid():
            form_em.save()
            return redirect('entreprise')
    if request.method == 'GET':
        form_em = FormulaireEntrepriseM(data=dic)
    return render(request, 'Entreprise/modifEntreprise.html', {'modifientreprise': form_em})


@login_required
def Entreprisek(request):
    try:
        entreprises = Entreprise.objects.all()
        for element in entreprises:
            print(element.nomEntreprise)
    except:
        a = False
    else:
        a = True
    context = {'cle': entreprises}
    return render(request, 'Entreprise/Entreprise.html', context)


@login_required
def Info_Entreprise(request):
    Entreprises = Entreprise.objects.all()
    context = {'Entreprises': Entreprises}
    return render(request, 'Entreprise/InfoEntreprise.html', context)


@login_required
def AfficheNomEntreprise(request):
    entreprise = Entreprise.object.all()
    context = {'entreprise': entreprise}
    return render(request, 'Dashbord/Dashbord.html', context)


# ================================================EXTRA=====================================================


@login_required  # ||
def Parametre(request):  # ||
    return render(request, 'Parametre.html')  # ||


@login_required  # ||
def Apropos(request):  # ||
    return render(request, 'Apropos.html')  # ||


@login_required  # ||
def Contact(request):  # ||
    return render(request, 'Contact.html')  # ||


@login_required  # ||
def Aide(request):  # ||
    return render(request, 'Aide.html')  # ||
    # ||


# =========================================================================================================


# =====================================================DECONEXION==========================================
def Finish(request):  # ||
    logout(request)  # ||
    return redirect('login')  # ||
# ==========================================================================================================
