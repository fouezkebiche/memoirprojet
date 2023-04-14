from django.shortcuts import render
# from django.http import HttpResponse
# from django.urls import reverse
from .models import université,faculte


# Create your views here.

def main(request):
  return render(request, 'main.html')

def login(request):
  return render(request, 'formulaire.html')

def etudiant(request):
  return render(request, 'etudiant.html')

def demandesetd(request):
  return render(request, 'etddemande.html')

def chefdepart(request):
  return render(request, 'chefdepart.html')

def demandes(request):
  return render(request, 'demandes.html')

def datademande(request):
  return render(request, 'datademande.html')

def maitredestaige(request):
  return render(request, 'maitredstaige.html')

def notation(request):
  return render(request, 'notation.html')

def absence(request):
  return render(request, 'absence.html')

def test(request):
  return render(request,'test.html',{'name':université.objects.all()})
