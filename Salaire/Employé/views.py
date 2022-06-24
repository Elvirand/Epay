from django.shortcuts import render, redirect, get_object_or_404
#from Entreprise.models import Entreprise
from Employé.formulaireEmployé import FormulaireEmployé
from Employé.models import Employé
#from Salaire.models import Salaire


def Liste_Employe(request):
    Employes = Employé.objects.all()
    context2 = {'Employes': Employes}
    #print(Salaire.CalculeSalaireBrut.fget(SalaireBrut))
    return render(request, 'Employé/Employé.html', context2)


def Ajoute_Employe(request):

    monformEmploye = FormulaireEmployé()
    print(4)
    if request.method == 'POST':
        monformEmploye = FormulaireEmployé(request.POST)
        print(3)
        if monformEmploye.is_valid():
            print(2)
            monformEmploye.save()
            return redirect('InfoE')
        print(1)
    context = {'monformEmploye': monformEmploye}
    return render(request, 'Employé/Ajouter.html', context)


def modifiemploye(request, employe_id):
    employe = get_object_or_404(Employé, pk=employe_id)
    dic = {'nomEmploye': employe.nomEmploye,
           'prenomEmploye': employe.prenomEmploye,
           'dateNaissance': employe.dateNaissance,
           'lieuNaissance': employe.lieuNaissance,
           'sexe': employe.sexe,
           'nationalite': employe.nationalite,
           'statusMatrimonial': 'Marié(e)',
           'fonction': employe.fonction,
           'typeContrat': employe.typeContrat,
           'dateRecrutement': employe.dateRecrutement,
           'dateFin': employe.dateFin,
           'salaireBase': employe.salaireBase,
           'salaireNet': employe.salaireNet}

    form_em = FormulaireEmployé(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEmployé(request.POST, instance=employe)
        if form_em.is_valid():
            form_em.save()
            return redirect('InfoE')
    if request.method =='GET':
        form_em = FormulaireEmployé(data=dic)
    return render(request, 'Employé/modifiemploye.html', {'modifiemploye': form_em})


def Supprime_Employe(request, employe_id):
    supprimeur = Employé.objects.get(id=employe_id)
    supprimeur.delete()
    return redirect('InfoE')

def Salaire_Employe(request, employe_id):
    salaire = Employé.objects.get(id=employe_id)
    salaire.delete()
    return redirect('InfoE')


def Menu(request):

    return render(request, 'Employé/MenuEmploye.html')
