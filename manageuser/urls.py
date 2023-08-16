from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	path('list', views.list, name="list_user"),
    path('set_profil/<int:id>', views.set_profil_form, name="set_profil"),
    path('save_profil/<int:id>', views.save_profil, name="save_profil"),
    path('delete/<int:id>', views.delete, name="delete_user"),
    re_path(r'^add', views.create, name="add_user"),
    #re_path(r'^logout', views.deconnexion, name="log_out"),
]