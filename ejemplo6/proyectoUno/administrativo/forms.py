from django.forms import ModelForm
from django import forms

# Importar los nuevos modelos
from administrativo.models import Matricula, Estudiante, Modulo

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo'] # AHORA INCLUYE 'costo'


class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo'] # AHORA INCLUYE 'costo'
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),}


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        # Puedes añadir widgets o etiquetas personalizadas si es necesario
        labels = {
            'nombre': 'Nombre del Estudiante',
            'apellido': 'Apellido del Estudiante',
            'cedula': 'Número de Cédula',
            'edad': 'Edad',
            'tipo_estudiante': 'Tipo de Estudiante',
        }

class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre'] 
                            
        labels = {
            'nombre': 'Nombre del Módulo (ej. Primero, Segundo)',
        }