from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Usuario, ModuloAccesibilidad, ConfiguracionAccesibilidad, ControlContraste, ControlTamañoTexto, RecursosInclusion

# Vistas para ConfiguracionAccesibilidad
class ConfiguracionAccesibilidadListView(ListView):
    model = ConfiguracionAccesibilidad
    template_name = 'accesibilidad/configuracion_list.html'

class ConfiguracionAccesibilidadCreateView(CreateView):
    model = ConfiguracionAccesibilidad
    fields = '__all__'
    template_name = 'accesibilidad/configuracion_form.html'
    success_url = reverse_lazy('configuracion_list')

class ConfiguracionAccesibilidadUpdateView(UpdateView):
    model = ConfiguracionAccesibilidad
    fields = '__all__'
    template_name = 'accesibilidad/configuracion_form.html'
    success_url = reverse_lazy('configuracion_list')

class ConfiguracionAccesibilidadDeleteView(DeleteView):
    model = ConfiguracionAccesibilidad
    template_name = 'accesibilidad/configuracion_confirm_delete.html'
    success_url = reverse_lazy('configuracion_list')

class ConfiguracionAccesibilidadDetailView(DetailView):
    model = ConfiguracionAccesibilidad
    template_name = 'accesibilidad/configuracion_detail.html'