from django.db import models
from parametres.models import Annee_academique, Session, Niveau, Filiere, Type_document, Examen

class Etudiant(models.Model):
	matricule=models.TextField()
	nom_complet=fichier=models.TextField()
	annee_academique=models.ForeignKey(Annee_academique, on_delete=models.CASCADE)
	filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)
	niveau=models.ForeignKey(Niveau, on_delete=models.CASCADE)
	type_document=models.ForeignKey(Type_document, on_delete=models.CASCADE)
	session=models.ForeignKey(Session, on_delete=models.CASCADE)
	examen=models.ForeignKey(Examen, on_delete=models.CASCADE)
	fichier=models.TextField()