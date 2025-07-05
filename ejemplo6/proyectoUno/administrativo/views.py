from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.db.models import Sum # Necesario para el cálculo de sumas directamente en la BD

# importar las clases de models.py
from administrativo.models import Matricula, Estudiante, Modulo 
# Importar los nuevos formularios
from administrativo.forms import MatriculaForm, MatriculaEditForm, EstudianteForm, ModuloForm 

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    """
    """
    matriculas = Matricula.objects.all()

    titulo = "Listado de matrículas"
    informacion_template = {'matriculas': matriculas,
    'numero_matriculas': len(matriculas), 'mititulo': titulo}
    return render(request, 'index.html', informacion_template)


def detalle_matricula(request, id):
    """

    """

    matricula = Matricula.objects.get(pk=id)
    informacion_template = {'matricula': matricula}
    return render(request, 'detalle_matricula.html', informacion_template)


def crear_matricula(request):
    """
    """
    if request.method=='POST':
        formulario = MatriculaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MatriculaForm()
    diccionario = {'formulario': formulario, 'titulo_formulario': 'Crear Nueva Matrícula'} # Añadido título
    return render(request, 'crear_matricula.html', diccionario)

def editar_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    print("----------matricula")
    print(matricula)
    print("----------matricula")
    if request.method=='POST':
        formulario = MatriculaEditForm(request.POST, instance=matricula)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MatriculaEditForm(instance=matricula)
    diccionario = {'formulario': formulario, 'titulo_formulario': 'Editar Matrícula'} # Añadido título
    return render(request, 'crear_matricula.html', diccionario) # Se reutiliza el template de crear


def detalle_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    informacion_template = {'e': estudiante}
    return render(request, 'detalle_estudiante.html', informacion_template)


# -----------------------------------------------------------------------------
# NUEVAS VISTAS PARA MODULOS
# -----------------------------------------------------------------------------

def listar_modulos(request):
    """
    Vista que permite presentar el listado de módulos con su información.
    Incluye el valor total de las matrículas asociadas a cada módulo.
    """
    # Usamos annotate con Sum para calcular el costo total directamente en la consulta a la BD
    modulos = Modulo.objects.annotate(
        valor_total_matriculas=Sum('lasmatriculas__costo')
    )
    
    titulo = "Listado de Módulos"
    informacion_template = {
        'modulos': modulos, # Cambiamos el nombre de la variable para simplicidad en el template
        'numero_modulos': len(modulos),
        'mititulo': titulo
    }
    return render(request, 'listar_modulos.html', informacion_template)


def crear_modulo(request):
    """
    Vista para crear un nuevo módulo.
    """
    if request.method == 'POST':
        formulario = ModuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_modulos') # Redirigir a la lista de módulos por su nombre
    else:
        formulario = ModuloForm()
    
    diccionario = {'formulario': formulario, 'titulo_formulario': 'Crear Nuevo Módulo'}
    return render(request, 'crear_modulo.html', diccionario)



def listar_estudiantes(request):
    """
    Vista que permite presentar el listado de estudiantes con su información detallada.
    Incluye el costo total de matrículas de cada estudiante.
    """
    # Usamos annotate con Sum para calcular el costo total directamente en la consulta a la BD
    estudiantes = Estudiante.objects.annotate(
        costo_total_matriculas=Sum('lasmatriculas__costo')
    )
    
    titulo = "Listado de Estudiantes"
    informacion_template = {
        'estudiantes': estudiantes, # Cambiamos el nombre de la variable para simplicidad en el template
        'numero_estudiantes': len(estudiantes),
        'mititulo': titulo
    }
    return render(request, 'listar_estudiantes.html', informacion_template)


def crear_estudiante(request):
    """
    Vista para crear un nuevo estudiante.
    """
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_estudiantes') # Redirigir a la lista de estudiantes por su nombre
    else:
        formulario = EstudianteForm()
    
    diccionario = {'formulario': formulario, 'titulo_formulario': 'Crear Nuevo Estudiante'}
    return render(request, 'crear_estudiante.html', diccionario)