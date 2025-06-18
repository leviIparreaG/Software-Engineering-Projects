
from urllib import request
from django.shortcuts import HttpResponse, get_object_or_404
from django.shortcuts import render
from .models import Estudiante, Grupo  # <---- Asegúrate de importar los modelos aquí
from .forms import NewForm


# Create your views here.


'''

def mi_funcion(request):
    
    estudiantes = []
    form = NewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['lastName']
        cuenta = form.cleaned_data['num_cuenta']

        print(nombre, apellido, cuenta)

        if nombre:
            estudiantes = Estudiante.objects.filter(nombres__icontains=nombre)
        elif apellido:
            estudiantes = Estudiante.objects.filter(apellidos__icontains=apellido)
        elif cuenta:
            estudiantes = Estudiante.objects.filter(numCta__icontains=cuenta)

        # Si no hay ningún filtro, se muestran todos
        if not nombre and not apellido and not cuenta:
            estudiantes = Estudiante.objects.all()

    elif request.method == 'POST':
        print('No hay resultados')

    return render(request, 'index.html', {
        'form': form,
        'estudiantes': estudiantes
    })
'''

'''
numCnta|   nombres      |   apellidos   |    grupos   |
-------------------------------------------------------
  314  |    César       |    Jardines   | 1 (id_grupo)|
'''
def index(request):
    estudiantes = []
    form = NewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['lastName']
        cuenta = form.cleaned_data['num_cuenta']

        if nombre:
            estudiantes = Estudiante.objects.filter(nombres__icontains=nombre).order_by('apellidos','nombres')
        elif apellido:
            estudiantes = Estudiante.objects.filter(apellidos__icontains=apellido).order_by('apellidos','nombres')
        elif cuenta:
            estudiantes = Estudiante.objects.filter(numCta__icontains=cuenta).order_by('apellidos','nombres')

        if not nombre and not apellido and not cuenta:
            # Si no se ingresó ningún filtro, mostrar todos
            estudiantes = Estudiante.objects.all().order_by('apellidos', 'nombres')

    else:
        # Si es GET o el POST no es válido, mostrar todos
        estudiantes = Estudiante.objects.all().order_by('apellidos', 'nombres')

    return render(request, "index.html", {
        "form": form,
        "estudiantes": estudiantes
})


def detalle_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    grupos = estudiante.grupos.all()
    return render(request, "detalle_estudiante.html", {
        "estudiante": estudiante,
        "grupos": grupos,
})



def tontines(re):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 33
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Hurtado Aponte Joshua Abel,Felipe Ramírez Alondra Navila, Flores Muñoz Mauricio, Mendiola Montes Victor Manuel")

def cums(request):
    '''
    1.- Todos los estudiantes con nombres Victor Manuel
    2.- Todos los estudiantes con numCta 320
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Perez Aparicio Ariadna Beatriz, Garcia Gommez Eduardo Biali")

def ejercicio1(request):
    nombre = Estudiante.objects.filter(nombres="Moisés")
    estudiantes = Estudiante.objects.filter(numCta=318)

    moises = "<br>".join([f"{estudiante.nombres} {estudiante.apellidos} - {estudiante.numCta}" for estudiante in nombre])
    estudiantes_318 = "<br>".join([f"{estudiante.nombres} {estudiante.apellidos} - {estudiante.numCta}" for estudiante in estudiantes])
    integrantes_equipo = ["Levi Iparrea", "Vazquez Jose", "Barradas Alberto"]

    resultado = f"""
    Informacion de estudiantes llamados Moisés:
    <br>
       {moises}
    <br>
    <br>
    Estudiantes con numCta 318: 
    <br>
        {estudiantes_318}
    <br>
    <br>
    Integrantes del equipo:
    <br>
      {integrantes_equipo}
    """
      
    '''
    1.- Todos los estudiantes con nombres Moisés
    2.- Todos los estudiantes con numCta 318
    3.- Los integrantes de este equipo
    '''
    return render(request, "index.html", {
        "estudiantes_moises": moises,
        "estudiante_318": estudiantes_318,
        "integrantes_equipo": integrantes_equipo
    })

def equipo_n(request):
    '''
    1.- Todos los estudiantes con apellidos Martínez
    2.- Todos los estudiantes con numCta 42
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Alcantara Andrade Daniel, Rodriguez Nevarez Edwin, Sanchez Rosas Roberto Samuel, Cataneo Tortolero Andres Rodrigo")

def ekiposupercool(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 33
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("López Asano Miguel Akira, Martínez Marcelo Ingrid Aylen, Pérez Evristo Eris, Ramírez Venegas Alexa Paola")
    
def space4(request):
    '''
    1.- Todos los estudiantes con nombres Victor Manuel
    2.- Todos los estudiantes con numCta 320
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("del Valle Vera Nancy Elena, Ugalde Flores Jimena, Cruz Gonzalez Irvin Javie")

def Dinamita(requestt):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Maro Flores Cid, Etni Sarai Castro Sierra, Moises Corpus Garcia, Moises Abraham Lira Rivera")

def ekuipo(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Castillo Camacho Violeta Ardeni, \n Juarez Cruz Joshua\n Kevin Steve Quezada Ordoñez\n karla Clemente Herrera") 

def Labubusalvajes(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 33
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Alan Oliver Lopez Robles, Dylan Enrique Juarez Martinez")  

def indez(request):
    '''
    1.- Todos los estudiantes con nombres Victor Manuel
    2.- Todos los estudiantes con numCta 320
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Luis Gerardo Estrada Garcia, Luis Ernesto Hernandez Rosas, Uziel Vidal Cruz, Yuznhio Sierra Casiano")

def index1(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Antonio Castillo Hernandez, Sergio Mejia Caballero, Ixchel Velazquez Vilchis")

def foo(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Ramón Arcos Morales, Victor Manuel Casarrubias Casarrubias")

def us(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 33
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("'Mildred, Leslie, Aldo, Francisco'")

def equipoPerdido1(request):
    '''
    1.- Todos los estudiantes con nombres Victor Manuel
    2.- Todos los estudiantes con numCta 320
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Luis Ernesto Hernández Rosas, Luis Gerardo, Yuznhio, Uziel Vidal")

def URLEquipo(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Ixchell, Atonio, Sergio")

def ekipo(request):
    '''
    1.- Todos los estudiantes
    2.- Todos los estudiantes con numCta 319
    3.- Los integrantes de este equipo
    '''
    return HttpResponse("Itzel, Raúl, Josue")