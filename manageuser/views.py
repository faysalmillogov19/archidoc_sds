from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def list(request):
	users=User.objects.all()
	return render(request,'registration/list.html',{'data':users})
def set_profil_form(request, id):
	user= User.objects.get(id=id)
	return render(request,'registration/set_profil_form.html',{'data':user})

def save_profil(request, id):
	if request.method=='POST':
		user= User.objects.get(id=id)
		user.is_superuser=int(request.POST.get('profil'))
		user.save()
	return redirect('list_user')

def delete(request, id):
	user= User.objects.get(id=id).delete()
	return redirect('list_user')


def index(request):
	
	if request.user.is_authenticated :
		return redirect('/')

	if request.POST:
		email=request.POST.get('email')
		password=request.POST.get('password')
		user = authenticate(username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('/') #serializers.serialize('user', user) #JsonResponse(data)	
		else:
			message="Nom utilisateur ou mot de passe incorrecte. Vérifier vos informations."
			return render(request,'registration/login.html',{'email':email,'password':password,"message":message})
	else :
		return render(request,'registration/login.html')


def deconnexion(request):
	logout(request)
	return redirect('/login')

def create(request):
	if request.POST:
		user = User.objects.create_user(request.POST.get('prenom'), request.POST.get('email'), request.POST.get('pass'))
		user.last_name=request.POST.get('nom')
		user.first_name=request.POST.get('prenom')
		user.username=request.POST.get('username')
		user.save()
		print(user)
		return redirect('/')

	else:
		return render(request, 'registration/user_details.html')