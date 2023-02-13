# Generated by Django 4.1.6 on 2023-02-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(choices=[['Informatica', 'Informatica'], ['Corporativo', 'Corporativo'], ['Ventas', 'Ventas'], ['BTA', 'BTA'], ['BTG', 'BTG'], ['BTO', 'BTO'], ['Administracion', 'Administracion'], ['Operaciones', 'Operaciones'], ['Gerencia General', 'Gerencia General'], ['KAM', 'KAM'], ['Despacho', 'Despacho']], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('serieproducto', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[['DESKTOP', 'DESKTOP'], ['LAPTOP', 'LAPTOP']], max_length=50, null=True)),
                ('marca', models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI]'], ['D-LINK', 'D-LINK']], max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('procesador', models.CharField(choices=[['AMD A6-3500', 'AMD A6-3500'], ['AMD A6-6400', 'AMD A6-6400'], ['CELERON G1610', 'CELERON G1610'], ['CELERON G550', 'CELERON G550'], ['I3 7100U', 'I3 7100U'], ['I5 8400', 'I5 8400'], ['I5-1035G1', 'I5-1035G1'], ['I5-3570', 'I5-3570'], ['I5-8265U', 'I5-8265U'], ['RYZEN-5 5500U', 'RYZEN-5 5500U']], max_length=50)),
                ('sistema_operativo', models.CharField(choices=[['Windows 7', 'Windows 7'], ['Windows 10', 'Windows 10'], ['Android', 'Android'], ['Otros', 'Otros']], max_length=100)),
                ('disco_duro', models.CharField(choices=[['100GB', '100GB'], ['120GB', '120GB'], ['200GB', '200GB'], ['250GB', '250GB'], ['500GB', '500GB'], ['1TB', '1TB']], max_length=100)),
                ('memoria_ram', models.CharField(choices=[['2GB', '2GB'], ['4GB', '4GB'], ['6GB', '6GB'], ['8GB', '8GB'], ['16GB', '16GB'], ['32GB', '32GB']], max_length=100)),
                ('direccion_ip', models.CharField(max_length=50)),
                ('hostname', models.CharField(max_length=50, null=True)),
                ('estado', models.CharField(choices=[['Nuevo', 'Nuevo'], ['Usado', 'Usado'], ['Activo', 'Activo'], ['Inactivo', 'Inactivo'], ['Desuso', 'Desuso']], max_length=100)),
                ('observaciones', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Monitores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('serieproducto', models.CharField(max_length=100)),
                ('marca', models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI]'], ['D-LINK', 'D-LINK']], max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[['Nuevo', 'Nuevo'], ['Usado', 'Usado'], ['Activo', 'Activo'], ['Inactivo', 'Inactivo'], ['Desuso', 'Desuso']], max_length=100)),
                ('observaciones', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Perifericos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_periferico', models.CharField(choices=[['Audifonos', 'Audifonos'], ['Adaptador inalambrico', 'Adaptador inalambrico'], ['Cargadores', 'Cargadores'], ['Cintillos', 'Cintillos'], ['Mouse', 'Mouse'], ['Teclado', 'Teclado'], ['Webcam', 'Webcam']], max_length=100)),
                ('serieproducto', models.CharField(max_length=100)),
                ('marca', models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI]'], ['D-LINK', 'D-LINK']], max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[['Nuevo', 'Nuevo'], ['Usado', 'Usado'], ['Activo', 'Activo'], ['Inactivo', 'Inactivo'], ['Desuso', 'Desuso']], max_length=100)),
                ('observaciones', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
