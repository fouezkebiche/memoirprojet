# Generated by Django 4.1.2 on 2023-04-15 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_faculte_id_univ'),
    ]

    operations = [
        migrations.CreateModel(
            name='absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_absence', models.IntegerField()),
                ('nom_etd', models.CharField(max_length=50)),
                ('specialite', models.CharField(max_length=50)),
                ('entreprise', models.CharField(max_length=50)),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
                ('nom_maitre', models.CharField(max_length=30)),
                ('date_jour', models.DateField()),
                ('heure_entre', models.TimeField()),
                ('heure_sorte', models.TimeField()),
                ('observation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='attestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_att', models.IntegerField()),
                ('nome_etd', models.CharField(max_length=50)),
                ('nome_maite', models.CharField(max_length=50)),
                ('etat_att', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_depart', models.IntegerField()),
                ('nom_depart', models.CharField(max_length=50)),
                ('id_fac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.faculte')),
            ],
        ),
        migrations.CreateModel(
            name='entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_entr', models.IntegerField()),
                ('nom_entr', models.CharField(max_length=50)),
                ('adresse_entr', models.CharField(max_length=50)),
                ('email_entr', models.CharField(max_length=25)),
                ('numéro_tlf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_etd', models.IntegerField()),
                ('nom_etd', models.CharField(max_length=50)),
                ('prenom_etd', models.CharField(max_length=50)),
                ('dateN_etd', models.DateField()),
                ('lieuN_etd', models.CharField(max_length=25)),
                ('specialite_etd', models.CharField(max_length=20)),
                ('niveau_etd', models.CharField(max_length=10)),
                ('semaistre', models.CharField(max_length=10)),
                ('annee_univ', models.IntegerField()),
                ('email_etd', models.EmailField(max_length=254)),
                ('pswd_etd', models.CharField(max_length=25)),
                ('numcard_etd', models.IntegerField()),
                ('num_securite', models.IntegerField()),
                ('num_telf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='notation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_note', models.IntegerField()),
                ('nom_etd', models.CharField(max_length=50)),
                ('dateN_etd', models.DateField()),
                ('lieuN_etd', models.CharField(max_length=25)),
                ('dateInscrit', models.DateField()),
                ('semaistre', models.CharField(max_length=10)),
                ('deplomeprepare', models.CharField(max_length=50)),
                ('durestaige', models.CharField(max_length=20)),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
                ('entreprise', models.CharField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
                ('plan_de_travail', models.TextField()),
                ('note', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_stage', models.IntegerField()),
                ('nom_etd', models.CharField(max_length=50)),
                ('prenom_etd', models.CharField(max_length=50)),
                ('faculte', models.CharField(max_length=50)),
                ('departement', models.CharField(max_length=50)),
                ('numcard_etd', models.IntegerField()),
                ('num_telf', models.IntegerField()),
                ('deplomeprepare', models.CharField(max_length=50)),
                ('themestaige', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('durestaige', models.CharField(max_length=20)),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
                ('num_securite', models.IntegerField()),
                ('id_depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.departement')),
                ('id_etd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.etudiant')),
                ('id_faculte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.faculte')),
            ],
        ),
        migrations.CreateModel(
            name='maitredestaige',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_maitre', models.IntegerField()),
                ('nom_maitre', models.CharField(max_length=50)),
                ('prenom_maitre', models.CharField(max_length=50)),
                ('email_maitre', models.CharField(max_length=50)),
                ('pswd_maitre', models.CharField(max_length=20)),
                ('id_entr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='chefDepartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_chef', models.IntegerField()),
                ('nom_chef', models.CharField(max_length=50)),
                ('prenom_chef', models.CharField(max_length=50)),
                ('email_chef', models.CharField(max_length=25)),
                ('pswd_chef', models.CharField(max_length=20)),
                ('id_depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.departement')),
            ],
        ),
    ]