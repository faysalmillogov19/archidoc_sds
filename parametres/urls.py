from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list_annee_academique/', views.list_annee_academique, name='list_annee_academique'),
    path('annee_academique_form/<int:id>', views.annee_academiqueForm, name='annee_academique_form'),
    path('set_annee_academique/<int:id>', views.set_annee_academique, name='set_annee_academique'),

    path('list_filiere/', views.list_filiere, name='list_filiere'),
    path('filiere_form/<int:id>', views.filiere_form, name='filiere_form'),
    path('set_filiere/<int:id>', views.set_filiere, name='set_filiere'),

    path('list_session/', views.list_session, name='list_session'),
    path('session_form/<int:id>', views.session_form, name='session_form'),
    path('set_session/<int:id>', views.set_session, name='set_session'),

    path('list_niveau/', views.list_niveau, name='list_niveau'),
    path('niveau_form/<int:id>', views.niveau_form, name='niveau_form'),
    path('set_niveau/<int:id>', views.set_niveau, name='set_niveau'),

    path('list_type/', views.list_type, name='list_type'),
    path('type_form/<int:id>', views.type_form, name='type_form'),
    path('set_type/<int:id>', views.set_type, name='set_type'),

    path('list_examen/', views.list_examen, name='list_examen'),
    path('examen_form/<int:id>', views.examen_form, name='examen_form'),
    path('set_examen/<int:id>', views.set_examen, name='set_examen'),
]
