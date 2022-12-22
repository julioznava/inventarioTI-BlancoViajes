from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Equipos, Monitores, Perifericos, Impresoras, Telefonia
from .forms import EquiposForm, MonitoresForm, PerifericosForm, ImpresorasForm, TelefoniaForm, CustomUserCreationForm, PersonasForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Equipos.objects.filter(codigo__icontains=q)
    else:
        data = Equipos.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home.html')


def login(request):
    return render(request, 'registration/login.html')

def panel(request):
    return render(request, 'panel.html')

def equipos(request):
    data = {
        'form': EquiposForm()
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se han ingresado los datos correctamente."
        else:
            data['form'] = formulario

    return render(request, 'equipos.html', data)


def listarequipos(request):

    listar = Equipos.objects.all()

    data = {
        'listar': listar,
    }
    return render(request, 'listarequipos.html', data)


def modificarequipos(request, id):
    equipos = get_object_or_404(Equipos, id=id)

    data = {
        'form':EquiposForm(instance=equipos)
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST, instance=equipos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarequipos")
        data["form"] = formulario

    return render(request, 'modificarequipos.html', data)


def eliminarequipos(request, id):
    eliminarequipo = get_object_or_404(Equipos, id=id)
    eliminarequipo.delete()
    return redirect(to="listarequipos")




def monitores(request):
    data = {
        'form': MonitoresForm()
    }
    if request.method == 'POST':
        formulario = MonitoresForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'monitores.html', data)


def listarmonitores(request):
    listar = Monitores.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'listarmonitores.html', data)


def modificarmonitores(request, id):
    monitores = get_object_or_404(Monitores, id=id)

    data = {
        'form':MonitoresForm(instance=monitores)
    }
    if request.method == 'POST':
        formulario = MonitoresForm(data=request.POST, instance=monitores)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarmonitores")
        data["form"] = formulario

    return render(request, 'modificarmonitores.html', data)


def eliminarmonitores(request, id):
    eliminarmonitor = get_object_or_404(Monitores, id=id)
    eliminarmonitor.delete()
    return redirect(to="listarmonitores")




def perifericos(request):
    data = {
        'form': PerifericosForm()
    }
    if request.method == 'POST':
        formulario = PerifericosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'perifericos.html', data)


def listarperifericos(request):
    listar = Perifericos.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'listarperifericos.html', data)

def modificarperisferico(request, id):
    perisfericos = get_object_or_404(Perifericos, id=id)

    data = {
        'form':PerifericosForm(instance=perisfericos)
    }
    if request.method == 'POST':
        formulario = PerifericosForm(data=request.POST, instance=perisfericos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarperifericos")
        data["form"] = formulario

    return render(request, 'modificarperisfericos.html', data)

def eliminarperisfericos(request, id):
    eliminarperisferico = get_object_or_404(Perifericos, id=id)
    eliminarperisferico.delete()
    return redirect(to="listarperifericos")



def impresoras(request):
    data = {
        'form': ImpresorasForm()
    }
    if request.method == 'POST':
        formulario = ImpresorasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'impresoras.html', data)


def listarimpresoras(request):
    listar = Impresoras.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'listarimpresoras.html', data)


def modificarimpresoras(request, id):
    impresoras = get_object_or_404(Impresoras, id=id)

    data = {
        'form':PerifericosForm(instance=impresoras)
    }
    if request.method == 'POST':
        formulario = ImpresorasForm(data=request.POST, instance=impresoras)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarimpresoras")
        data["form"] = formulario

    return render(request, 'modificarimpresoras.html', data)

def eliminarimpresoras(request, id):
    eliminarimpresora = get_object_or_404(Impresoras, id=id)
    eliminarimpresora.delete()
    return redirect(to="listarimpresoras")





def telefonia(request):
    data = {
        'form': TelefoniaForm()
    }
    if request.method == 'POST':
        formulario = TelefoniaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'telefonia.html', data)


def listartelefonia(request):
    listar = Telefonia.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'listartelefonia.html', data)


def modificartelefonia(request, id):
    telefonia = get_object_or_404(Telefonia, id=id)

    data = {
        'form':PerifericosForm(instance=telefonia)
    }
    if request.method == 'POST':
        formulario = TelefoniaForm(data=request.POST, instance=telefonia)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listartelefonia")
        data["form"] = formulario

    return render(request, 'modificartelefonia.html', data)


def eliminartelefonia(request, id):
    eliminartelefonia = get_object_or_404(Telefonia, id=id)
    eliminartelefonia.delete()
    return redirect(to="listartelefonia")



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request)
            messages.success(request, "Te has registrado en forma exitosa")
            return redirect(to="login")
        data["form"] = formulario
    return render(request, './registration/registro.html', data)


def personas(request):
    data = {
        'form': PersonasForm()
    }
    if request.method == 'POST':
        formulario = PersonasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'personas.html', data)

def listarpersonas(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Equipos.objects.filter(persona__icontains=q)
    else:
        data = Equipos.objects.all()
    context = {
        'data': data
    }

    listar = Persona.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'buscarpersona.html', context)


def detalle(request):
    return render(request, 'detalle.html')






