from django.contrib import admin
from .models import Persona, Equipos, Monitores, Perifericos, Impresoras, Telefonia, Departamento

# Register your models here.
admin.site.register(Persona)
admin.site.register(Departamento)
admin.site.register(Equipos)
admin.site.register(Monitores)
admin.site.register(Perifericos)
admin.site.register(Impresoras)
admin.site.register(Telefonia)