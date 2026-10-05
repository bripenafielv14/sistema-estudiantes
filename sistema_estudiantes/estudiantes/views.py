from django.shortcuts import render, redirect
from .forms import EstudianteForm
from .models import Estudiante


def inicio(request):
    estudiantes = Estudiante.objects.all()
    form = EstudianteForm()

    return render(request, 'estudiantes/inicio.html', {
        'form': form,
        'estudiantes': estudiantes
    })


def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inicio')

    else:
        form = EstudianteForm()

    return render(request, 'estudiantes/registrar.html', {'form': form})


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/listar.html', {'estudiantes': estudiantes})


def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)

    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)

        if form.is_valid():
            form.save()
            return redirect('inicio')

        estudiantes = Estudiante.objects.all()

        return render(request, 'estudiantes/inicio.html', {
            'form': form,
            'estudiantes': estudiantes
        })

    form = EstudianteForm(instance=estudiante)

    return render(request, 'estudiantes/editar.html', {
        'form': form
    })

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('inicio')