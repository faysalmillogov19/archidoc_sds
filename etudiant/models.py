from django.db import models


class Etudiant(models.Model):
    matricule = models.TextField()
    nom_complet = fichier = models.TextField()
    annee_academique = models.ForeignKey(
        "parametres.Annee_academique", on_delete=models.CASCADE
    )
    filiere = models.ForeignKey("parametres.Filiere", on_delete=models.CASCADE)
    niveau = models.ForeignKey("parametres.Niveau", on_delete=models.CASCADE)
    type_document = models.ForeignKey(
        "parametres.Type_document", on_delete=models.CASCADE
    )
    session = models.ForeignKey("parametres.Session", on_delete=models.CASCADE)
    examen = models.ForeignKey("parametres.Examen", on_delete=models.CASCADE)
    fichier = models.TextField()
