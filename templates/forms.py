from django.forms import ModelForm
from my_site.models import *

class FormAjouterSoldat(ModelForm):
    class Meta:
        model = Soldat
        fields = ['nom', 'grade', 'specialite']
        labels = {
            'nom' : 'nom',
            'grade' : 'grade',
            'specialite' : 'specialite'
        }
