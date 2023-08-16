from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from datetime import datetime, timedelta
import os
from .models import Document
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
	data = Document.objects.all()
	return render(request,'Document/index.html',{'data':data})
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
		data=Document.objects.get(id=id)

	return render(request,'Document/form.html', {'data':data, 'annees':annees, 'filieres':filieres, 'niveaux':niveaux, 'sessions':sessions, 'type_documents':type_documents,'examens':examens})

@login_required
def search(request):

	annees=Annee_academique.objects.all()
	filieres=Filiere.objects.all()
	niveaux=Niveau.objects.all()
	sessions=Session.objects.all()
	type_documents=Type_document.objects.all()
	

	return render(request,'Document/search.html', {'annees':annees, 'filieres':filieres, 'niveaux':niveaux, 'sessions':sessions, 'type_documents':type_documents})


@login_required

def save(request):
	doc=Document()
	doc.niveau= Niveau.objects.get(id=int(request.POST.get('niveau'))) 
	doc.session1=Session.objects.get(id=int(request.POST.get('session1')))
	doc.session2=Session.objects.get(id=int(request.POST.get('session2')))
	doc.filiere=Filiere.objects.get(id=int(request.POST.get('filiere')))
	doc.examen=Examen.objects.get(id=int(request.POST.get('examen')))
	doc.type_document=Type_document.objects.get(id=int(request.POST.get('type_document')))
	doc.annee_academique=Annee_academique.objects.get(id=int(request.POST.get('annee_academique')))

	if request.FILES.get("fichier"):
		file_input=request.FILES.get("fichier")
		doc.fichier=uploadFile(file_input, "archives/", '.pdf')

	doc.save()

	data= Document.objects.all()

	return redirect('list_archive')

@login_required
def set(request, id):

	doc=Document.objects.get(id=id)
	if request.method=="POST":
		doc.niveau= Niveau.objects.get(id=int(request.POST.get('niveau'))) 
		doc.session1=Session.objects.get(id=int(request.POST.get('session1')))
		doc.session2=Session.objects.get(id=int(request.POST.get('session2')))
		doc.filiere=Filiere.objects.get(id=int(request.POST.get('filiere')))
		doc.examen=Examen.objects.get(id=int(request.POST.get('examen')))
		doc.type_document=Type_document.objects.get(id=int(request.POST.get('type_document')))
		doc.annee_academique=Annee_academique.objects.get(id=int(request.POST.get('annee_academique')))


		if request.FILES.get('fichier'):
			deleteFile(doc.fichier)
			file_input=request.FILES.get("fichier")
			doc.fichier=uploadFile(file_input, "archives/", '.pdf')

		doc.save()
	else:
		deleteFile(doc.fichier)
		doc.delete()

	return redirect('list_archive')

@login_required
def details(request, id):
	doc =Document.objects.get(id=id)
	return render(request,'Document/details.html',{'doc':doc})

@login_required
def found(request):
	if request.method=="POST":
		data=Document.objects.filter( annee_academique=int( request.POST.get('annee_academique') ) )
		if request.POST.get('niveau'):
			data=data.filter(niveau=int( request.POST.get('niveau') ))
		if request.POST.get('session'):
			data=data.filter(session=int( request.POST.get('session1') ))
		if request.POST.get('filiere'):
			data=data.filter(filiere=int( request.POST.get('filiere') ))
		if request.POST.get('type_document'):
			data=data.filter(type_document=int( request.POST.get('type_document') ))
		#export(data)
		return render(request,'Document/index.html',{'data':data})

def export(data):
	table=[]
	for row in data:
		#pdfReader = PyPDF2.PdfReader('static/'+row.fichier)
		#print(pdfReader.numPages)
		n_row=[str(row.annee_academique.debut)+'-'+str(row.annee_academique.fin), row.filiere.libelle, row.niveau.libelle, row.session.libelle, row.type_document.libelle,row.fichier ]
		table.append(n_row)
		convertPDFToExcel(row)
	df = pd.DataFrame( table, columns=['Annee_academique', 'Filiere', 'Niveau','Session', 'Type_document','Fichier'] )
	return df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')

def convertPDFToExcel(row):
	#for row in data:
	df = tabula.read_pdf('static/'+row.fichier, pages = 'all')[0]
	df.head()
	df.to_excel('file.xlsx')


def uploadFile(file_input, folder, extension):
	name=str(datetime.now().strftime("_%Y_%m_%d_%H_%M_%S"))+str(extension)
	file_name=folder+name
	if not os.path.exists(file_name):
		default_storage.save('static/'+file_name, file_input)
	return file_name

def deleteFile(link):
	os.remove('static/'+link)