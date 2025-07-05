from django.forms import ModelForm
from django import forms

from administrativo.models import Matricula, Modulo, Estudiante


class MatriculaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...',
                'class': 'form-control'
            }), }


class ModuloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Modulo
        fields = ['nombre']


class EstudianteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Estudiante
        fields = ['nombre', 'nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']