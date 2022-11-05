from django.shortcuts import render
#from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def render_vista_familiar(request):
    familiar1 = Familiar(dni=12354892, nombre='Lucas Villalba', fecha_nac='1997-05-25', parentezco='Hermano')
    familiar2 = Familiar(dni=90359915, nombre='Oso Melero', fecha_nac='2000-07-07', parentezco='Tio')
    familiar3 = Familiar(dni=40581265, nombre='Ezequiel Gallo', fecha_nac='1990-04-12', parentezco='Abuelo')

    return render(request, 'mostrar_familiar.html', {
        'objetos': [familiar1, familiar2, familiar3]
    })