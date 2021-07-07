from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q

from . import models
from .forms import RegistrationForm,ProductsForm
from .carro import Carro


# Create your views here.
def index(request):
    context={}
    last_products=models.Productos.objects.order_by('-id')[:3]
    products=models.Productos.objects.all()[:7]
    categories=models.Categorias.objects.all()
    context['last']=last_products
    context['first']=products
    context['Categorias']=categories
    return render(request, 'home.html',context)

def category(request,id=None):
    context={}
    products=models.Productos.objects.filter(categoria_pertenece=id)
    categories=models.Categorias.objects.all()
    context['Categorias']=categories
    if request.method=='POST':
        queryset=request.POST.get("buscar")
        products=models.Productos.objects.filter(Q(title__icontains=queryset)|Q(description__icontains=queryset)).distinct()
        context['buscando']=queryset
        context['posts']=products
        
        return render(request, 'category.html',context)      
    context['products']=products
    context['Cate']=models.Categorias.objects.get(id=id)
    return render(request, 'category.html',context)

def aboutus(request):
    context={}
    categories=models.Categorias.objects.all()
    context['Categorias']=categories
    return render(request,'about.html',context)

def contact(request):
    context={}
    categories=models.Categorias.objects.all()
    context['Categorias']=categories
    return render(request, 'contact.html',context)

def new_product(request):
    context={}
    categories=models.Categorias.objects.all()
    if request.method=='POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto Creado Exitosamente!")
            return redirect("/")
        else:
            context['form']=form
            return render(request, 'new_product.html',context) 
    else:
        form = ProductsForm()
    context['form']=form    
    context['Categorias']=categories
    return render(request, 'new_product.html',context)

def carrito(request):
    context={}
    categories=models.Categorias.objects.all()
    context['Categorias']=categories
    return render(request,'carrito.html',context)

def register(request):
    context={}
    categories=models.Categorias.objects.all()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario Registrado con Exito!!")
        return redirect("/")
    else:
        form=RegistrationForm()
    context['form']=form
    context['Categorias']=categories
    return render(request, 'register.html',context)

def product(request,id=None):
    context={}
    categories=models.Categorias.objects.all()
    if id==None:
        all_products=models.Productos.objects.all()
        context['post']=all_products
    else:
        product=models.Productos.objects.get(id=id)
        context['product']=product
    context['Categorias']=categories
    return render(request, 'product.html',context)

def product_edit(request,id):
    context={}
    product=models.Productos.objects.get(id=id)
    categories=models.Categorias.objects.all()
    if request.method=='GET':
        form=ProductsForm(instance=product)
    else:
        form=ProductsForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,f"Se Actualizo con Exito el Producto de nombre:{product.title} - id:{product.id}")
        return redirect('sitio:index')
    context['form']=form
    context['product']=product
    context['Categorias']=categories
    return render(request, 'new_product.html',context)

def product_delete(request,id):
    form=models.Productos.objects.get(id=id)
    if request.method=='POST':
        messages.error(request,f"Se elimino el producto: {form.title}")
        form.delete()
        return redirect("/")

def agregar_producto(request,id):
   
    carro=Carro(request)
    producto=models.Productos.objects.get(id=id)
    carro.agregar(producto=producto)
    return redirect("/carrito")

def eliminar_producto(request,id):
   
    carro=Carro(request)
    producto=models.Productos.objects.get(id=id)
    carro.eliminar(producto=producto)
    return redirect("/carrito")

def restar_producto(request,id):
   
    carro=Carro(request)
    producto=models.Productos.objects.get(id=id)
    carro.restar_producto(producto=producto)
    return redirect("/carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("/carrito")

