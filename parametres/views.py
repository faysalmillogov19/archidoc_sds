from django.shortcuts import render, redirect
from .models import Annee_academique, Filiere, Session, Niveau, Type_document, Examen

# Create your views here.
def list_annee_academique(request):
	
	if request.method == "POST":
		annee = Annee_academique()
		annee.libelle=request.POST.get('libelle')
		annee.debut=request.POST.get('debut')
		annee.fin=request.POST.get('fin')
		annee.save()

	annee_academiques=Annee_academique.objects.all()

	return render(request,  'annee_academique/index.html', {'annee_academiques':annee_academiques } )

def annee_academiqueForm(request, id):
	annee=0
	if id > 0:
		annee=Annee_academique.objects.get(id=id)
	return render(request, 'annee_academique/form.html', {'annee':annee})

def set_annee_academique(request, id):
	annee=Annee_academique.objects.get(id=id)
	if request.method == "POST":
		annee.libelle=request.POST.get('libelle')
		annee.debut=request.POST.get('debut')
		annee.fin=request.POST.get('fin')
		annee.save()
	else:
		annee.delete()

	return redirect('list_annee_academique')


	# FILIERE.
def list_filiere(request):
	

	if request.method == "POST":
		data = Filiere()
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()

	data=Filiere.objects.all()

	return render(request,  'filiere/index.html', {'data':data } )

def filiere_form(request, id):
	data=0
	if id > 0:
		data=Filiere.objects.get(id=id)
	return render(request, 'filiere/form.html', {'data':data})

def set_filiere(request, id):
	data=Filiere.objects.get(id=id)
	if request.method == "POST":
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()
	else:
		data.delete()

	return redirect('list_filiere')

# SESSION
def list_session(request):
	
	if request.method == "POST":
		data = Session()
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()

	data=Session.objects.all()

	return render(request,  'session/index.html', {'data':data } )

def session_form(request, id):
	data=0
	if id > 0:
		data=Session.objects.get(id=id)
	return render(request, 'session/form.html', {'data':data})

def set_session(request, id):
	data=Session.objects.get(id=id)
	if request.method == "POST":
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()
	else:
		data.delete()

	return redirect('list_session')

#NIVEAUX

def list_niveau(request):
	

	if request.method == "POST":
		data = Niveau()
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()

	data=Niveau.objects.all()

	return render(request,  'niveau/index.html', {'data':data } )

def niveau_form(request, id):
	data=0
	if id > 0:
		data=Niveau.objects.get(id=id)
	return render(request, 'niveau/form.html', {'data':data})

def set_niveau(request, id):
	data=Niveau.objects.get(id=id)
	if request.method == "POST":
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()
	else:
		data.delete()

	return redirect('list_niveau')


##TYPE DOCUMENT

def list_type(request):
	
	if request.method == "POST":
		data = Type_document()
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()

	data=Type_document.objects.all()

	return render(request,  'type/index.html', {'data':data } )

def type_form(request, id):
	data=0
	if id > 0:
		data=Type_document.objects.get(id=id)
	return render(request, 'type/form.html', {'data':data})

def set_type(request, id):
	data=Type_document.objects.get(id=id)
	if request.method == "POST":
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()
	else:
		data.delete()

	return redirect('list_type')


## EXAMEN

def list_examen(request):
	
	if request.method == "POST":
		data = Examen()
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()

	data=Examen.objects.all()

	return render(request,  'examen/index.html', {'data':data } )

def examen_form(request, id):
	data=0
	if id > 0:
		data=Examen.objects.get(id=id)
	return render(request, 'examen/form.html', {'data':data})

def set_examen(request, id):
	data=Examen.objects.get(id=id)
	if request.method == "POST":
		data.libelle=request.POST.get('libelle')
		data.description=request.POST.get('description')
		data.save()
	else:
		data.delete()

	return redirect('list_examen')
