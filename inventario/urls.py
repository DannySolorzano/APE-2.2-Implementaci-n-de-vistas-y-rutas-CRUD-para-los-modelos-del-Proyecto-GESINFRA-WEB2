from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventario/', views.listar_equipos, name='listar_equipos'),
    path('inventario/nuevo/', views.crear_equipo, name='crear_equipo'),
    path('inventario/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
]