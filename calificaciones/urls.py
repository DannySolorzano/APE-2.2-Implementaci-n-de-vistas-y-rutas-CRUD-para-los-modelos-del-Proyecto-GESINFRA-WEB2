from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='calificaciones_index'),
    # Agrega más rutas según necesites
]