from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from datetime import datetime, timedelta
import os
from .models import Etudiant
from parametres.models import Annee_academique, Filiere, Niveau, Session, Type_document, Examen
import pandas as pd
import openpyxl
import tabula
from pdfquery import PDFQuery
import PyPDF2
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
	data = Etudiant.objects.all()
	return render(request,'Etudiant/index.html',{'data':data})
@login_required
def form(request, id):
	data=0
	annees=Annee_academique.objects.all()
	filieres=Filiere.objects.all()
	niveaux=Niveau.objects.all()
	sessions=Session.objects.all()
	examens=Examen.objects.all()
	type_documents=Type_document.objects.all()
	if id>0:
		data=Etudiant.objects.get(id=id)

	return render(request,'Etudiant/form.html', {'data':data, 'annees':annees, 'filieres':filieres, 'niveaux':niveaux, 'sessions':sessions, 'type_documents':type_documents,'examens':examens})

@login_required
def search(request):

	annees=Annee_academique.objects.all()
	filieres=Filiere.objects.all()
	niveaux=Niveau.objects.all()
	sessions=Session.objects.all()
	Type_documents=Type_document.objects.all()
	

	return render(request,'Etudiant/search.html', {'annees':annees, 'filieres':filieres, 'niveaux':niveaux, 'sessions':sessions, 'Type_documents':Type_documents})


@login_required
def save(request):
	doc=Etudiant()
	doc.matricule=request.POST.get('matricule')
	doc.nom_complet=request.POST.get('nom_complet')
	doc.niveau= Niveau.objects.get(id=int(request.POST.get('niveau'))) 
	doc.session=Session.objects.get(id=int(request.POST.get('session')))
	doc.filiere=Filiere.objects.get(id=int(request.POST.get('filiere')))
	doc.examen=Examen.objects.get(id=int(request.POST.get('examen')))
	doc.type_document=Type_document.objects.get(id=int(request.POST.get('type_document')))
	doc.annee_academique=Annee_academique.objects.get(id=int(request.POST.get('annee_academique')))

	if request.FILES.get("fichier"):
		file_input=request.FILES.get("fichier")
		doc.fichier=uploadFile(file_input, "archives/", '.pdf')

	doc.save()

	data= Etudiant.objects.all()

	return redirect('list_etudiant')

@login_required
def set(request, id):

	doc=Etudiant.objects.get(id=id)
	if request.method=="POST":
		doc.matricule=request.POST.get('matricule')
		doc.nom_complet=request.POST.get('nom_complet')
		doc.niveau= Niveau.objects.get(id=int(request.POST.get('niveau'))) 
		doc.session=Session.objects.get(id=int(request.POST.get('session')))
		doc.filiere=Filiere.objects.get(id=int(request.POST.get('filiere')))
		doc.examen=Examen.objects.get(id=int(request.POST.get('examen')))
		doc.Type_document=Type_document.objects.get(id=int(request.POST.get('type_document')))
		doc.annee_academique=Annee_academique.objects.get(id=int(request.POST.get('annee_academique')))


		if request.FILES.get('fichier'):
			deleteFile(doc.fichier)
			file_input=request.FILES.get("fichier")
			doc.fichier=uploadFile(file_input, "archives/", '.pdf')

		doc.save()
	else:
		deleteFile(doc.fichier)
		doc.delete()

	return redirect('list_etudiant')

@login_required
def details(request, id):
	doc =Etudiant.objects.get(id=id)
	return render(request,'Etudiant/details.html',{'doc':doc})

@login_required
def found(request):
	if request.method=="POST":
		data=Etudiant.objects.filter( annee_academique=int( request.POST.get('annee_academique') ) )
		if request.POST.get('niveau'):
			data=data.filter(niveau=int( request.POST.get('niveau') ))
		if request.POST.get('session'):
			data=data.filter(session=int( request.POST.get('session') ))
		if request.POST.get('filiere'):
			data=data.filter(filiere=int( request.POST.get('filiere') ))
		if request.POST.get('Type_document'):
			data=data.filter(Type_document=int( request.POST.get('Type_document') ))
		#export(data)
		return render(request,'Etudiant/index.html',{'data':data})



def uploadFile(file_input, folder, extension):
	name=str(datetime.now().strftime("_%Y_%m_%d_%H_%M_%S"))+str(extension)
	file_name=folder+name
	if not os.path.exists(file_name):
		default_storage.save('static/'+file_name, file_input)
	return file_name

def deleteFile(link):
	os.remove('static/'+link)