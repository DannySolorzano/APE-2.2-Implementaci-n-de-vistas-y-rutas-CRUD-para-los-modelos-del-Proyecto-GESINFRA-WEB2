from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Equipo
from .forms import EquipoForm

def home(request):
    """Página principal del sistema"""
    return render(request, 'inventario/home.html')

@login_required
def listar_equipos(request):
    """Vista para listar todos los equipos (READ)"""
    equipos = Equipo.objects.all().order_by('-fecha_registro')
    
    # Calcular el valor total de los equipos
    valor_total = 0
    for equipo in equipos:
        valor_total += equipo.precio_adquisicion
    
    context = {
        'equipos': equipos,
        'total_equipos': equipos.count(),
        'valor_total': valor_total
    }
    
    return render(request, 'inventario/listar_equipos.html', context)

@login_required
def crear_equipo(request):
    """Vista para crear un nuevo equipo (CREATE)"""
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.responsable = request.user  # Asignar usuario actual
            equipo.save()
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    
    context = {
        'form': form,
        'titulo': 'Registrar Nuevo Equipo'
    }
    
    return render(request, 'inventario/crear_equipo.html', context)

@login_required
def detalle_equipo(request, equipo_id):
    """Vista para ver detalles de un equipo"""
    equipo = get_object_or_404(Equipo, id=equipo_id)
    
    context = {
        'equipo': equipo
    }
    
    return render(request, 'inventario/detalle_equipo.html', context)

# Create your views here.
