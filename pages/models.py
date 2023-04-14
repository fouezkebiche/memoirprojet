from django.db import models

# Create your models here.

class université(models.Model):
    id_univ=models.IntegerField()
    nom_univ=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_univ
    

class faculte(models.Model):
    id_fac = models.IntegerField()
    nom_fac = models.CharField(max_length=50)
    id_univ= models.ForeignKey(université,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_fac
    

class departement(models.Model):
    id_depart=models.IntegerField()
    nom_depart=models.CharField(max_length=50)
    id_fac=models.ForeignKey(faculte,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_depart
    

class chefDepartement(models.Model):
    id_chef=models.IntegerField()  
    id_depart=models.ForeignKey(departement,on_delete=models.CASCADE)  
    nom_chef=models.CharField(max_length=50) 
    prenom_chef =models.CharField(max_length=50)
    email_chef =models.CharField(max_length=25)
    pswd_chef=models.CharField(max_length=20)

    def __str__(self):
        return self.nom_chef
    

class entreprise(models.Model):
    id_entr=models.IntegerField()  
    nom_entr=models.CharField(max_length=50)  
    adresse_entr =models.CharField(max_length=50)
    email_entr=models.CharField(max_length=25)  
    numéro_tlf=models.IntegerField()

    def __str__(self):
        return self.nom_entr
    

class maitredestaige(models.Model):
    id_maitre=models.IntegerField()  
    id_entr=models.ForeignKey(entreprise,on_delete=models.CASCADE)  
    nom_maitre=models.CharField(max_length=50) 
    prenom_maitre =models.CharField(max_length=50)
    email_maitre =models.CharField(max_length=50)
    pswd_maitre=models.CharField(max_length=20)

    def __str__(self):
        return self.nom_maitre
    

class etudiant(models.Model):
    id_etd=models.IntegerField()
    nom_etd=models.CharField(max_length=50)
    prenom_etd=models.CharField(max_length=50)
    dateN_etd=models.DateField()
    lieuN_etd=models.CharField(max_length=25)
    specialite_etd=models.CharField(max_length=20)
    niveau_etd=models.CharField(max_length=10)
    semaistre=models.CharField(max_length=10)
    annee_univ=models.IntegerField()
    email_etd=models.EmailField()
    pswd_etd=models.CharField(max_length=25)
    numcard_etd=models.IntegerField()
    num_securite=models.IntegerField()
    num_telf=models.IntegerField()

    def __str__(self):
        return self.nom_etd
    

    # id_stage=models.ForeignKey(stage,on_delete=models.CASCADE)
    # id_depart=models.ForeignKey(departement,on_delete=models.CASCADE)

class stage(models.Model):
    id_stage =models.IntegerField()
    id_etd=models.ForeignKey(etudiant,on_delete=models.CASCADE)
    nom_etd=models.CharField(max_length=50)
    prenom_etd=models.CharField(max_length=50)
    id_faculte=models.ForeignKey(faculte,on_delete=models.CASCADE)
    faculte=models.CharField(max_length=50)
    id_depart=models.ForeignKey(departement,on_delete=models.CASCADE)
    departement=models.CharField(max_length=50)
    numcard_etd=models.IntegerField()
    num_telf=models.IntegerField()
    deplomeprepare=models.CharField(max_length=50)
    themestaige=models.CharField(max_length=50)
    responsable=models.CharField(max_length=50)
    durestaige=models.CharField(max_length=20)
    datedebut=models.DateField()
    datefin=models.DateField()
    num_securite=models.IntegerField()

    def __str__(self):
        return self.id_stage
    

class absence(models.Model):
    id_absence =models.IntegerField()
    nom_etd=models.CharField(max_length=50)
    specialite=models.CharField(max_length=50)
    entreprise=models.CharField(max_length=50)
    datedebut=models.DateField()
    datefin=models.DateField()
    nom_maitre=models.CharField(max_length=30)
    date_jour=models.DateField()
    heure_entre=models.TimeField() 
    heure_sorte=models.TimeField()
    observation=models.TextField()  

    def __str__(self):
        return self.nom_etd
    

class notation(models.Model):
    id_note=models.IntegerField()
    entreprise=models.CharField(max_length=50)
    nom_etd=models.CharField(max_length=50)
    dateN_etd=models.DateField()
    lieuN_etd=models.CharField(max_length=25)
    dateInscrit=models.DateField()
    semaistre=models.CharField(max_length=10)
    deplomeprepare=models.CharField(max_length=50)
    durestaige=models.CharField(max_length=20)
    datedebut=models.DateField()
    datefin=models.DateField()
    entreprise=models.CharField(max_length=50)
    lieu=models.CharField(max_length=50)
    plan_de_travail=models.TextField()
    note=models.IntegerField()

    def __str__(self):
        return self.nom_etd
    

class attestation(models.Model):
    id_att=models.IntegerField()
    nome_etd=models.CharField(max_length=50)
    nome_maite=models.CharField( max_length=50)
    etat_att=models.TextField()

    def __str__(self):
        return self.nome_etd
    
    

    




    


    
      
    
    
