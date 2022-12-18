from django.shortcuts import render, redirect
from my_site.models import *
from templates.forms import *

# Create your views here.
def base(request):
    return render(request, "base.html")

def voir_soldat(request):
    tous_les_soldats = Soldat.objects.all()
    contenu = {"soldats" : tous_les_soldats}
    return render(request, "voir_soldat.html", contenu)

def creer_soldat(request):
    if request.method == "POST":
        form = FormAjouterSoldat(request.POST)
        if form.is_valid():
            nouveau_soldat = Soldat()
            nouveau_soldat.nom = form.cleaned_data['nom']
            nouveau_soldat.grade = form.cleaned_data['grade']
            nouveau_soldat.specialite = form.cleaned_data['specialite']
            nouveau_soldat.save()
            return redirect('voir_soldat')
        else:
            print("Erreur, formulaire invalide")
    else:
        form = FormAjouterSoldat()
        contenu = {"formulaire" : form}
        return render(request, "creer_soldat.html", contenu)