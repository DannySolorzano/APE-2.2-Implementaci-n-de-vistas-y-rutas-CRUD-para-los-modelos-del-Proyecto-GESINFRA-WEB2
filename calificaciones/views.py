from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Institucion, Docente, NivelEducativo, Estudiante, Paralelo, Directivo, Calificacion

# Vistas para Institucion
class InstitucionListView(ListView):
    model = Institucion
    template_name = 'calificaciones/institucion_list.html'

class InstitucionCreateView(CreateView):
    model = Institucion
    fields = '__all__'
    template_name = 'calificaciones/institucion_form.html'
    success_url = reverse_lazy('institucion_list')

class InstitucionUpdateView(UpdateView):
    model = Institucion
    fields = '__all__'
    template_name = 'calificaciones/institucion_form.html'
    success_url = reverse_lazy('institucion_list')

class InstitucionDeleteView(DeleteView):
    model = Institucion
    template_name = 'calificaciones/institucion_confirm_delete.html'
    success_url = reverse_lazy('institucion_list')

class InstitucionDetailView(DetailView):
    model = Institucion
    template_name = 'calificaciones/institucion_detail.html'

# Vistas para Docente (similar para los demás modelos)
class DocenteListView(ListView):
    model = Docente
    template_name = 'calificaciones/docente_list.html'

class DocenteCreateView(CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'calificaciones/docente_form.html'
    success_url = reverse_lazy('docente_list')

class DocenteUpdateView(UpdateView):
    model = Docente
    fields = '__all__'
    template_name = 'calificaciones/docente_form.html'
    success_url = reverse_lazy('docente_list')

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'calificaciones/docente_confirm_delete.html'
    success_url = reverse_lazy('docente_list')

class DocenteDetailView(DetailView):
    model = Docente
    template_name = 'calificaciones/docente_detail.html'

# ... Repetir para los demás modelos (NivelEducativo, Estudiante, Paralelo, Directivo, Calificacion)

# Vistas para Calificacion
class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificaciones/calificacion_list.html'

class CalificacionCreateView(CreateView):
    model = Calificacion
    fields = '__all__'
    template_name = 'calificaciones/calificacion_form.html'
    success_url = reverse_lazy('calificacion_list')

class CalificacionUpdateView(UpdateView):
    model = Calificacion
    fields = '__all__'
    template_name = 'calificaciones/calificacion_form.html'
    success_url = reverse_lazy('calificacion_list')

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificaciones/calificacion_confirm_delete.html'
    success_url = reverse_lazy('calificacion_list')

class CalificacionDetailView(DetailView):
    model = Calificacion
    template_name = 'calificaciones/calificacion_detail.html'