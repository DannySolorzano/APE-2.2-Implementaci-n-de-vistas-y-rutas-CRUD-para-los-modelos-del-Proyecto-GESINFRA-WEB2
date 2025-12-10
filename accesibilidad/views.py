from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import timezone
import json
from .models import *

def index(request):
    # Obtener o crear configuración para el usuario actual o anónimo
    if request.user.is_authenticated:
        config, created = ConfiguracionAccesibilidad.objects.get_or_create(
            usuario=request.user
        )
    else:
        config, created = ConfiguracionAccesibilidad.objects.get_or_create(
            usuario=None,
            defaults={'token_accesibilidad': 'normal'}
        )
    
    # Obtener datos para mostrar
    terminologias = TerminologiaEspecifica.objects.filter(activo=True)[:5]
    tokens = TokenInmunizacion.objects.filter(activo=True, fecha_expiracion__gt=timezone.now())[:5]
    recursos = RecursoAccesible.objects.filter(activo=True)[:5]
    contenidos = ContenidoAccesible.objects.filter(replicado=True)[:5]
    
    context = {
        'config': config,
        'terminologias': terminologias,
        'tokens': tokens,
        'recursos': recursos,
        'contenidos': contenidos,
        'transiciones_activas': ControlTransicionesTexto.objects.filter(activo=True),
    }
    return render(request, 'accesibilidad/index.html', context)


@csrf_exempt
def actualizar_configuracion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if request.user.is_authenticated:
                config, created = ConfiguracionAccesibilidad.objects.get_or_create(
                    usuario=request.user
                )
            else:
                config, created = ConfiguracionAccesibilidad.objects.get_or_create(
                    usuario=None
                )
            
            # Actualizar configuración
            if 'alto_contraste' in data:
                config.alto_contraste = data['alto_contraste']
            if 'tamanio_fuente' in data:
                config.tamanio_fuente = data['tamanio_fuente']
            if 'lectura_asistida' in data:
                config.lectura_asistida = data['lectura_asistida']
            if 'token_accesibilidad' in data:
                config.token_accesibilidad = data['token_accesibilidad']
            
            config.save()
            
            # Registrar log
            LogAccesibilidad.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                tipo_accion='configuracion',
                descripcion='Configuración de accesibilidad actualizada',
                datos=data
            )
            
            return JsonResponse({
                'success': True,
                'config': {
                    'alto_contraste': config.alto_contraste,
                    'tamanio_fuente': config.tamanio_fuente,
                    'lectura_asistida': config.lectura_asistida,
                    'token_accesibilidad': config.token_accesibilidad,
                }
            })
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})


@login_required
def gestionar_terminologias(request):
    if request.method == 'POST':
        termino = request.POST.get('termino')
        definicion = request.POST.get('definicion')
        categoria = request.POST.get('categoria')
        
        if termino and definicion:
            TerminologiaEspecifica.objects.create(
                termino=termino,
                definicion=definicion,
                categoria=categoria
            )
            messages.success(request, 'Terminología agregada exitosamente')
            return redirect('gestionar_terminologias')
    
    terminologias = TerminologiaEspecifica.objects.all()
    context = {'terminologias': terminologias}
    return render(request, 'accesibilidad/gestionar_terminologias.html', context)


@login_required
def gestionar_transiciones(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        duracion = request.POST.get('duracion', 300)
        efecto = request.POST.get('efecto', 'fade')
        
        if nombre:
            ControlTransicionesTexto.objects.create(
                nombre=nombre,
                duracion=duracion,
                efecto=efecto
            )
            messages.success(request, 'Transición agregada exitosamente')
            return redirect('gestionar_transiciones')
    
    transiciones = ControlTransicionesTexto.objects.all()
    context = {'transiciones': transiciones}
    return render(request, 'accesibilidad/gestionar_transiciones.html', context)


@login_required
def gestionar_tokens(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        fecha_expiracion = request.POST.get('fecha_expiracion')
        
        if nombre and tipo and valor and fecha_expiracion:
            TokenInmunizacion.objects.create(
                nombre=nombre,
                tipo=tipo,
                valor=valor,
                fecha_expiracion=fecha_expiracion
            )
            messages.success(request, 'Token creado exitosamente')
            return redirect('gestionar_tokens')
    
    tokens = TokenInmunizacion.objects.all()
    context = {'tokens': tokens}
    return render(request, 'accesibilidad/gestionar_tokens.html', context)


def replicar_contenido(request, contenido_id):
    contenido = get_object_or_404(ContenidoAccesible, id=contenido_id)
    
    contenido.replicado = True
    contenido.ultima_replicacion = timezone.now()
    contenido.save()
    
    # Registrar log
    LogAccesibilidad.objects.create(
        usuario=request.user if request.user.is_authenticated else None,
        tipo_accion='replicacion',
        descripcion=f'Contenido replicado: {contenido.titulo}',
        datos={'contenido_id': contenido_id, 'titulo': contenido.titulo}
    )
    
    messages.success(request, 'Contenido replicado exitosamente')
    return redirect('index')


def filtrar_recursos(request):
    tipo = request.GET.get('tipo', '')
    
    if tipo:
        recursos = RecursoAccesible.objects.filter(tipo=tipo, activo=True)
    else:
        recursos = RecursoAccesible.objects.filter(activo=True)
    
    tipos = RecursoAccesible.objects.values_list('tipo', flat=True).distinct()
    
    # Registrar log de filtrado
    LogAccesibilidad.objects.create(
        usuario=request.user if request.user.is_authenticated else None,
        tipo_accion='filtro',
        descripcion=f'Filtrado de recursos por tipo: {tipo}',
        datos={'tipo_filtro': tipo, 'resultados': recursos.count()}
    )
    
    context = {
        'recursos': recursos,
        'tipos': tipos,
        'tipo_seleccionado': tipo
    }
    return render(request, 'accesibilidad/filtrar_recursos.html', context)


@login_required
def agregar_recurso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        descripcion = request.POST.get('descripcion')
        linkedin_reunachio = request.POST.get('linkedin_reunachio')
        descriptor = request.POST.get('descriptor')
        almacenamiento_recurrente = request.POST.get('almacenamiento_recurrente') == 'on'
        
        if nombre and tipo and descripcion:
            recurso = RecursoAccesible.objects.create(
                nombre=nombre,
                tipo=tipo,
                descripcion=descripcion,
                linkedin_reunachio=linkedin_reunachio,
                descriptor=descriptor,
                almacenamiento_recurrente=almacenamiento_recurrente
            )
            
            # Agregar filtros si existen
            filtros_tipo = request.POST.getlist('filtro_tipo[]')
            filtros_valor = request.POST.getlist('filtro_valor[]')
            
            for tipo_filtro, valor in zip(filtros_tipo, filtros_valor):
                if tipo_filtro and valor:
                    FiltroRecurso.objects.create(
                        recurso=recurso,
                        tipo_filtro=tipo_filtro,
                        valor=valor
                    )
            
            messages.success(request, 'Recurso agregado exitosamente')
            return redirect('agregar_recurso')
    
    return render(request, 'accesibilidad/agregar_recurso.html')


def leer_contenido(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            texto = data.get('texto', '')
            
            if texto:
                # Registrar log de lectura
                LogAccesibilidad.objects.create(
                    usuario=request.user if request.user.is_authenticated else None,
                    tipo_accion='lectura',
                    descripcion='Lectura asistida activada',
                    datos={'texto_length': len(texto)}
                )
                
                return JsonResponse({
                    'success': True,
                    'mensaje': 'Texto listo para lectura',
                    'texto': texto
                })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})