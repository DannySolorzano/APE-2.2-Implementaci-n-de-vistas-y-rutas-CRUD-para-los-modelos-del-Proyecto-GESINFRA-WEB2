from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Usuario, TipoEquipo, EstadoEquipo, Ubicacion, Responsable, Proveedor, Equipo

# Vistas para Equipo (modelo principal)
class EquipoListView(ListView):
    model = Equipo
    template_name = 'inventario/equipo_list.html'

class EquipoCreateView(CreateView):
    model = Equipo
    fields = '__all__'
    template_name = 'inventario/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

class EquipoUpdateView(UpdateView):
    model = Equipo
    fields = '__all__'
    template_name = 'inventario/equipo_form.html'
    success_url = reverse_lazy('equipo_list')

class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'inventario/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo_list')

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'inventario/equipo_detail.html'

