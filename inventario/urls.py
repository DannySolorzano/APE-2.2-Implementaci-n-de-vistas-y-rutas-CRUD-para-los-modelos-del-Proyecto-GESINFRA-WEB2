"""
URL configuration for gesinfraweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # URLs para Equipo
    path('equipo/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipo/nuevo/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('equipo/<int:pk>/editar/', views.EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipo/<int:pk>/eliminar/', views.EquipoDeleteView.as_view(), name='equipo_delete'),

    # ... URLs para los demás modelos (Usuario, TipoEquipo, etc.)
    ]