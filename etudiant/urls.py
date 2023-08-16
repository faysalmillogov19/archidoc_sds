from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name='list_etudiant'),
    path('form/<int:id>', views.form, name='form_etudiant'),
    path('search', views.search, name='search'),
    path('save/', views.save, name='save_etudiant'),
    path('set/<int:id>', views.set, name='set_etudiant'),
    path('details/<int:id>', views.details, name='details_etudiant'),
    path('found', views.found, name='found'),
]