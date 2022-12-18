from django.shortcuts import render
from my_site.models import *

# Create your views here.
def base(request):
    return render(request, "base.html")

def voir_soldat(request):
    tous_les_soldats = Soldat.objects.all()
    contenu = {"soldats" : tous_les_soldats}
    return render(request, "voir_soldat.html", contenu)