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

app_name = 'accesibilidad'

urlpatterns = [
    # URLs para ConfiguracionAccesibilidad
    path('configuracion/', views.ConfiguracionAccesibilidadListView.as_view(), name='configuracion_list'),
    path('configuracion/nuevo/', views.ConfiguracionAccesibilidadCreateView.as_view(), name='configuracion_create'),
    path('configuracion/<int:pk>/', views.ConfiguracionAccesibilidadDetailView.as_view(), name='configuracion_detail'),
    path('configuracion/<int:pk>/editar/', views.ConfiguracionAccesibilidadUpdateView.as_view(), name='configuracion_update'),
    path('configuracion/<int:pk>/eliminar/', views.ConfiguracionAccesibilidadDeleteView.as_view(), name='configuracion_delete'),

    # ... URLs para los demás modelos
]