from django.shortcuts import render
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
    form = FormAjouterSoldat()
    contenu = {"formulaire" : form}
    return render(request, "creer_soldat.html", contenu)