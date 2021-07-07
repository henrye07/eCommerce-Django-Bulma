from django.urls import path
from . import views

app_name='sitio'
urlpatterns = [
    path('', views.index,name='index'),
    path('categories/<int:id>', views.category,name='categorias'),
    path('categories/', views.category,name='buscar'),
    path('about/',views.aboutus,name="acerca"),
    path('contact/', views.contact,name='contacto'),
    path('new_product/', views.new_product,name='nuevoProducto'),
    path('carrito/',views.carrito,name='carrito'),
    path('register/', views.register,name='register'),
    path('product/<int:id>', views.product,name='producto'),
    path('product/edit/<int:id>', views.product_edit,name='productEdit'),
    path('carrito/agregar/<int:id>', views.agregar_producto,name='agregar'),
    path('carrito/eliminar/<int:id>', views.eliminar_producto,name='eliminar'),
    path('carrito/restar/<int:id>', views.restar_producto,name='restar'),
    path('carrito/limpiar/', views.limpiar_carro,name='limpiar'),
    
]
