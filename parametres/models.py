from django.db import models


# Create your models here.
class Annee_academique(models.Model):
    libelle = models.TextField()
    debut = models.IntegerField()
    fin = models.IntegerField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)


class Session(models.Model):
    libelle = models.TextField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)


class Niveau(models.Model):
    libelle = models.TextField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)


class Filiere(models.Model):
    libelle = models.TextField()
    code = models.TextField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)


class Type_document(models.Model):
    libelle = models.TextField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)


class Examen(models.Model):
    libelle = models.TextField()
    description = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    updated = models.TimeField(auto_now=True, auto_now_add=False)
