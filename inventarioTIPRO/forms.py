from django import forms
from .models import Equipos, Monitores, Perifericos, Impresoras, Telefonia, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquiposForm(forms.ModelForm):

    class Meta:
        model = Equipos
        fields = '__all__'

class MonitoresForm(forms.ModelForm):

    class Meta:
        model = Monitores
        fields = '__all__'

class PerifericosForm(forms.ModelForm):

    class Meta:
        model = Perifericos
        fields = '__all__'


class ImpresorasForm(forms.ModelForm):

    class Meta:
        model = Impresoras
        fields = '__all__'


class TelefoniaForm(forms.ModelForm):

    class Meta:
        model = Telefonia
        fields = '__all__'

class PersonasForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_permissions']


