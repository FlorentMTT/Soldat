# Generated by Django 4.1.4 on 2022-12-18 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=32)),
                ('niveau', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='Soldat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=32)),
                ('grade', models.DecimalField(decimal_places=0, max_digits=1)),
                ('specialite', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Possede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.equipement')),
                ('soldat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.soldat')),
            ],
        ),
        migrations.CreateModel(
            name='Arme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=32)),
                ('niveau', models.DecimalField(decimal_places=0, max_digits=1)),
                ('nbMunition', models.DecimalField(decimal_places=0, max_digits=2)),
                ('soldat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.soldat')),
            ],
        ),
    ]
