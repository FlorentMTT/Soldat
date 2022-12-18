from django.db import models

# Create your models here.

class Soldat(models.Model):
    nom = models.CharField(max_length=32, null=False)
    grade = models.DecimalField(max_digits=1, decimal_places=0, null=False)
    specialite = models.CharField(max_length=32, null=True)

#class Equipement(models.Model):
#    nom = models.CharField(max_length=32, null=False)
#    niveau = models.DecimalField(max_digits=1, decimal_places=0, null=False)
#
#class Arme(models.Model):
#    nom = models.CharField(max_length=32, null=False)
#    niveau = models.DecimalField(max_digits=1, decimal_places=0, null=False)
#    nbMunition = models.DecimalField(max_digits=2, decimal_places=0, null=False)
#
#    soldat = models.ForeignKey(Soldat, on_delete=models.CASCADE, null = False)
#
#class Possede(models.Model):
#    soldat = models.ForeignKey(Soldat, on_delete=models.CASCADE, null=False)
#    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, null=False)

