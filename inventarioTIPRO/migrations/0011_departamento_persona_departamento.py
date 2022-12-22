# Generated by Django 4.1.1 on 2022-10-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioTIPRO', '0010_alter_persona_impresoras_alter_persona_monitores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(choices=[['Informatica', 'Informatica'], ['Corporativo', 'Corporativo'], ['Ventas', 'Ventas'], ['BTA', 'BTA'], ['BTG', 'BTG'], ['BTO', 'BTO'], ['Administracion', 'Administracion'], ['Operaciones', 'Operaciones'], ['Gerencia General', 'Gerencia General'], ['KAM', 'KAM'], ['Despacho', 'Despacho']], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventarioTIPRO.departamento'),
        ),
    ]
