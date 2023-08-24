from django.db import models


class Document(models.Model):
    annee_academique = models.ForeignKey(
        "parametres.Annee_academique", on_delete=models.CASCADE
    )
    filiere = models.ForeignKey("parametres.Filiere", on_delete=models.CASCADE)
    niveau = models.ForeignKey("parametres.Niveau", on_delete=models.CASCADE)
    type_document = models.ForeignKey(
        "parametres.Type_document", on_delete=models.CASCADE
    )
    session1 = models.ForeignKey(
        "parametres.Session", related_name="session1", on_delete=models.CASCADE
    )
    session2 = models.ForeignKey(
        "parametres.Session", related_name="session2", on_delete=models.CASCADE
    )
    examen = models.ForeignKey("parametres.Examen", on_delete=models.CASCADE)
    fichier = models.TextField()
