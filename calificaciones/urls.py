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

app_name = 'calificaciones'

urlpatterns = [
    # URLs para Institucion
    path('institucion/', views.InstitucionListView.as_view(), name='institucion_list'),
    path('institucion/nuevo/', views.InstitucionCreateView.as_view(), name='institucion_create'),
    path('institucion/<int:pk>/', views.InstitucionDetailView.as_view(), name='institucion_detail'),
    path('institucion/<int:pk>/editar/', views.InstitucionUpdateView.as_view(), name='institucion_update'),
    path('institucion/<int:pk>/eliminar/', views.InstitucionDeleteView.as_view(), name='institucion_delete'),

    # URLs para Docente
    path('docente/', views.DocenteListView.as_view(), name='docente_list'),
    path('docente/nuevo/', views.DocenteCreateView.as_view(), name='docente_create'),
    path('docente/<int:pk>/', views.DocenteDetailView.as_view(), name='docente_detail'),
    path('docente/<int:pk>/editar/', views.DocenteUpdateView.as_view(), name='docente_update'),
    path('docente/<int:pk>/eliminar/', views.DocenteDeleteView.as_view(), name='docente_delete'),

    # ... URLs para los demás modelos (NivelEducativo, Estudiante, Paralelo, Directivo, Calificacion)
]