from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipos, Monitores, Perifericos
from .forms import EquiposForm, MonitoresForm, PerifericosForm, CustomUserCreationForm
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

    return render(request, 'Equipos/equipos.html', data)


def listarequipos(request):

    listar = Equipos.objects.all()

    data = {
        'listar': listar,
    }
    return render(request, 'Equipos/listarequipos.html', data)


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

    return render(request, 'Equipos/modificarequipos.html', data)


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

    return render(request, 'Monitores/monitores.html', data)


def listarmonitores(request):
    listar = Monitores.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'Monitores/listarmonitores.html', data)


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

    return render(request, 'Monitores/modificarmonitores.html', data)


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

    return render(request, 'Perifericos/perifericos.html', data)


def listarperifericos(request):
    listar = Perifericos.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'Perifericos/listarperifericos.html', data)

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

    return render(request, 'Perifericos/modificarperisfericos.html', data)

def eliminarperisfericos(request, id):
    eliminarperisferico = get_object_or_404(Perifericos, id=id)
    eliminarperisferico.delete()
    return redirect(to="listarperifericos")



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


def detalle(request):
    return render(request, 'detalle.html')






