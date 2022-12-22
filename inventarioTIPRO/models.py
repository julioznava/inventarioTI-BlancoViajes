from django.db import models

# Create your models here.

opcion_MARCA_PC = [
    ["Lenovo", "Lenovo"],
    ["Dell", "Dell"],
    ["HP", "HP"],
    ["Generico", "Generico"],
]

opcion_MARCA_MONITOR = [
    ["LG", "LG"],
    ["DELL", "DELL"],
    ["HP", "HP"],
    ["AOC", "AOC"],

]


opcion_MARCA_MOUSE = [
    ["GENIUS", "GENIUS"],
    ["LENOVO", "LENOVO"],
]

opcion_MARCA_TECLADO = [
    ["GENIUS", "GENIUS"],
    ["LENOVO", "LENOVO"],
    ["LOGITEC", "LOGITEC"],

]


opcion_TIPO = [
    ["DESKTOP", "DESKTOP"],
    ["LAPTOP", "LAPTOP"],
]

opcion_so = [
    ["Windows 7", "Windows 7"],
    ["Windows 10", "Windows 10"],
    ["Android", "Android"],
    ["Otros", "Otros"],
]

opcion_HDD = [
    ["100GB", "100GB"],
    ["120GB", "120GB"],
    ["200GB", "200GB"],
    ["250GB", "250GB"],
    ["500GB", "500GB"],
    ["1TB", "1TB"],
]

opcion_RAM = [
    ["2GB", "2GB"],
    ["4GB", "4GB"],
    ["6GB", "6GB"],
    ["8GB", "8GB"],
    ["16GB", "16GB"],
    ["32GB", "32GB"],
]

opcion_PROCESADOR = [
    ["AMD A6-3500", "AMD A6-3500"],
    ["AMD A6-6400", "AMD A6-6400"],
    ["CELERON G1610", "CELERON G1610"],
    ["CELERON G550", "CELERON G550"],
    ["I3 7100U", "I3 7100U"],
    ["I5 8400", "I5 8400"],
    ["I5-1035G1", "I5-1035G1"],
    ["I5-3570", "I5-3570"],
    ["I5-8265U", "I5-8265U"],
    ["RYZEN-5 5500U", "RYZEN-5 5500U"],
]

opcion_ESTADO = [
    ["Nuevo", "Nuevo"],
    ["Usado", "Usado"],
    ["Activo", "Activo"],
    ["Inactivo", "Inactivo"],
    ["Desuso", "Desuso"],
]

opcion_PERIFERICO = [
    ["Audifonos", "Audifonos"],
    ["Adaptador inalambrico", "Adaptador inalambrico"],
    ["Webcam", "Webcam"],
    ["Cargadores", "Cargadores"],
    ["Cargadores", "Cargadores"],
    ["Otros", "Otros"],
]

opcion_TELEFONIA = [
    ["Telefonia fija", "Telefonia fija"],
    ["Telefonia movil", "Telefonia movil"],
]

opcion_DEPARTAMENTOS = [
    ["Informatica","Informatica"],
    ["Corporativo","Corporativo"],
    ["Ventas","Ventas"],
    ["BTA","BTA"],
    ["BTG","BTG"],
    ["BTO","BTO"],
    ["Administracion","Administracion"],
    ["Operaciones","Operaciones"],
    ["Gerencia General","Gerencia General"],
    ["KAM","KAM"],
    ["Despacho","Despacho"],
]

