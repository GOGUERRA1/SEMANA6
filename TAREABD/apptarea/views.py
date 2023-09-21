from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def get_productos(request):
    listado_productos = Producto.objects.order_by("descripcion")
    context = {"listado": listado_productos}
    return render(request, "productos.html", context)

def add_producto(request):
    if request. method == 'GET':
        context = { "form": ProductoForm() }
        return render(request, "add_producto.html", context)
    
    elif request.method == 'POST':
        producto_form = ProductoForm(data=request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect(reverse("get_productos")) 
        else:
            producto_form = ProductoForm()
            context = {"error" : "Existen errores en el formulario"}
            return render(request, "add_producto.html", context)
