from typing import List
from django.db.models.query import QuerySet
import json
from django.http import JsonResponse
from django.shortcuts import render
from miMascotasorgApp.forms import FormularioContacto
from miMascotasorgApp.models import Alimentacion, Alojamiento, Consejos, Entrenamiento, Legal, Otros, Sanitario, caballo, gato, pajaro, peces, perro
from django.db.models import Q
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator

# ----------------------------- VISTAS ------------------------------------
def home(request):
    return render(request, 'menu/home.html')

def servicios(request):
    return render(request, 'menu/servicios.html', {'nbar': 'servicios'})

# Devuelve cualquier noticias en funcion al tipo de servicio, también se filtra por busqueda
def tipoServicio(request, tipo):    
    lista_noticias = ""
    resultado = 0
    volver = ""
    lista_base = ['Legales', 'Sanitarios', 'Alimentacion', 'Alojamiento', 'Entrenamiento', 'Otros']
    lista = list(filter(lambda x: (x != tipo), lista_base))

    if request.POST:
        request.session['buscar'] = request.POST.get('buscar')
        lista_noticias = filtro_busqueda(tipo, request.POST.get('buscar'))    
        resultado = lista_noticias.count
        volver = 'true'
    else:
        if request.GET.get('page') == None:
            request.session['buscar'] = None
            lista_noticias = serviciosAll(tipo)               
            resultado = lista_noticias.count
            volver = 'false'             
        else:
            if(request.session['buscar'] != None):
                lista_noticias = filtro_busqueda(tipo, request.session['buscar']) 
                volver = 'true'
            else:
                lista_noticias = filtro_busqueda(tipo, "")
                volver = 'false'
            resultado = lista_noticias.count
            volver = 'true'
                                
    paginator = Paginator(lista_noticias, 1)
    page = request.GET.get('page') or 1
    page_actual = int(page)
    lista_noticias = paginator.get_page(page)
    paginas = range(1, lista_noticias.paginator.num_pages + 1)
    print(lista)
    return render(request, 'servicios/tipo-servicios.html', {'items': lista_noticias, 'tipo':tipo, 'lista':lista, 'paginas': paginas, 'pagina_actual': page_actual, 'pagina': page, 'resultado': resultado, 'buscar':request.session['buscar'], 'volver': volver})

# Devuelve cualquier consejo, también se filtra por keyword
def consejos(request):
    lista_consejos = ""
    resultado = 0
    volver = ""

    if request.POST:
        request.session['buscar'] = request.POST.get('buscar')
        lista_consejos = filtro_busqueda_consejos(request.POST.get('buscar'))    
        resultado = lista_consejos.count
        volver = 'true'
    else:
        if request.GET.get('page') == None:
            request.session['buscar'] = None
            lista_consejos = Consejos.objects.get_queryset().order_by('id')              
            resultado = lista_consejos.count
            volver = 'false'             
        else:
            if(request.session['buscar'] != None):
                lista_consejos = filtro_busqueda_consejos(request.session['buscar']) 
                volver = 'true'
            else:
                lista_consejos = filtro_busqueda_consejos("")
                volver = 'false'
            resultado = lista_consejos.count
            
                                
    paginator = Paginator(lista_consejos, 1)
    page = request.GET.get('page') or 1
    page_actual = int(page)
    lista_consejos = paginator.get_page(page)
    paginas = range(1, lista_consejos.paginator.num_pages + 1)

    return render(request, 'menu/consejos.html', {'nbar':'consejos', 'items': lista_consejos, 'paginas': paginas, 'pagina_actual': page_actual, 'pagina': page, 'resultado': resultado, 'buscar':request.session['buscar'], 'volver': volver})


def detalleConsejo(request, id):
    consejo = Consejos.objects.get(id=id)
    return render(request, 'consejos/detalle-consejo.html', {'consejo': consejo})


def mascotas(request):
    return render(request, 'menu/mascotas.html', {'nbar': 'mascotas'})