opcion_USUARIOS = [
    ["Boggie, Maria Fernanda", "Boggie, Maria Fernanda"],
    ["Bravo, Marta Jimena", "Bravo, Marta Jimena"],
    ["Bustamante, Luis Armando", "Bustamante, Luis Armando"],
    ["Cardenas, Daisy Dayana", "Cardenas, Daisy Dayana"],
    ["Caviedes, Manuel Enrique", "Caviedes, Manuel Enrique"],
    ["Céspedes, Casandra Catalina", "Céspedes, Casandra Catalina"],
    ["Gonzalez, Erica Del Carmen", "Gonzalez, Erica Del Carmen"],
    ["Gonzalez, Margarita Del Carmen", "Gonzalez, Margarita Del Carmen"],
    ["Grandon, Pamela Loreto", "Grandon, Pamela Loreto"],
    ["Hermosilla, Valois Eleazar", "Hermosilla, Valois Eleazar"],
    ["Hernandez, America", "Hernandez, America"],
    ["Jantzent, Fernando", "Jantzent, Fernando"],
    ["Jimenez, Gianina Andrea", "Jimenez, Gianina Andrea"],
    ["Kromschroder, Juan Oscar", "Kromschroder, Juan Oscar"],
    ["Kromschroder, Juan", "Kromschroder, Juan"],
    ["Luna, Natalia Andrea", "Luna, Natalia Andrea"],
    ["Meneses, Yesenia Jackeline", "Meneses, Yesenia Jackeline"],
    ["Merchan, Gisselle Karolina", "Merchan, Gisselle Karolina"],
    ["Navarro, Julio Esteban", "Navarro, Julio Esteban"],
    ["Olea, Mireya Pamela", "Olea, Mireya Pamela"],
    ["Ramirez, Carlos Rafael", "Ramirez, Carlos Rafael"],
    ["Sanchez, Yineth Esperanza", "Sanchez, Yineth Esperanza"],
    ["Toro, Maritza Soledad", "Toro, Maritza Soledad"],
    ["Valenzuela, Karina Andrea", "Valenzuela, Karina Andrea"],
    ["Vargas, Karina Andrea", "Vargas, Karina Andrea"],
    ["Venegas, Carlos Sebastian", "Venegas, Carlos Sebastian"],
    ["Vera, Nelly", "Vargas, Vera, Nelly"],
    ["Zamora, Francisco Javier", "Zamora, Francisco Javier"],
]




class Equipos(models.Model):
    codigo = models.CharField(max_length=100)
    serieproducto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=opcion_TIPO, null=True)
    marca = models.CharField(max_length=100, choices=opcion_MARCA_PC)
    modelo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=50, choices=opcion_PROCESADOR)
    sistema_operativo = models.CharField(max_length=100, choices=opcion_so)
    disco_duro = models.CharField(max_length=100, choices=opcion_HDD)
    memoria_ram = models.CharField(max_length=100, choices=opcion_RAM)
    direccion_ip = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.modelo


class Monitores(models.Model):
    codigo = models.CharField(max_length=100)
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=opcion_MARCA_MONITOR)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.modelo


class Mouse(models.Model):
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=opcion_MARCA_MOUSE)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.modelo


class Teclado(models.Model):
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=opcion_MARCA_TECLADO)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.modelo


class Perifericos(models.Model):
    tipo_periferico = models.CharField(max_length=100, choices=opcion_PERIFERICO)
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.tipo_periferico

class Impresoras(models.Model):
    codigo = models.CharField(max_length=100)
    serieproducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.modelo

class Telefonia(models.Model):
    tipo_telefonia = models.CharField(max_length= 50, choices=opcion_TELEFONIA)
    codigo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    sistema_operativo = models.CharField(max_length=100, choices=opcion_so)
    estado = models.CharField(max_length=100, choices=opcion_ESTADO)
    observaciones = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.marca

class Departamento(models.Model):
    departamento = models.CharField(max_length=50, choices=opcion_DEPARTAMENTOS)

    def __str__(self):
        return self.departamento

class Persona(models.Model):
    persona = models.CharField(max_length=50, choices=opcion_USUARIOS)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)
    equipos = models.ForeignKey(Equipos, on_delete=models.PROTECT, null=True)
    monitores = models.ForeignKey(Monitores, on_delete=models.PROTECT, null=True, blank=True)
    mouse = models.ForeignKey(Mouse, on_delete=models.PROTECT, null=True, blank=True)
    teclado = models.ForeignKey(Teclado, on_delete=models.PROTECT, null=True,blank=True)
    perifericos = models.ForeignKey(Perifericos, on_delete=models.PROTECT, null=True, blank=True)
    telefonia = models.ForeignKey(Telefonia, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.persona


