from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Respuesta,Informe

class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Respuesta
        fields = (
            'encuesta',
            'respuesta',
            )
class InformeForm(forms.ModelForm):

    class Meta:
        model = Informe
        fields = (
            'titulo',
            'descripcion',
            'foto',
            )

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'rut',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            )

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')