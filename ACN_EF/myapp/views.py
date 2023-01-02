from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def saludo(request):
    diccionario = {"Titulo": "Saludo",
                    "saludo": "Bienvenidos"}
    return render(request, "saludo.html", diccionario)
 
def integrantes(request):
    integrantes = ["Alagon Vicente, Ronald Aldair", "Caman Gutierrez, Kevin Gabriel", "Navarro Yarleque, Jairo Marcelo"]
    diccionario = {"Titulo": "Integrantes del Proyecto",
                    "integrantes": integrantes}
 
    return render(request, "integrantes.html", diccionario)

def crear_producto(request):
    return render(request, "crear_producto.html")

def crear_curso(request):
    return render(request, "crear_curso.html")

