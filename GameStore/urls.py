from django.contrib import admin
from django.urls import path
from primeraApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('videojuegos', views.listadoVideojuegos),
    path('insertarVideojuegos', views.insertarVideojuegos),
    path('eliminarVideojuegos/<int:id>', views.eliminarVideojuegos),
    path('modificarVideojuegos/<int:id>', views.modificarVideojuegos)
]
