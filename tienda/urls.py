from django.urls import path
from . import views

urlpatterns = [
    # Catálogos por categoría
    path('collares/', views.collares, name='collares'),
    path('anillos/', views.anillos, name='anillos'),
    path('aretes/', views.aretes, name='aretes'),
    path('pulseras/', views.pulseras, name='pulseras'),

    # Carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('actualizar/<int:producto_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('quitar/<int:producto_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),

    # Pago y confirmación
    path('checkout/', views.checkout, name='checkout'),
    path('confirmar-pedido/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmacion/<int:pedido_id>/', views.confirmacion_pedido, name='confirmacion_pedido'),
]

