from django.contrib import admin
from .models import université,faculte,departement,chefDepartement,entreprise,maitredestaige,etudiant,stage,absence,notation,attestation
# Register your models here.

admin.site.register(université)
admin.site.register(faculte)
admin.site.register(departement)
admin.site.register(chefDepartement)
admin.site.register(entreprise)
admin.site.register(maitredestaige)
admin.site.register(etudiant)
admin.site.register(stage)
admin.site.register(absence)
admin.site.register(notation)
admin.site.register(attestation)

