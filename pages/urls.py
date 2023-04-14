from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='index'),
    path('login/',views.login,name='login'),
    path('etudiant/',views.etudiant,name='etudiant'),
    path('demandesetd/',views.demandesetd,name='demandesetd'),
    path('chefdepart/',views.chefdepart,name='chefdepart'),
    path('demandes/',views.demandes,name='demandes'),
    path('datademande/',views.datademande,name='datademande'),
    path('maitredestaige/',views.maitredestaige,name='maitredestaige'),
    path('notation/',views.notation,name='notation'),
    path('absence/',views.absence,name='absence'),
    path('test/',views.test,name='test'),




]
