from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_accesibilidad'),
    path('actualizar-configuracion/', views.actualizar_configuracion, name='actualizar_configuracion'),
    path('gestionar-terminologias/', views.gestionar_terminologias, name='gestionar_terminologias'),
    path('gestionar-transiciones/', views.gestionar_transiciones, name='gestionar_transiciones'),
    path('gestionar-tokens/', views.gestionar_tokens, name='gestionar_tokens'),
    path('replicar-contenido/<int:contenido_id>/', views.replicar_contenido, name='replicar_contenido'),
    path('filtrar-recursos/', views.filtrar_recursos, name='filtrar_recursos'),
    path('agregar-recurso/', views.agregar_recurso, name='agregar_recurso'),
    path('leer-contenido/', views.leer_contenido, name='leer_contenido'),
]