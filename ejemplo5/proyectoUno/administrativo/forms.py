from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Estudiante, \
        NumeroTelefonico

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese apellido por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
        return valor


class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El número debe contener solo dígitos.")
        if len(telefono) != 10:
            raise forms.ValidationError("El número telefónico debe tener exactamente 10 dígitos.")
        return telefono

    def clean_tipo(self):
        tipo = self.cleaned_data['tipo']
        if not tipo:
            raise forms.ValidationError("Debe ingresar un tipo.")
        primera_letra = tipo[0].lower()
        if primera_letra in "aeiou":
            raise forms.ValidationError("El tipo debe comenzar con una consonante.")
        return tipo

class NumeroTelefonicoEstudianteForm(NumeroTelefonicoForm):

    def __init__(self, estudiante, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()