# Devuelve json de las mascotas y se pinta en el JS
def tipoMascotas(request, tipo):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        lista_mascotas = []
        for mascota in mascotasAll(tipo):
            data_mascota = {}
            data_mascota['id'] = mascota.id
            data_mascota['tipo'] = mascota.tipo
            data_mascota['nombre'] = mascota.nombre
            data_mascota['caracter'] = mascota.caracter
            data_mascota['altura'] = mascota.altura
            data_mascota['peso'] = mascota.peso
            data_mascota['salud'] = mascota.salud
            data_mascota['observaciones'] = mascota.observaciones
            data_mascota['imagen'] = str(mascota.imagen)
            lista_mascotas.append(data_mascota)
        data = json.dumps(lista_mascotas)
        return JsonResponse({'lista': data})
    return render(request, 'mascotas/tipo-mascotas.html', {'tipo': tipo})


def contacto(request):
    if request.POST:
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            template = get_template('correo/correo.html')
            contenido = template.render(
                {'nombre': formulario_contacto.cleaned_data['nombre'], 'email': formulario_contacto.cleaned_data['email'], 'mensaje': formulario_contacto.cleaned_data['mensaje']})
            mail = EmailMultiAlternatives(
                'Contacto cliente', '', settings.EMAIL_HOST_USER, ['contacto@mimascotas.org'])
            mail.attach_alternative(contenido, 'text/html')
            mail.send()
            # send_mail(formulario_contacto.cleaned_data['asunto'], "Nombre: " + formulario_contacto.cleaned_data['mensaje'] + "\nCorreo electrónico: " + formulario_contacto.cleaned_data ['email'] + "\nMensaje: " + formulario_contacto.cleaned_data['mensaje'], settings.EMAIL_HOST_USER, ['contacto@mimascotas.org'])
            formulario_contacto = FormularioContacto()
            return render(request, 'menu/contacto.html', {'nbar': 'contacto', 'form': formulario_contacto, 'success': 'true'})
        else:
            pass
    else:
        formulario_contacto = FormularioContacto()
    return render(request, 'menu/contacto.html', {'nbar': 'contacto', 'form': formulario_contacto})


def foro(request):
    return render(request, 'menu/foro.html')


def detalleServicio(request, tipo, id):
    lista_base = ['Legales', 'Sanitarios', 'Alimentacion',
                  'Alojamiento', 'Entretenimiento', 'Otros']
    lista = list(filter(lambda x: (x != tipo), lista_base))
    if tipo == 'Legales':
        noticias = Legal.objects.get(id=id)
    elif tipo == 'Sanitarios':
        noticias = Sanitario.objects.get(id=id)
    return render(request, 'servicios/detalleServicios.html', {'noticia': noticias, 'tipo': tipo, 'lista': lista, 'volver': 'true'})

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request, *args, **argv):
    return render(request, '500.html', status=500)

#--------------- MÉTODOS -----------------

def filtro_busqueda(tipo, buscar):

    if tipo == 'Legales':

        noticias = Legal.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    elif tipo == 'Sanitarios':

        noticias = Sanitario.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    elif tipo == 'Alimentacion':

        noticias = Alimentacion.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    elif tipo == 'Alojamiento':

        noticias = Alojamiento.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    elif tipo == 'Entrenamiento':

        noticias = Entrenamiento.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    elif tipo == 'Otros':

        noticias = Otros.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(subtitulo__icontains=buscar) |
            Q(detalle__icontains=buscar)
        ).distinct()

    return noticias

def filtro_busqueda_consejos(buscar):

    consejos = Consejos.objects.filter(
        Q(keyword__icontains=buscar)
    ).distinct()

    return consejos

def serviciosAll(tipo):    
    if tipo == 'Legales':
        noticias = Legal.objects.get_queryset().order_by('id') 
    elif tipo == 'Sanitarios':
        noticias = Sanitario.objects.get_queryset().order_by('id') 
    elif tipo == 'Alimentacion':
        noticias = Alimentacion.objects.get_queryset().order_by('id') 
    elif tipo == 'Alojamiento':
        noticias = Alojamiento.objects.get_queryset().order_by('id') 
    elif tipo == 'Entrenamiento':
        noticias = Entrenamiento.objects.get_queryset().order_by('id') 
    elif tipo == 'Otros':
        noticias = Otros.objects.get_queryset().order_by('id') 
    return noticias

def mascotasAll(tipo):
    if tipo == 'perros':
        mascotas = perro.objects.all()
    elif tipo == 'gatos':
        mascotas = gato.objects.all()
    elif tipo == 'caballos':
        mascotas = caballo.objects.all()
    elif tipo == 'peces':
        mascotas = peces.objects.all()
    elif tipo == 'pajaros':
        mascotas = pajaro.objects.all()
    return mascotas
