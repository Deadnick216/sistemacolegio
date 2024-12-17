from django import forms
from .models import Estudiante, Docente, Nodocente, Asignatura, Evento, Anotacion, Nota, Reclamo
from django.db import models
class LoginDocenteForm(forms.Form):
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginNodocenteForm(forms.Form):
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'correo', 'rut', 'tipo']

class CreateDocenteForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Docente
        fields = ['nombre', 'correo', 'contrasena', 'rut', 'tipo']

class CreateNodocenteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Nodocente
        fields = ['nombre', 'correo', 'password', 'rut', 'tipo', 'descripcion']

class CreateAsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'descripcion']

class AssignAsignaturaForm(forms.Form):
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), label="Estudiante")
    asignatura = forms.ModelMultipleChoiceField(queryset=Asignatura.objects.all(), label="Asignaturas")

class CreateEventoForm(forms.ModelForm):
    fecha = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'datetimepicker'}))

    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha']

class CreateAnotacionForm(forms.ModelForm):
    class Meta:
        model = Anotacion
        fields = ['fecha', 'descripcion']


class CreateNotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota']
        widgets = {
            'nota': forms.NumberInput(attrs={'step': '0.1', 'lang': 'es'}),  # Permitir decimales
        }

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['docente', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }