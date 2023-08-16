from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name='list_archive'),
    path('form/<int:id>', views.form, name='form_archive'),
    path('search', views.search, name='search'),
    path('save/', views.save, name='save_archive'),
    path('set/<int:id>', views.set, name='set_archive'),
    path('details/<int:id>', views.details, name='details'),
    path('found', views.found, name='found'),
]