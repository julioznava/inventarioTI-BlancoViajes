# Generated by Django 4.1.6 on 2023-02-13 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioTIPRO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='marca',
            field=models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI'], ['D-LINK', 'D-LINK']], max_length=100),
        ),
        migrations.AlterField(
            model_name='monitores',
            name='marca',
            field=models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI'], ['D-LINK', 'D-LINK']], max_length=100),
        ),
        migrations.AlterField(
            model_name='perifericos',
            name='marca',
            field=models.CharField(choices=[['AOC', 'AOC'], ['DELL', 'DELL'], ['GENIUS', 'GENIUS'], ['LENOVO', 'LENOVO'], ['LG', 'LG'], ['LOGITEC', 'LOGITEC'], ['HP', 'HP'], ['GENERICO', 'GENERICO'], ['POLI', 'POLI'], ['D-LINK', 'D-LINK']], max_length=100),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarios', models.CharField(choices=[['Boggie, Maria Fernanda', 'Boggie, Maria Fernanda'], ['Bravo, Marta Jimena', 'Bravo, Marta Jimena'], ['Bustamante, Luis Armando', 'Bustamante, Luis Armando'], ['Cardenas, Daisy Dayana', 'Cardenas, Daisy Dayana'], ['Caviedes, Manuel Enrique', 'Caviedes, Manuel Enrique'], ['Céspedes, Casandra Catalina', 'Céspedes, Casandra Catalina'], ['Gonzalez, Erica Del Carmen', 'Gonzalez, Erica Del Carmen'], ['Gonzalez, Margarita Del Carmen', 'Gonzalez, Margarita Del Carmen'], ['Grandon, Pamela Loreto', 'Grandon, Pamela Loreto'], ['Hermosilla, Valois Eleazar', 'Hermosilla, Valois Eleazar'], ['Hernandez, America', 'Hernandez, America'], ['Jantzent, Fernando', 'Jantzent, Fernando'], ['Jimenez, Gianina Andrea', 'Jimenez, Gianina Andrea'], ['Kromschroder, Juan Oscar', 'Kromschroder, Juan Oscar'], ['Kromschroder, Juan', 'Kromschroder, Juan'], ['Meneses, Yesenia Jackeline', 'Meneses, Yesenia Jackeline'], ['Merchan, Gisselle Karolina', 'Merchan, Gisselle Karolina'], ['Navarro, Julio Esteban', 'Navarro, Julio Esteban'], ['Olea, Mireya Pamela', 'Olea, Mireya Pamela'], ['Ramirez, Carlos Rafael', 'Ramirez, Carlos Rafael'], ['Sanchez, Yineth Esperanza', 'Sanchez, Yineth Esperanza'], ['Toro, Maritza Soledad', 'Toro, Maritza Soledad'], ['Valenzuela, Karina Andrea', 'Valenzuela, Karina Andrea'], ['Vargas, Karina Andrea', 'Vargas, Karina Andrea'], ['Venegas, Carlos Sebastian', 'Venegas, Carlos Sebastian'], ['Vera, Nelly', 'Vargas, Vera, Nelly'], ['Zamora, Francisco Javier', 'Zamora, Francisco Javier']], max_length=100, verbose_name='Asignado')),
                ('departamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioTIPRO.departamento')),
            ],
        ),
    ]