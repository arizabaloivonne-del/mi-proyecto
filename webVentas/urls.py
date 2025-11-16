from django.contrib import admin
from django.urls import path, include
from usuarios.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),  # Página principal
    path('admin/', admin.site.urls),

    # App usuarios (registro, login, páginas informativas)
    path('cuentas/', include('usuarios.urls')),

    # Autenticación por defecto de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # App tienda (productos, carrito, pedidos)
    path('tienda/', include('tienda.urls')),
]
