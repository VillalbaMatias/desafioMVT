from django.contrib import admin
from django.urls import path
#from .views import mostrar_familiares
from Familiar import views

urlpatterns = [
    #path('mostrar_familiares/', mostrar_familiares)
    path('mostrar_familiar_html/', views.render_vista_familiar)
]
