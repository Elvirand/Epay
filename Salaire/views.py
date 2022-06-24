from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.http import request
#from Entreprise.models import Entreprise
# Create your views here.
from Employé.models import Employé
from Salaire.models import Salaire
from Employé.formulaireEmployé import RecupereSalaireBase
from Salaire.formulaireSalaire import RecupereIndemnites


def Sal(request, pk, it, ip, a):
    employe = Employé.objects.get(id=pk)
    nomEmploye = employe.nomEmploye
    salaireBase = employe.salaireBase
    salaireBrut = salaireBase +it + ip
    salaireCotisable = salaireBrut - (it + ip)
    salaireTaxable = salaireBrut - ip
    cnps = salaireCotisable * 0.042
    irpp = (salaireTaxable * 0.7 - cnps - 41667) * 0.1
    cac = irpp * 0.1
    cfcSalarial = salaireTaxable * 0.01
    if salaireBase >= 0 and salaireBase <= 50000:
        crtv = 0
    elif salaireBase > 50000 and salaireBase <= 100000:
        crtv = 750
    elif salaireBase > 100000 and salaireBase <= 200000:
        crtv = 1650
    elif salaireBase > 200000 and salaireBase <= 300000:
        crtv = 3250
    elif salaireBase > 300000 and salaireBase <= 400000:
        crtv = 4550
    elif salaireBase > 400000 and salaireBase <= 500000:
        crtv = 5850
    elif salaireBase > 500000 and salaireBase <= 600000:
        crtv = 7150
    elif salaireBase > 600000 and salaireBase <= 700000:
        crtv = 8450
    elif salaireBase > 700000 and salaireBase <= 800000:
        crtv = 9750
    elif salaireBase > 800000 and salaireBase <= 900000:
        crtv = 11050
    elif salaireBase > 900000 and salaireBase <= 1000000:
        crtv = 12350
    else:
        crtv = 13000

    if salaireBrut >= 62000 and salaireBrut <= 75000:
        tc = 250
    elif salaireBrut > 75000 and salaireBrut <= 100000:
        tc = 500
    elif salaireBrut > 100000 and salaireBrut <= 125000:
        tc = 750
    elif salaireBrut > 125000 and salaireBrut <= 150000:
        tc = 1000
    elif salaireBrut > 150000 and salaireBrut <= 200000:
        tc = 1250
    elif salaireBrut > 200000 and salaireBrut <= 250000:
        tc = 1500
    elif salaireBrut > 250000 and salaireBrut <= 300000:
        tc = 1750
    elif salaireBrut > 300000 and salaireBrut <= 500000:
        tc = 2500
    else:
        tc = 3000

    totalRetenus = cfcSalarial + irpp + cnps + cac + crtv + tc
    salaireNet1 = salaireBrut - totalRetenus
    salaireNet = salaireNet1 - a
    monSalaire = Salaire(Employé=employe, salaireBase=salaireBase, salaireBrut=salaireBrut, salaireCotisable=salaireCotisable, salaireTaxable=salaireTaxable, cnps=cnps, irpp=irpp, cac=cac, cfc=cfcSalarial, crtv=crtv, tc=tc, totalRetenus=totalRetenus, salaireNet1=salaireNet1, salaireNet=salaireNet, indemniteTransport=it, indemniteRepresentation=ip, aCompte = a)
    monSalaire.save()
    context = {'employe':employe, 'nomEmploye':nomEmploye, 'salaireBase': salaireBase, 'salaireBrut':salaireBrut, 'indTransport':it, 'indRepresentation':ip, 'salaireCotisable':salaireCotisable, 'salaireTaxable':salaireTaxable, 'cnps':cnps, 'irpp':irpp, 'cac':cac, 'cfcSalarial':cfcSalarial, 'crtv':crtv, 'tc':tc, 'totalRetenus':totalRetenus, 'salaireNet1':salaireNet1, 'salaireNet':salaireNet}
    return render(request, 'Salaire/Salaire.html', context)

def Indemnites(request, pk):
    monformindemnites = RecupereIndemnites()
    if request.method == 'POST':
        monformindemnites = RecupereIndemnites(request.POST)
        if monformindemnites.is_valid():
            monformindemnites.save()
            it = monformindemnites.cleaned_data.get('indemniteTransport')
            ip = monformindemnites.cleaned_data.get('indemniteRepresentation')
            a = monformindemnites.cleaned_data.get('aCompte')
            return redirect('sal', pk, it, ip, a)
        print(1)
    context = {'monformindemnites': monformindemnites, 'pk':pk}
    return render(request, 'Salaire/CalulSala.html', context)


def Affiche_Salaire(request):
    salaires = Salaire.objects.all()
    context2 = {'salaires': salaires}
    return render(request, 'Salaire/salaires.html', context2)
